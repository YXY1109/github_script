#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import time
import random
import datetime

import yaml

"""
获取参数：https://www.cnblogs.com/hlikex/p/17026496.html
获取：cookie：变化
获取：token：变化
获取：user_agent。可以获取
获取：代理。可以获取
"""

with open("config.yaml", "r", encoding='utf-8') as file:
    file_data = file.read()
config = yaml.safe_load(file_data)

headers = {
    "Cookie": config['cookie'],
    "User-Agent": config['user_agent']
}

# 请求参数
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
begin = 0
params = {
    "action": "list_ex",
    "begin": begin,
    "count": 5,
    "fakeid": config['fakeid'],
    "type": "9",
    "token": config['token'],
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "need_author_name": 1
}

# 在不知道公众号有多少文章的情况下，使用while语句
# 也方便重新运行时设置页数
file_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
csv_name = f"csv/article_{file_time}.csv"
with open(csv_name, "w", encoding='utf-8') as file:
    file.write("文章标识符aid,标题title,链接url(永久),发布时间time\n")

spider_index = 1
while True:
    # 随机暂停几秒，避免过快的请求导致过快的被查到
    time.sleep(random.randint(2, 6))

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"执行时间：{now_time}")

    resp = requests.get(url, headers=headers, params=params, verify=False)
    msg_json = resp.json()
    print(f"公众号结果:{msg_json}")
    # 公众号结果:{'base_resp': {'err_msg': 'freq control', 'ret': 200013}}

    if msg_json['base_resp']['ret'] == 200003:
        print("cookie 过期, stop at {}".format(str(begin)))
        break

    # 微信流量控制, 退出
    if msg_json['base_resp']['ret'] == 200013:
        print("微信流量控制, stop at {}".format(str(begin)))
        time.sleep(3600)
        continue

    # 如果返回的内容中为空则结束
    if len(msg_json['app_msg_list']) == 0:
        print("所有文章为空")
        break

    if "app_msg_list" in msg_json:
        for item in msg_json["app_msg_list"]:
            info = '"{}","{}","{}","{}"'.format(str(item["aid"]), item['title'], item['link'],
                                                datetime.datetime.fromtimestamp(item['create_time']).strftime(
                                                    '%Y-%m-%d %H:%M:%S'))
            with open(csv_name, "a", encoding='utf-8') as f:
                f.write(info + '\n')
        print(f"第{spider_index}次爬取成功\n")

    # 间隔1分钟
    time.sleep(2 * 60)
    spider_index = spider_index + 1
    print("\n\n---------------------------------------------------------------------------------\n")
