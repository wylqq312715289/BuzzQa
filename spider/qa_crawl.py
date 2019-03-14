# coding=utf8

import re, os, sys, json, logging, random, time, threading
import sys
from lxml.html import make_links_absolute

reload(sys)
sys.setdefaultencoding('utf-8')

from crawl_data.domain.article.dal.helper import get_springdb_client
from crawl_data.domain.consts.store import SpringTable
from ss_extractor.src.article.extract_util.htmls import build_doc
from pyutil.kafka_proxy.kafka_proxy import KafkaProxy
from pyutil.program import debuginfo, timing, metrics

from utils import crawl, read_redit, put_data2redit, get_md5, list_cut, load_json, store_json
from get_goal_page_info import GoalPageCrawler
from config import Config

# logging.basicConfig(filename="/data00/home/wangyulong.ai/log/qa_logs.txt", level=logging.INFO)
# logging.basicConfig(filename=None, level=logging.INFO)

class QACrawler(object):
    KAFKA_TOPIC_NAME = "crawl_doc_event_buzzqa"
    KAFKA_CLUSTER_NAME = "kafka_main_aws_us"
    KAFKA_CONSUMER_GROUP = "test_get_kafka_data"
    ON_LINE = False
    if ON_LINE:
        version = "V3.5"
        BUZZQA_CRAWL_INFO = 'buzzqa_crawl_info/{}'
        DEBUG = False
        TO_KAFKA = True
    else:
        BUZZQA_CRAWL_INFO = 'buzzqa_crawl_info_test/{}'
        DEBUG = True
        TO_KAFKA = False
    DEFAULT_THREADS_NUM = 3 # 3线程更新站点信息
    DEFAULT_UA_USED = 1
    debug_json_file = "/data00/home/wangyulong.ai/log/qa_info.json"

    def __init__(self, conf):
        self.conf = conf
        self._spring_client = get_springdb_client(SpringTable.crawl_link, socket_timeout=5)
        self.ua_used = int(conf.ua_used) if conf.ua_used else self.DEFAULT_UA_USED
        self.threads_num = int(conf.threads_num) if conf.threads_num else self.DEFAULT_THREADS_NUM
        self.proxies = conf.get_values('squid_proxies')
        self.min_q_len = 2
        # 适应所有站点的xpat配置
        self.web_conf = Config().web_info_config  # type: dict
        # 需要更新的hub站点和xpath模板名称 # type: list
        self.web_seeds = Config().web_seeds
        self.init()

    def init(self):
        if self.DEBUG:
            if os.path.exists(self.debug_json_file):
                os.remove(self.debug_json_file)
            self.test_json = []
            self.debug_log_dict = {}

        if self.web_conf is None:
            logging.warning("QACrawler self.web_conf = None")

        if self.web_seeds is None:
            logging.warning("QACrawler self.web_seeds = None")

        # init kafka
        self.procducer = KafkaProxy(
            topic=self.KAFKA_TOPIC_NAME,
            key_hash=True,
            cluster_name=self.KAFKA_CLUSTER_NAME,
            consumer_group=self.KAFKA_CONSUMER_GROUP,
        )

        self.languages = self.get_languages()
        # init metrics
        for metrics_key in self.web_conf.keys():
            metrics.define_counter(metrics_key+"_received_qa_pair", '')
        metrics.define_counter("abandon_goal_pages", '')
        for metrics_key in self.languages:
            metrics.define_counter(metrics_key + "_q_count", '')
            metrics.define_counter(metrics_key + "_qa_count", '')

    def get_languages(self):
        sources = self.web_conf.keys()
        languages = []
        for source_name in sources:
            lg = self.web_conf.get(source_name).get("language")
            if not lg is None: languages.append(lg)
        languages = list(set(languages))
        return languages

    def process(self):
        while (True):
            sub_sample_list = list_cut(self.web_seeds, self.threads_num)
            threads = []
            for i in range(0, self.threads_num):
                sub_samples = sub_sample_list[i]
                thread = threading.Thread(target=self.handle_task, args=(i, sub_samples))
                thread.start()
                threads.append(thread)
            [t.join() for t in threads]
            log_content = "main thread of instagram end. process web set num is %d" % (len(self.web_seeds))
            logging.info(log_content)
            if self.DEBUG:
                store_json(self.debug_json_file, self.test_json)
                print(self.debug_log_dict)
                break
            else:
                time.sleep(10 * 60) # 10分钟爬取并判断一次hub页
                # print("end epoch")
                # break

    def handle_task(self, batch_index, sub_sources):
        '''
        :param batch_index: 线程id
        :param sub_sources: hub页面(url,format_class)的list
        :return: None
        '''
        for i, web_seed in enumerate(sub_sources, 0):
            url, web_name = web_seed
            hub_page_crawl_interval = self.web_conf.get(web_name).get("crawl_interval")

            # 获取最新更新时间
            mp_uid = get_md5(url)
            redis_key = 'last_crawl_ts_%s' % mp_uid
            redis_key = self.BUZZQA_CRAWL_INFO.format(redis_key)
            value = read_redit(self._spring_client, redis_key)
            last_crawl_ts = int(value) if value else 0

            curr_ts = int(time.time())
            if curr_ts - last_crawl_ts < hub_page_crawl_interval:
                log_content = "cur_ts - last_crawl_ts=%d,hub_page_crawl_interval=%d, " \
                              "dont need update" % (curr_ts - last_crawl_ts, hub_page_crawl_interval)
                logging.info(log_content)
                continue

            goal_pages_info = self.get_info_from_hub_page(web_seed)
            # print(goal_pages_info)
            if goal_pages_info is None: # 该url为垃圾网页
                return
            self.process_goal_pages(goal_pages_info)
            # 保存该次爬取时间点到redis
            put_data2redit(self._spring_client, redis_key, str(curr_ts))

    # 从hub页面中爬取goal页面的相关信息（url,ans_num）
    def get_info_from_hub_page(self, web_seed):
        '''
        :param web_seed: hub站点种子(url,source_name)
        :return: [goal page list, source_name, goal page answers num list]
        '''
        url, source_name = web_seed
        page_content = self.get_page(url)  # 返回抓取到的网页内容
        if page_content is None: return None

        hub_page_tree = build_doc(page_content)
        hub_page_tree = make_links_absolute(hub_page_tree, url)

        goal_pages = self.get_goal_pages_by_tree(hub_page_tree, source_name)
        answers_num = self.get_hub_page_ans_num_by_tree(hub_page_tree, source_name)
        # print(len(goal_pages),answers_num);exit();
        try:
            if not answers_num is None:
                if self.DEBUG: print(len(answers_num),len(goal_pages))
                assert len(goal_pages) == len(answers_num)
        except:
            log_content = "WebInfoUpdate get_info_from_hub_page() error, %s " % (url)
            log_content += "len(sub_goal_pages)!=len(every_question_ans_num)"
            logging.error(log_content)

        if len(goal_pages) == 0:
            log_content = "get goal pages num = 0 from hub page: %s ." % (url)
            logging.warning(log_content)

        info = {}
        info["goal_page_urls"] = goal_pages
        info["source_name"] = source_name
        info["ans_num"] = answers_num
        if self.DEBUG: print(answers_num)
        return info

    def process_goal_pages(self, goal_pages_info):
        # 用户最近一次爬取的item
        goal_page_urls = goal_pages_info.get("goal_page_urls")
        answers_num = goal_pages_info.get("ans_num")
        source_name = goal_pages_info.get("source_name")

        # 处理hub页中的每一个goal页面
        for i in range(len(goal_page_urls)):
            time.sleep(0.5) # 防止页面429
            url = goal_page_urls[i]
            # 如果hub页无法抓取ans_num数量
            if answers_num is None or len(answers_num)==0:
                qa_info = self.crawl_goal_page(url,source_name)
                if not qa_info is None:
                    self.store_data_to_kafka(qa_info)
                continue

            mp_uid = get_md5(url)
            redis_key = 'goal_page_answers_num_%s' % (mp_uid)
            redis_key = self.BUZZQA_CRAWL_INFO.format(redis_key)
            old_ans_num = read_redit(self._spring_client, redis_key)
            old_ans_num = int(old_ans_num) if old_ans_num else None

            ans_num = answers_num[i]
            if old_ans_num is None or old_ans_num != ans_num:
                qa_info = self.crawl_goal_page(url, source_name)
                if not qa_info is None:
                    self.store_data_to_kafka(qa_info)
                logging.info("Put new data to kafka. crawl goal page %s ." % (url))
            put_data2redit(self._spring_client, redis_key, str(ans_num))

    def crawl_goal_page(self, url, source_name):
        goal_page = GoalPageCrawler(self.conf, url, source_name)
        goal_page.process()
        if goal_page.qa_info is None:
            logging.info("goal_page.qa_info is None, goal page update failed.")
            metrics.emit_counter('abandon_goal_pages', 1)
            return None
        qa_info = goal_page.qa_info
        if len(qa_info.get("q")) <= self.min_q_len: # 过滤遗漏短问题 问题长度为1
            logging.info("in crawl_goal_page. miss out: need filter q = ''. url=%s" % (url))
            return None
        qa_info["crawled date"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return qa_info

    def store_data_to_kafka(self, qa_info):
        message = {}
        q_url = qa_info.get("url")
        q_key = get_md5(q_url) if q_url else None
        source = qa_info.get("source")
        message["q_key"] = q_key
        message["ans_num"] = qa_info.get("ans_num")
        message["q"] = qa_info.get("q")
        if qa_info.get("q") and len( qa_info.get("q") ) <= self.min_q_len:
            logging.info("in store_data_to_kafka miss out: need filter q = ''. url=%s" % (q_url))
            return # 过滤遗漏短问题 问题长度为1
        message["q_star"] = qa_info.get("q_star")
        message["url"] = q_url
        message["source"] = source
        message["crawled date"] = qa_info.get("crawled date")
        message["blames"] = None
        message["praises"] = None
        message["ans"] = None
        message["a_key"] = None
        message["ans_time"] = None
        message["q_describe"] = qa_info.get("q_describe")
        answers_dict = qa_info.get("Answers")

        redis_key = 'kafka_sended_q_flag_%s' % (q_key)
        redis_key = self.BUZZQA_CRAWL_INFO.format(redis_key)
        q_sended = read_redit(self._spring_client, redis_key)

        if q_sended is None:
            language = self.web_conf.get(source).get("language")
            metrics_key = language + "_q_count"
            metrics.emit_counter(metrics_key, 1)
            put_data2redit(self._spring_client, redis_key, str("sended"))

        # 存储只包含题目站点或无回答站点到kafka
        if answers_dict is None or len(answers_dict) == 0:
            if not q_sended is None: return  # 曾经存储过该题目到kafka
            try:
                value = [ (q_key,json.dumps(message).encode("utf-8")) ]
                if self.TO_KAFKA:
                    self.procducer.write_msgs( value )
                    # print("ok!")

                language = self.web_conf.get(source).get("language")
                metrics_key = language + "_qa_count"
                metrics.emit_counter(metrics_key, 1)

                metrics_key = source + "_received_qa_pair"
                metrics.emit_counter(metrics_key, 1)

                if self.DEBUG:
                    self.test_json.append(message)
                    if self.debug_log_dict.get(metrics_key) is None:
                        self.debug_log_dict[metrics_key] = 0
                    self.debug_log_dict[metrics_key] += 1

            except Exception as e:
                log_content = "kafka write_msgs error. exception is: %s" % (e)
                logging.error(log_content)
            return

        # 存储问题及答案对到kafka
        for ans_key in answers_dict.keys():
            blames = answers_dict.get(ans_key).get("blames")
            praises = answers_dict.get(ans_key).get("praises")
            ans = answers_dict.get(ans_key).get("ans")
            ans_time = answers_dict.get(ans_key).get("ans_time")
            a_key = get_md5(ans)
            redis_key = q_key + a_key
            redis_key = self.BUZZQA_CRAWL_INFO.format(redis_key)
            qa_sended = read_redit(self._spring_client, key=redis_key)
            if not qa_sended is None: continue

            message["blames"] = blames
            message["praises"] = praises
            message["ans_time"] = ans_time
            message["ans"] = ans
            message["a_key"] = a_key

            try:
                language = self.web_conf.get(source).get("language")
                metrics_key = language + "_qa_count"
                metrics.emit_counter(metrics_key, 1)

                value = [ (q_key, json.dumps(message).encode("utf-8")) ]
                if self.TO_KAFKA:
                    self.procducer.write_msgs(value)
                metrics_key = source + "_received_qa_pair"
                metrics.emit_counter(metrics_key, 1)

                if self.DEBUG:
                    self.test_json.append(message)
                    if self.debug_log_dict.get(metrics_key) is None:
                        self.debug_log_dict[metrics_key] = 0
                    self.debug_log_dict[metrics_key] += 1
            except Exception as e:
                log_content = "kafka write_msgs error. exception is: %s" % (e)
                logging.error(log_content)
            put_data2redit(self._spring_client, key=redis_key, value=str("sended"))

    def get_goal_pages_by_tree(self, tree, source_name):
        try:
            main_web_conf = self.web_conf.get(source_name)
            hub_page_conf = main_web_conf.get("hub_page_conf")
            goal_pages_xpath = hub_page_conf.get("get_goal_urls_xpath")
            goal_pages = tree.xpath(goal_pages_xpath)  # type:list
        except Exception as e:
            log_content = "WebInfoUpdate get_goal_pages_by_tree() error, tree or website_name error e = %s"
            logging.error(log_content, e)
            goal_pages = []
        return goal_pages

    # 获取hub界面上的每个question的answer个数
    def get_hub_page_ans_num_by_tree(self, tree, source_name):
        try:
            main_web_conf = self.web_conf.get(source_name)
            hub_page_conf = main_web_conf.get("hub_page_conf")
            ans_num_xpath = hub_page_conf.get('get_ans_num_xpath')
            ans_num_re = hub_page_conf.get('get_ans_num_re')
            if ans_num_xpath is None: return None
            result = tree.xpath(ans_num_xpath)  # type:list
            result = map(lambda x: x.text_content().strip(), result)
            result = map(lambda x: x.encode('utf8'), result)
            result = map(lambda x: int(re.findall(ans_num_re, x)[0]), result)  # type:list
        except Exception as e:
            log_content = "hub page get ans num error, tree or website_name or format error,e=%s"
            logging.error(log_content, e)
            result = []
        return result

    def get_page(self, url):
        proxy = random.choice(self.proxies)
        try:
            html = crawl(url, ua_used=self.ua_used, proxy=proxy, method='get')
        except Exception as e:
            log_text = "invalid url, crawl %s failed" % (url)
            logging.error(log_text)
            html = None
        return html

def post_argparse(parser):
    pass

if __name__ == '__main__':
    from crawl_data.domain.utils.script import get_fullpath, script_init
    from pyutil.springdb import SpringDBClient
    import django

    django.setup()
    SpringDBClient.set_zone('online')

    sc = script_init(
        'crawl_buzzup_qa_v2',
        ['wangyulong'],
        get_fullpath(__file__, '../../../../../conf/i18n/'),
        post_argparse=post_argparse)

    update = QACrawler(sc.conf)
    update.process()





