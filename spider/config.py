# coding=utf8

class Config(object):
    version = "V3.5"
    online_interval = 20 * 60


    # 英语类种子站点
    en_seeds = [
        ("https://www.quora.com/sitemap/questions", "Quora_en"),
        ("https://answers.yahoo.com/", "Yahoo_en"),

        ("https://www.blurtit.com/topics?page=1", "Blurtit"),
        ("https://www.blurtit.com/topics?page=2", "Blurtit"),
        ("https://www.blurtit.com/?tab=all&filter=popular&page=1", "Blurtit"),
        ("https://www.blurtit.com/?tab=all&filter=popular&page=2", "Blurtit"),
        ("https://www.blurtit.com/?filter=all_activity", "Blurtit"),

        ("https://www.fluther.com/?page=1", "Fluther"),  # 等价于 https://www.fluther.com/
        ("https://www.fluther.com/?page=2", "Fluther"),

        ("https://www.reddit.com/r/AskReddit/?count=1", "Reddit"),

        ("https://money.stackexchange.com/", "StackExchange"),
        ("https://parenting.stackexchange.com/", "StackExchange"),
        ("https://movies.stackexchange.com/", "StackExchange"),
        ("https://travel.stackexchange.com/", "StackExchange"),
        ("https://pets.stackexchange.com/", "StackExchange"),
        ("https://sustainability.stackexchange.com/", "StackExchange"),
        ("https://health.stackexchange.com/", "StackExchange"),
        ("https://literature.stackexchange.com/", "StackExchange"),
        ("https://crafts.stackexchange.com/", "StackExchange"),
        ("https://lifehacks.stackexchange.com/", "StackExchange"),
        ("https://interpersonal.stackexchange.com/", "StackExchange"),
        ("https://politics.stackexchange.com/", "StackExchange"),
        ("https://alcohol.stackexchange.com/", "StackExchange"),
        ("https://diy.stackexchange.com/", "StackExchange"),
        ("https://fitness.stackexchange.com/", "StackExchange"),
        ("https://worldbuilding.stackexchange.com/", "StackExchange"),

    ]

    # 葡语类种子站点
    br_seeds = [
        ("https://br.answers.yahoo.com/", "Yahoo_br"),
        ("http://gloove.com.br/questions", "Gloove"),

        ("https://elaele.com.br/encontros", "Elaele"),
        ("https://elaele.com.br/paquera", "Elaele"),

        ("https://www.perguntedireito.com.br/", "Perguntedireito"),
        ("https://www.perguntedireito.com.br/questions", "Perguntedireito"),
        ("https://www.perguntedireito.com.br/questions?start=20", "Perguntedireito"),
    ]
    # 日语类种子站点
    jp_seeds = [
        ("https://jp.quora.com/sitemap/questions", "Quora_jp"),

        ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=0", "Yahoo_jp"),
        ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=1", "Yahoo_jp"),
        ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=2", "Yahoo_jp"),

        ("https://okwave.jp/list/new_question/", "Okwave"),
        ("https://okwave.jp/list/many_pv/today/", "Okwave"),
        ("https://okwave.jp/list/many_answer/", "Okwave"),

        ("https://qanda.rakuten.ne.jp/search_pv.php3?page=1", "Qanda"),
        ("https://qanda.rakuten.ne.jp/search_pv.php3?page=2", "Qanda"),
        ("https://qanda.rakuten.ne.jp/search.php3?page=1", "Qanda"),

        ("https://oshiete.goo.ne.jp/articles/qa/2008/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2009/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2010/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2013/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2003/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2005/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2001/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2002/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2012/", "Goo"),
        ("https://oshiete.goo.ne.jp/articles/qa/2006/", "Goo"),

        ("http://sooda.jp/questions/%E6%81%8B%E6%84%9B_%E4%BA%BA%E9%96%93%E9%96%A2%E4%BF%82%E3%81%AE%E6%82%A9%E3%81%BF/recent_all-list/",
        "Sooda"),
        ("http://sooda.jp/questions/%E4%BB%95%E4%BA%8B_%E3%82%AD%E3%83%A3%E3%83%AA%E3%82%A2/recent_all-list/", "Sooda"),
        ("http://sooda.jp/questions/%E6%9A%AE%E3%82%89%E3%81%97/recent_all-list/", "Sooda"),
        ("http://sooda.jp/questions/%E7%BE%8E%E5%AE%B9_%E5%81%A5%E5%BA%B7/recent_all-list/", "Sooda"),
        ("http://sooda.jp/questions/%E8%B6%A3%E5%91%B3_%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%86%E3%82%A4%E3%83%A1%E3%83%B3%E3%83%88/recent_all-list/",
        "Sooda"),

    ]

    test_seeds = [
        # ("https://www.reddit.com/r/AskReddit/", "Reddit"),
        ("https://www.quora.com/sitemap/questions", "Quora_en"),
        # ("https://okwave.jp/list/new_question/", "Okwave"),
        # ("https://okwave.jp/list/many_pv/today/", "Okwave"),
        # ("https://okwave.jp/list/many_answer/", "Okwave"),
        # ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=0", "Yahoo_jp"),
        # ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=1", "Yahoo_jp"),
        # ("https://chiebukuro.yahoo.co.jp/list/question_list.php?flg=2", "Yahoo_jp"),
        # ("https://qanda.rakuten.ne.jp/search_pv.php3?page=1", "Qanda"),
        # ("http://q.hatena.ne.jp/list","Hatena"),
        # ("https://jp.quora.com/sitemap/questions", "Quora_jp"),

    ]

    web_seeds = en_seeds + br_seeds + jp_seeds
    # web_seeds = test_seeds

    """
    crawl_interval: # 该类站点抓取周期
    get_goal_urls_xpath: hub页中目标页链接获取xptah
    get_ans_num_xpath: hub页/目标页获取问题回答数目xpath
    get_ans_num_re: 用正则从包含回答数字的文本中抽取int(ans_num)
    get_q_xpath: 目标页中抽取题目内容的xptah
    get_ans_xpath: 目标页中抽取answers内容的xpath
    ans_max_len: answer长度阈值
    ans_min_len: answer长度阈值
    """

    web_info_config = {
        ### 英语站点配置
        "Blurtit": {
            # 适配站点类 "https://www.blurtit.com/topics?page=%d"%( int(k) )
            # 适配站点类 "https://www.blurtit.com/?tab=all&filter=popular&page=%d"%( int(k) )
            # 适配站点 "https://www.blurtit.com/?filter=all_activity"
            "language": "English",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//article/div[@class='article-main']/div[@class='feed-item-title clearfix']/a[1]/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//ul[@class='pull-left action-links']/li[@class='separate'][1]/a",
                "get_ans_num_re": r'([\d]+)[\D]+Answer',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//h1[@class='page-title editable-non-textarea']",
                "get_q_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//article/div[@class='article-main']/div[@class='user-content clearfix ']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": None,  # 登录才能看到问题回答时间
                "get_ans_time_re": r"[\s\S]*",

                # len(answers)
                "get_ans_num_xpath": ".//div[@id='answers']//h2[@class='pull-left']",
                "get_ans_num_re": r'([\d]+)[\D]+Answer',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Fluther": {
            # 适配站点类型 "https://www.fluther.com/?page=%d"%( int(k) )
            "language": "English",
            "crawl_interval": online_interval,  # 多久开始监测一次该类站点
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//ul[@class='disc-list']/li/h4/a/@href",

                # len(answers) in hub page
                "get_ans_num_xpath": ".//ul[@class='disc-list']/li/span[@class='smalltext']",
                "get_ans_num_re": r'([\d]+)[\D]+response',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "ans_filter_re": r'[\s\S]*(@)[\s\S]*',  # 过滤包含特殊字符的回答

                # question
                "get_q_xpath": ".//div[@id='question']/h1",
                "get_q_re": r"[\s\S]*",

                # q_describe
                "q_describe_xpath": ".//div[@class='question-body']//div[@id='description']",
                "q_describe_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": ".//li[@class='great-question']//span[@class='gq-score']",
                "get_q_star_re": r"[\d]+",

                # ans time
                "get_ans_time_xpath": None,
                "get_ans_time_re": r"[\s\S]*",

                # answer_num
                "get_ans_num_xpath": ".//div[@class='content']/h2/span[@id='flr-response-count']",
                "get_ans_num_re": r'[\d]+',

                # answers (list)
                "get_ans_xpath": ".//div[@id='quiplist']//div[@class='message']",
                "get_ans_re": r"[\s\S]*",

                # answers praises (list)
                "get_ans_praises_xpath": ".//span[@class='qspan great-answer']/span[@class='score']",
                "get_ans_praises_re": r'[\d]+',

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "StackExchange": {
            # 适配站点类型 "https://stackexchange.com/?page=%d"%( int(k) )
            "language": "English",
            "crawl_interval": online_interval,  # 多久开始监测一次该类站点
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[contains(@class,'question-summary')]/div[@class='summary']/h3/a/@href",

                # len(answers) in hub page
                "get_ans_num_xpath": ".//div[contains(@class,'question-summary')]//div[contains(@class,'answered')]",
                "get_ans_num_re": r'([\d]+)[\D]+answer',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[@id='content']//div[@id='question-header']/h1[@itemprop='name']/a",
                "get_q_re": r"[\s\S]*",

                # q_describe
                "q_describe_xpath": ".//div[@class='post-layout']//div[@class='post-text']",
                "q_describe_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@id='answers']/div[contains(@class,'answer')]//div[@class='post-text']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": ".//div[@id='question']//div[@class='vote']/span[@class='vote-count-post ']",
                "get_q_star_re": r'([-]?\d+)',

                # ans time
                "get_ans_time_xpath": ".//div[@class='answercell post-layout--right']//div[@class='user-action-time'][last()]/span",
                "get_ans_time_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@id='answers-header']//h2",
                "get_ans_num_re": r'([\d]+)[\D]+Answer',

                # answers praises (list)
                "get_ans_praises_xpath": ".//div[@id='answers']//div[@class='vote']/span[@class='vote-count-post ']",
                "get_ans_praises_re": r'([-]?\d+)',

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Answers": {
            # HTTP 403
            "language": "English",
            "crawl_interval": online_interval,  # 多久开始监测一次该类站点
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//article[@id='center']//h1[@class='title']/a/@href",

                # len(answers) in hub page
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "ans_filter_not_contain": None,  # answer内容不包含

                # question
                "get_q_xpath": ".//h1[@class='title']/span[@class='title_text']",
                "get_q_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='answer_wrapper ']/div[@class='answer_text']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": None,
                "get_ans_time_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Quora_en": {
            "language": "English",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='ContentWrapper']/div/div/div/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[contains(@class,'question_text_edit')]//span[@class='rendered_qtext']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='ui_qtext_expanded']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//a[@class='answer_permalink']/span",
                "get_ans_time_re": r"[\s\S]*",

                # len(answers)
                "get_ans_num_xpath": ".//div[@class='answer_count']",
                "get_ans_num_re": r'([\d]+)[\D]+Answer',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Yahoo_en": {
            "language": "English",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='Bfc']/h3/a[@class='Fz-14 Fw-b Clr-b Wow-bw title']/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@class='Bfc']/div[@class='Clr-888 Fz-12 Lh-18']",
                "get_ans_num_re": r'([\d]+)[\D]+answer',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,
                "topk_ans": 5,

                # question
                "get_q_xpath": ".//h1[@class='Fz-24 Fw-300 Mb-10']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@class='Mend-10 Fz-13 Fw-n D-ib']",
                "get_ans_num_re": r'([\d]+)[\D]+answer',

                # answers (list)
                "get_ans_xpath": ".//span[@class='ya-q-full-text']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//span[@class='Clr-88 ya-localtime']",
                "get_ans_time_re": r"[\s\S]*",

                # answers praises (list)
                "get_ans_praises_xpath": ".//div[@data-ya-type='thumbsUp']/div[@class='D-ib Mstart-23 count']",
                "get_ans_praises_re": r"[\d]+",

                # answers blames (list)
                "get_ans_blames_xpath": ".//div[@data-ya-type='thumbsDown']/div[@class='D-ib Mstart-23 count']",
                "get_ans_blames_re": r"[\d]+",

            },
        },

        "Reddit": {
            "language": "English",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//a[@class='title may-blank ']/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//a[@class='bylink comments may-blank']",
                "get_ans_num_re": r'[\d]+',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,
                "topk_ans": 5,

                # question
                "get_q_xpath": ".//a[@class='title may-blank ']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//a[@class='bylink comments may-blank']",
                "get_ans_num_re": r'[\d]+',

                # answers (list)
                "get_ans_xpath": ".//div[@class='sitetable nestedlisting']/div[contains(@class,'noncollapsed   comment')]"
                                 "/div[@class='entry unvoted']/form/div/div[@class='md']",
                "get_ans_re": r"[\s\S]*",

                # ans time
                "get_ans_time_xpath": ".//div[@class='sitetable nestedlisting']/div[contains(@class,'noncollapsed   comment')]"
                                      "/div[@class='entry unvoted']/p[@class='tagline']/time[@class='live-timestamp']",
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        ### 葡语站点配置
        "Yahoo_br": {
            "language": "Portuguese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='Bfc']/h3/a[@class='Fz-14 Fw-b Clr-b Wow-bw title']/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@class='Bfc']/div[@class='Clr-888 Fz-12 Lh-18']",
                "get_ans_num_re": r'([\d]+)[\D]+resposta',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//h1[@class='Fz-24 Fw-300 Mb-10']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@class='Mend-10 Fz-13 Fw-n D-ib']",
                "get_ans_num_re": r'([\d]+)[\D]+resposta',

                # answers (list)
                "get_ans_xpath": ".//span[@class='ya-q-full-text']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//span[@class='Clr-88 ya-localtime']",
                "get_ans_time_re": r"[\s\S]*",

                # answers praises (list)
                "get_ans_praises_xpath": ".//div[@data-ya-type='thumbsUp']/div[@class='D-ib Mstart-23 count']",
                "get_ans_praises_re": r"[\d]+",

                # answers blames (list)
                "get_ans_blames_xpath": ".//div[@data-ya-type='thumbsDown']/div[@class='D-ib Mstart-23 count']",
                "get_ans_blames_re": r"[\d]+",

            },
        },

        "Elaele": {
            "language": "Portuguese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='js_lista']//a[@class='titulo']/@href",
                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[@class='container']/a[@class='preto']/h1",
                "get_q_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='row resposta-item']//div[@class='descricao']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//div[@class='row resposta-item']//span[@class='timeago']",
                "get_ans_time_re": r"[\s\S]*",

                # len(answers)
                "get_ans_num_xpath": ".//div[@class='hidden-xs hidden-sm col-md-3 cinza']",
                "get_ans_num_re": r'([\d]+)[\D]+resposta',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Perguntedireito": {
            "language": "Portuguese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='qa-q-item-title']/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@class='qa-q-item-stats']//span[@class='qa-a-count-data']",
                "get_ans_num_re": r'[\d]+',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[@class='qa-main-heading']//span[@itemprop='name']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": ".//div[@class='qa-part-q-view']//div[@class='qa-q-view-content']/div[@itemprop='text']",
                "q_describe_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='qa-a-item-content']/div[@itemprop='text']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//span[@class='qa-a-item-when-data']/time",
                "get_ans_time_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@class='qa-part-a-list']/h2/span[@itemprop='answerCount']",
                "get_ans_num_re": r'[\d]+',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Gloove": {
            "language": "Portuguese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='qa-q-item-title']/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//span[@class='qa-a-count-data']",
                "get_ans_num_re": r"[\d]+",
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "q_not_filter_re": r'[\s\S]*(\?|？)[\s]*$',  # 含有特殊字符的题目不过滤

                # question
                "get_q_xpath": ".//span[@class='entry-title']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@class='qa-part-a-list']/h2",
                "get_ans_num_re": r'([\d]+)[\D]+Resposta',

                # answers (list)
                "get_ans_xpath": ".//div[@class='qa-a-item-content']/div[@class='entry-content']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                "get_ans_time_xpath": ".//span[@class='qa-a-item-when-data']//span[@class='value-title']",
                "get_ans_time_re": r"[\s\S]*",

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        ### 日语站点配置
        "Yahoo_jp": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//ul[@id='qa_lst']/li/dl/dt/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//ul[@id='qa_lst']/li/dl/dd",
                "get_ans_num_re": r'回答数[\D]*([\d]+)',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[contains(@class,'mdPstd')]/div[@class='ttl']/h1",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[contains(@class,'ptsQes')]/div[@class='attInf']/dl",
                "get_ans_num_re": r'回答数[\D]*([\d]+)',

                # answers (list)
                "get_ans_xpath": ".//div[contains(@class,'othrAns')]//div[@class='ptsQes']/p[contains(@class,'queTxt')]",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                "get_ans_time_xpath": ".//div[contains(@class,'othrAns')]//div[@class='usrInfo']//p[@class='upDt']",
                "get_ans_time_re": r"[\s\S]*",

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": r"[\d]+",

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": r"[\d]+",

            },
        },

        "Okwave": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//p[@class='qat']/a/@href",

                "get_ans_num_xpath": ".//div[contains(@class,'ico_cate_list')]",
                "get_ans_num_re": r'回答数[\D]*([\d]+)',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[@class='okw_inner']//h1[@itemprop='name']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": ".//div[@class='q_desc_area']/div[@class='q_desc']",
                "q_describe_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='other_area']//div[@class='a_textarea']",
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": ".//div[@class='other_area']//ul[@class='hed_area']/li[1]",
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # len(answers)
                "get_ans_num_xpath": ".//div[@class='okw_btn_area']/ul[@class='smry']/li/span",
                "get_ans_num_re": r'[\d]+',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Qanda": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//p[@class='qat']/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@class='ico_cate_list on_gry clearfix']",
                "get_ans_num_re": r'回答数[\D]*([\d]+)',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//p[@id='question_title']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": ".//p[@class='datail_tex qa_tex']/span[@id='question']",
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//p[@class='font_siz_18 fo_wei_b']/span",
                "get_ans_num_re": r'[\d]+',

                # answers (list)
                "get_ans_xpath": ".//div[@class='ok_lq_answer-inner']//span[@class='answer']",
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": ".//div[@class='ok_lq_answer-inner']/p[last()]",
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Goo": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//h2[@class='level']/a[@data-osccid='qa']/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@class='r_apply']",
                "get_ans_num_re": r"[\d]+",
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "ans_filter_re": None,  # 过滤包含特殊字符的回答
                "q_not_filter_re": None,  # 含有特殊字符的题目不过滤

                # question
                "get_q_xpath": ".//div[@class='q_article_info clearfix']/h1",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,

                # answers (list)
                "get_ans_xpath": None,
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": None,
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Sooda": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@id='qa_list_top']/dl[@class='list']/dt/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": ".//div[@id='qa_list_top']/dl[@class='list']/dt/a",
                "get_ans_num_re": r'[\s\S]*\(([\d]+)\)[\s]*$',
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "ans_filter_re": None,  # 过滤包含特殊字符的回答
                "q_not_filter_re": None,  # 含有特殊字符的题目不过滤

                # question
                "get_q_xpath": ".//p[@id='question_body']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": None,
                "get_ans_num_re": r"[\d]+",

                # answers (list)
                "get_ans_xpath": ".//div[@class='answer_detail']/p[@class='sentence']",
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": None,
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Hatena": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//a[@class='question-content-container']/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": None,
                "get_ans_num_re": r"[\d]+",
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                "ans_filter_re": None,  # 过滤包含特殊字符的回答
                "q_not_filter_re": None,  # 含有特殊字符的题目不过滤

                # question
                "get_q_xpath": ".//span[@class='question-content-inner']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": ".//div[@class='section answer']/div[@class='header']",
                "get_ans_num_re": r"[\d]+",

                # answers (list)
                "get_ans_xpath": ".//div[contains(@class,'answer-formatted-body')]",
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": ".//h3[contains(@class,'answer-title')]/span[@class='timestamp']/a",
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

        "Quora_jp": {
            "language": "Japanese",
            "crawl_interval": online_interval,
            "hub_page_conf": {
                "get_goal_urls_xpath": ".//div[@class='ContentWrapper']/div/div/div/a/@href",

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": None,
                "get_ans_num_re": None,
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,

                # question
                "get_q_xpath": ".//div[contains(@class,'question_text_edit')]//span[@class='rendered_qtext']",
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # answers (list)
                "get_ans_xpath": ".//div[@class='ui_qtext_expanded']",
                "get_ans_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # ans time
                "get_ans_time_xpath": ".//a[@class='answer_permalink']/span",
                "get_ans_time_re": r"[\s\S]*",

                # len(answers)
                "get_ans_num_xpath": ".//div[@class='answer_count']",
                "get_ans_num_re": r'([\d]+)[\D]+回答',

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },

    }

    template = {
        "new_None": {
            "language": "English",
            "crawl_interval": 1 * 3,
            "hub_page_conf": {
                "get_goal_urls_xpath": None,

                # 获取hub页对应问题回答数量 没有写None
                "get_ans_num_xpath": None,
                "get_ans_num_re": r"[\d]+",
            },
            "goal_page_conf": {
                "ans_max_len": 1e10,
                "ans_min_len": -1,
                "topk_ans": 5,

                "ans_filter_re": None,  # 过滤包含特殊字符的回答
                "q_not_filter_re": None,  # 含有特殊字符的题目不过滤

                # question
                "get_q_xpath": None,
                "get_q_re": r"[\s\S]*",

                "q_describe_xpath": None,
                "q_describe_re": r"[\s\S]*",

                # ans_num
                "get_ans_num_xpath": None,
                "get_ans_num_re": r"[\d]+",

                # answers (list)
                "get_ans_xpath": None,
                "get_ans_re": r"[\s\S]*",

                "get_ans_time_xpath": None,
                "get_ans_time_re": r"[\s\S]*",

                # question star
                "get_q_star_xpath": None,
                "get_q_star_re": None,

                # answers praises (list)
                "get_ans_praises_xpath": None,
                "get_ans_praises_re": None,

                # answers blames (list)
                "get_ans_blames_xpath": None,
                "get_ans_blames_re": None,

            },
        },
    }
