# coding=utf8
import re, os, sys, json, logging, random, time, threading
os.environ['DJANGO_SETTINGS_MODULE'] = 'crawl_data.djangosite.settings'
import crawl_data.setup_crawl_env

from lxml import etree
from collections import Counter
from lxml.html import make_links_absolute
from lxml.html.clean import Cleaner
import json
from urllib import unquote

from ss_extractor.src.article.article_extract.modules.extract_content.content_processor import get_clean_content
from ss_extractor.src.article.image_process.image_extract import ImageExtractor  # extract
from ss_extractor.src.article.extract_util.htmls import build_doc

from utils import crawl
from config import Config

reload(sys)
sys.setdefaultencoding('utf-8')

class GoalPageCrawler(object):
    DEFAULT_UA_USED = 1

    # RT 为富文本（rich text）
    def __init__(self, conf, url, source_name):
        """
        :param conf: basic conf
        :param url: 问答目标页地址 # type: string
        :param source_name: 主站点名称 case: "Yahoo_en"
        """
        self.min_q_len = 2 # 只抓取问题长度大于2的目标页
        self.web_name = source_name
        self.goal_url = url
        self.ua_used = int(conf.ua_used) if conf.ua_used else self.DEFAULT_UA_USED  # 用户代理
        self.proxies = conf.get_values('squid_proxies')
        self.image_extractor = ImageExtractor(conf)
        self.web_conf = Config().web_info_config.get(source_name)  # 定义xpath配置
        if self.web_conf is None:
            log_content = "web_info_config key %s miss hit. url = %s" % (source_name, self.goal_url)
            logging.warning(log_content)
        self.init_qa_info()

    def init_qa_info(self):
        self.qa_info = {}
        self.qa_info["url"] = self.goal_url
        self.qa_info["q"] = ""
        self.qa_info["q_star"] = None  # 问题的星级
        self.qa_info["Answers"] = {}  # 各answers的实体文本 type:list
        self.qa_info["ans_num"] = None  # 该问题回答数量 type:list
        self.qa_info["source"] = self.web_name

    def process(self):
        about_page = self.get_page(self.goal_url)  # 返回抓取到的网页内容
        tree = build_doc(about_page) if about_page else None
        if tree is None:
            log_content = "get html content error, get this page failed. url = %s" % (self.goal_url)
            logging.warning(log_content)
            return

        # 问题
        question = self.get_detail_info(tree, key="get_q", int_flag=False)
        q_describe = self.get_detail_info(tree, key="q_describe", int_flag=False)
        q_star = self.get_detail_info(tree, key="get_q_star", int_flag=True)
        self.update_q(question, q_describe, q_star)
        if self.qa_info is None: return

        # 回答
        ans = self.get_ans_RT_info(tree, key="get_ans")

        if ans is None:
            self.qa_info = None
            error_content = "please remove this qa. url=%s"
            logging.info(error_content, self.goal_url)
            return

        if len(ans) == 0:  # 面向只抓取问题型站点
            self.qa_info["ans_num"] = 0
            self.qa_info["Answers"] = {}
            return

        ans_blames = self.get_detail_info(tree, "get_ans_blames", int_flag=True)
        ans_praises = self.get_detail_info(tree, "get_ans_praises", int_flag=True)
        ans_num = self.get_detail_info(tree, "get_ans_num", int_flag=True)
        ans_time = self.get_detail_info(tree, "get_ans_time", int_flag=False)
        self.update_a(ans, ans_num, ans_blames, ans_praises, ans_time)
        # print(self.qa_info)

    def update_q(self, question, q_describe, q_star):
        if (question is None) or len(question) == 0 or len(question[0]) <= self.min_q_len:
            self.qa_info = None
            # print("question = ", question)
            error_content = "please check get_q_xpath. "
            error_content += "question is None, please remove this qa. url=%s"
            logging.warning(error_content, self.goal_url)
            return None
        if self.q_content_filter(question[0]) is None:
            self.qa_info = None
            error_content = "filter this q. url = %s"
            logging.warning(error_content, self.goal_url)
            return None

        # 部分不带？的问题添加？
        self.qa_info["q"] = question[0].strip()
        bool1 = "?" not in self.qa_info["q"][-3:]
        bool2 = "？" not in self.qa_info["q"][-3:]
        if bool1 and bool2:
            self.qa_info["q"] += "?"
        self.qa_info["q_describe"] = q_describe[0] if q_describe else None
        self.qa_info["q_star"] = q_star[0] if q_star else None

    def update_a(self, ans, ans_num, ans_blames, ans_praises, ans_time):
        goal_page_conf = self.web_conf.get("goal_page_conf")
        # 废弃该问题, 页面不符合标准xpath规范或富文本提取不到
        self.qa_info["ans_num"] = ans_num[0] if ans_num else None

        if (not ans_praises is None) and len(ans) != len(ans_praises):
            self.qa_info = None
            error_content = "len(ans_praises)!= len(ans),url=%s"
            logging.error(error_content, self.goal_url)
            return

        if (not ans_blames is None) and len(ans) != len(ans_blames):
            self.qa_info = None
            error_content = "len(ans_blames)!= len(ans),url=%s"
            logging.error(error_content, self.goal_url)
            return

        top_k = goal_page_conf.get("topk_ans")
        if top_k is None:
            import_id = range(len(ans))
        else:
            import_id = [[k, len(ans[k])] for k in range(len(ans))]
            import_id = sorted(import_id, key=lambda x: x[1], reverse=True)
            import_id = [import_id[k][0] for k in range(min(top_k,len(import_id)))]

        ans_result = {}
        for i in import_id:
            key = "ans_%.3d" % (i)
            if self.ans_content_filter(ans[i]) is None:
                continue
            ans_result[key] = {}
            ans_result[key]["ans"] = ans[i]

            # 抽取点赞
            if not ans_praises is None:
                try:
                    ans_result[key]["praises"] = ans_praises[i]
                except:
                    log_content = "GoalPageCrawler len(ans)=%d != len(ans_praises)=%d, " \
                                  "url=%s"%(len(ans),len(ans_praises),self.goal_url)
                    logging.warning(log_content)
            else:
                ans_result[key]["praises"] = None

            # 抽取点踩
            if not ans_blames is None:
                try:
                    ans_result[key]["blames"] = ans_blames[i]
                except:
                    log_content = "GoalPageCrawler len(ans)=%d != len(ans_blames)=%d, " \
                                  "url=%s"%(len(ans),len(ans_blames),self.goal_url)
                    logging.warning(log_content)
            else:
                ans_result[key]["blames"] = None

            # 抽取回答时间
            if not ans_time is None:
                try:
                    ans_result[key]["ans_time"] = ans_time[i]
                except:
                    log_content = "GoalPageCrawler len(ans)=%d != len(ans_time)=%d, " \
                                  "url=%s"%(len(ans),len(ans_time),self.goal_url)
                    logging.warning(log_content)
            else:
                ans_result[key]["ans_time"] = None

        self.qa_info["Answers"] = ans_result

    # 清除html页面中问题回答中没用的子标签
    def clear_content(self, node, node_name="script"):
        need_rm_nodes = node.findall(node_name)
        for need_rm_node in need_rm_nodes:
            node.remove(need_rm_node)
        return node

    def get_detail_info(self, tree, key, int_flag=False):
        goal_page_conf = self.web_conf.get("goal_page_conf")
        # 配置文件无法获取关键值
        if goal_page_conf is None:
            log_content = "goal_page_conf not exist in web_info_config, url = %s" % (key, self.goal_url)
            logging.info(log_content)
            return None

        main_xpath = goal_page_conf.get(key + "_xpath")
        # 配置文件无法获取关键值
        if main_xpath is None:
            log_content = "key %s_xpath not exist in web_info_config, url = %s" % (key, self.goal_url)
            logging.info(log_content)
            return None

        main_re = goal_page_conf.get(key + "_re")
        # 配置文件无法获取关键值
        if main_re is None:
            log_content = "key %s_re not exist in web_info_config, url = %s" % (key, self.goal_url)
            logging.info(log_content)
            return None

        result = tree.xpath(main_xpath)
        # html文本中无法获取xpath的节点
        if result is None:
            log_content = "tree get None from xpath(%s), url = %s" % (main_xpath, self.goal_url)
            logging.warning(log_content)
            return None

        try:
            result = map(self.clear_content, result)  # 去掉script nodes
            result = map(lambda x: x.text_content().strip(), result)
            result = map(lambda x: x.encode('utf8'), result)
            result = map(lambda x: re.findall(main_re, x)[0], result)  # type:list
            if int_flag:
                result = map(lambda x: int(x), result)
        except Exception as e:
            log_content = "qa_info get %s error, url=%s, exception=%s"
            logging.error(log_content, key, self.goal_url, e)
            return None
        return result

    # 过滤answers
    def ans_content_filter(self, content):
        goal_page_conf = self.web_conf.get("goal_page_conf")
        max_len = goal_page_conf.get("ans_max_len")
        min_len = goal_page_conf.get("ans_min_len")
        filter_re = goal_page_conf.get("ans_filter_re")
        has_key_word = re.findall(filter_re, content) if filter_re else []
        bool1 = len(content) >= min_len if min_len else True
        bool2 = len(content) <= max_len if max_len else True
        has_key_word = False if len(has_key_word)==0 else True
        if bool1 and bool2 and not has_key_word:
            return content
        return None

    def q_content_filter(self, content):
        goal_page_conf = self.web_conf.get("goal_page_conf")
        re_result = goal_page_conf.get("q_not_filter_re")
        has_key_word = re.findall(re_result, content) if re_result else [ "key_word" ]
        has_key_word = False if len(has_key_word) == 0 else True
        if has_key_word: return content
        return None

    # 抓取目标页的answers的富文本
    def get_ans_RT_info(self, tree, key):
        goal_page_conf = self.web_conf.get("goal_page_conf")
        # 配置文件无法获取关键值
        if goal_page_conf is None:
            log_content = "goal_page_conf not exist, url = %s" % (key, self.goal_url)
            logging.warning(log_content)
            return None

        main_xpath = goal_page_conf.get(key + "_xpath")
        # 配置文件无法获取关键值
        if main_xpath is None:
            log_content = "key %s_xpath not exist, url = %s" % (key, self.goal_url)
            logging.info(log_content)
            return []

        main_re = goal_page_conf.get(key + "_re")
        # 配置文件无法获取关键值
        if main_re is None:
            log_content = "key %s_re not exist, url = %s" % (key, self.goal_url)
            logging.warning(log_content)
            return None

        result = tree.xpath(main_xpath)
        # html文本中无法获取xpath的节点
        if result is None:
            log_content = "tree get None from xpath(%s), url = %s" % (main_xpath, self.goal_url)
            logging.warning(log_content)
            return None
        try:
            if len(result) == 0: return []  # 0个回答或xpath不匹配
            result = map(lambda x: etree.tostring(x, method='html'), result)
            result = map(self.content2RT, result)  # 获取富文本
            result = map(lambda x: unquote(x).encode("utf8"), result)
            result = map(lambda x: x.replace("<div>", ""), result)  # 获取富文本
            result = map(lambda x: x.replace("</div>", ""), result)  # 获取富文本
        except Exception as e:
            error_content = "get ans error, please discard this goal page. url=%s, exception=%s"
            logging.warning(error_content, self.goal_url, e)
            result = None
        return result

    # 获取该html界面的富文本
    def content2RT(self, content):
        content, _ = get_clean_content(
            url=self.goal_url,
            content=content,
            title=None,
            valid_sections=set(),
            req=None,
            page_num=0,
            log_id="goal page clean_content",
            # language="en",
        )
        content = make_links_absolute(content, self.goal_url)
        content, _, __ = self.image_extractor.extract(self.goal_url, content, max_images=10)
        return content

    def get_page(self, url):
        proxy = random.choice(self.proxies)
        try:
            html = crawl(url, ua_used=self.ua_used, proxy=proxy, method='get')
            html = html.decode("utf-8", 'ignore')
        except Exception as e:
            logging.warning("crawl %s failed,e=%s", url, e)
            html = None
        return html

