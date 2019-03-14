# 版本说明
## 2018.3.23(V3)
    抓取版V3 版本 上线

## 2018.3.25(V3.1)
    1、修改metrics 统计日增问题bug
    2、添加Qanda站点的问题描述部分
    3、添加OKwave站点的问题描述部分
    4、修改多个 hub页种子 （StackExchange，Yahoo_jp，Okwave）
    5、新增站点支持：Goo，Sooda，Quora_jp，Hatena

#部分goal页不在需求范围内：如: http://sooda.jp/are_you_adult?to=/qa/503746 不属于Sooda爬取的内容"

## 2018.3.26(V3.2)
    1、修改kafka写入策略为has_key

## 2018.3.28(V3.3)
    1、Yahoo_en，Reddit过滤回答长度短的回答(只取top5)
    2、日语qanda、okwave有部分问题与问题描述一模一样，需要处理(无更新)"

## 2018.3.28(V3.4)
    1、修改了img 转义问题

## 2018.4.2(V3.5)
    1、修改quora_en 和quora_jp 的get_q_xpath 匹配不到并存储到kafka->{q:""}的bug
        修复办法: 修改config->web_info_config->Quora_en和Quora_jp->goal_page_conf->get_q_xpath:
        之前是: ".//div[@class='header']//span[@class='rendered_qtext']"
        改后是: ".//div[contains(@class,'question_text_edit')]//span[@class='rendered_qtext']"

    2、GoalPageCrawler和QACrawler类内添加 min_q_len 过滤条件


## V3.6待上线
    1、待修改Qanda Okwave重复问题（消重那边的任务）

# 程序部分说明
1、GoalPageCrawler类爬取目标页内容（爬取规则基于dom树xpath）
2、QACrawler类整个程序的类接口，按时循环抓取各大站点内容
3、config 各大站点种子以及各大站点xpath配置



