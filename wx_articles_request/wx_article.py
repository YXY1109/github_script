import re
import time

import requests
from scrapy import Selector


def get_article_content():
    article_url = "https://mp.weixin.qq.com/s/L9IIvYfdepRq0PgDTVKqyA"
    article_url = "https://mp.weixin.qq.com/s/G3cPTeVyOM5OcxSnIRbcfg"
    # article_url = "https://mp.weixin.qq.com/s/dWGHOGVVwsMtHHz48QhS1A"
    response = requests.get(article_url)
    print(f"返回状态：{response.status_code}")
    html = response.text
    # print(f"返回内容：{html}")
    print("*" * 50)

    time_stamp = re.findall(r"var createTimestamp = '(\d{10})'", html)
    if time_stamp:
        create_time_stamp = time_stamp[0]
        print(f"时间戳：{create_time_stamp}")
        # 时间戳转时间
        normal_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(create_time_stamp)))
        print(f"时间：{normal_time}")

    selector = Selector(text=html)
    title = selector.xpath('//*[@id="activity-name"]/text()').get().strip()
    print(f"标题：{title}")
    source = selector.xpath('//*[@id="js_name"]/text()').get().strip()
    print(f"来源：{source}")

    # 只取到文本
    # content = selector.xpath('//*[@id="js_content"]//span/text()').getall()
    # print(f"文本详情：{content}")

    # todo 有问题
    selector_list = selector.xpath('//*[@id="js_content"]//section|//*[@id="js_content"]//p').getall()
    for item in selector_list:
        # 解析item
        sel_item = Selector(text=item)
        print(sel_item)
    # print(f"详情：{content}")


if __name__ == '__main__':
    """
    通过链接地址，获取时间，标题，来源等信息
    """
    get_article_content()