def post_argparse(parser):
    pass


if __name__ == '__main__':
    from crawl_data.domain.utils.script import get_fullpath, script_init
    from pyutil.springdb import SpringDBClient
    import django

    sc = script_init(
        'crawl_buzzup_qa_v2',
        ['wangyulong'],
        get_fullpath(__file__, '../../../../../conf/i18n/'),
        post_argparse=post_argparse)
    qa_website_xpath = Config().web_info_config

    django.setup()
    SpringDBClient.set_zone('online')

    logging.basicConfig(filename=None, level=logging.WARNING)

    seed_webs = [
        # # ### blurtit 站点case
        # ("https://beauty.blurtit.com/4549234/what-are-the-latest-trends-in-modest-activewear-for-women-","Blurtit"), #含图
        # ("https://www.blurtit.com/4549517/why-digital-watercolor-art-is-gaining-popularity","Blurtit"),
        # ("https://www.blurtit.com/4549507/why-people-are-harping-so-much-about-borrowed-religion","Blurtit"),
        # ("https://arts-literature.blurtit.com/2537525/plot-of-how-my-brother-leon-brought-home-a-wife","Blurtit"),
        # ("https://technology.blurtit.com/205769/how-do-i-type-a-letter-on-my-computer-and-then-print-it","Blurtit"),
        #
        # # ### Fluther 站点case
        # ("https://www.fluther.com/206638/is-it-legal-in-the-olympics-to-inject-ones-self-with/","Fluther"),
        # ("https://www.fluther.com/206662/do-you-believe-the-north-korean-government-is-really-going-to/","Fluther"),
        # ("https://www.fluther.com/206717/did-i-get-rid-of-the-computer-virus-on-my-samsung/","Fluther"),
        # ("https://www.fluther.com/206785/what-are-some-important-weather-formulas-mathematical-with-units/","Fluther"),
        # ("https://www.fluther.com/206837/how-could-you-eat-badly-as-a-vetgetarian-according-to-the/","Fluther"), # 不带？号
        # ("https://www.fluther.com/206802/can-the-body-heal-itself-3-in-the-series-back-painneck/","Fluther"), # 有@
        #
        # # ### StackExchange 站点case
        # ("https://math.stackexchange.com/questions/2689332/monic-polynomials-whose-roots-are-their-remaining-coefficients","StackExchange"), #有公式
        # ("https://electronics.stackexchange.com/questions/361348/what-is-the-name-for-this-encapsulated-smps","StackExchange"), #有图
        # ("https://academia.stackexchange.com/questions/105405/what-to-do-with-small-research-results-in-theoretical-computer-science","StackExchange"), #有图
        # #
        # # ### Answers
        # # ### ("http://www.answers.com/Q/Does_Zeus_live_on_mount_Olympus","Answers"),
        # # # 有问题站点
        # ("https://www.fluther.com//206465/is-it-reasonable-to-expect-a-police-officer-armed-with-a/","Fluther"),
        # ("https://legal.blurtit.com/321621/-were-james-hoyt-and-kristen-mckay-really-murdered-and-what-were-the-details","Blurtit"),
        # ("https://worldbuilding.stackexchange.com//questions/106941/would-it-be-possible-to-genetically-engineer-a-human-immune-to-weapons-if-so-u","StackExchange"),
        # #
        # # ## Elaele
        # ("https://elaele.com.br/encontros/93910-onde-voce-me-levaria-pra-sair.html","Elaele"),
        # ("https://elaele.com.br/encontros/48151-meninas-socorro-to-menstruada-nao-quero-cancelar-encontro.html", "Elaele"),
        # #
        # # ### Perguntedireito
        # ("https://www.perguntedireito.com.br/12523/direito-civil","Perguntedireito"),
        # ("https://www.perguntedireito.com.br/12503/quem-teve-50-faltas-em-um-ano-tem-direito-a-ferias","Perguntedireito"),
        #
        # ## Okwave
        # ("https://okwave.jp/qa/q9478599.html","Okwave"),
        # ("https://okwave.jp/qa/q9478604.html","Okwave"),
        #
        # ## Quora_en
        # ("https://www.quora.com/How-did-the-US-battle-communism-in-Asia-in-the-1950s","Quora_en"),
        #
        # ## Yahoo_en
        # ("https://answers.yahoo.com/question/index?qid=20180312154406AAKJZoK","Yahoo_en"),
        # ("https://answers.yahoo.com/question/index?qid=20180315205809AA0N2vy","Yahoo_en"),
        #
        # ## Yahoo_br
        # ("https://br.answers.yahoo.com/question/index?qid=20180313012141AA9CLC6","Yahoo_br"),
        #
        # # ## Gloove
        # ("http://gloove.com.br/261740/meninas-voc%C3%AAs-preferem-te-amo-mentiroso-uma-ere%C3%A7%C3%A3o-sincera","Gloove"),
        # ("http://gloove.com.br/267070/good-night", "Gloove"),  # 没带问号 不抓
        # # ### Yahoo_jp
        # ("https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14187592859","Yahoo_jp"),
        # ("https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11187652841","Yahoo_jp"),
        # ("https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10187592600","Yahoo_jp"),
        #
        # ## Qanda
        # ("https://qanda.rakuten.ne.jp/qa9479792.html","Qanda"),
        #
        # ## Okwave
        # ("https://okwave.jp/qa/q9479791.html","Okwave"),
        #
        # # reddit
        # ("https://www.reddit.com/r/AskReddit/comments/85nck7/serious_whats_the_creepiestmost_interesting/","Reddit"),
        #
        # ##
        # ("https://answers.yahoo.com/question/index?qid=20180319175649AAVldfb","Yahoo_en"),
        # ("https://answers.yahoo.com/question/index?qid=20180319133244AAfPFdN", "Yahoo_en"),
        #
        # ("https://money.stackexchange.com/questions/86920/can-a-zelle-bank-transfer-be-reversed-or-denied-after-credit-has-been-added","StackExchange"),
        # ("https://jp.quora.com/なぜ日本では-オーガニック商品の取り扱いが少ない","Quora_jp"),
        # ("https://www.reddit.com/r/AskReddit/comments/876iqs/911_dispatchers_of_reddit_what_are_some_of_the/","Reddit"),
        # ("https://answers.yahoo.com/question/index?qid=20180319175649AAVldfb", "Yahoo_en"),
        # ("https://www.quora.com/Why-are-regular-mass-shootings-accepted-as-the-price-for-being-able-to-have-guns-in-American-society","Quora_en"),
        ("https://www.quora.com/How-can-I-earn-money-without-an-investment-2","Quora_en"),
    ]

    for url, source_name in seed_webs:
        qap = GoalPageCrawler(sc.conf, url, source_name)
        qap.process()
        print(qap.qa_info)
