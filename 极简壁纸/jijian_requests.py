import json
import time

import execjs
import requests
from fake_useragent import UserAgent

headers = {
    'referer': 'https://bz.zzzmh.cn/',  # 这个是必须
    'user-agent': UserAgent().random
}

json_data = {
    'size': 24,
    'current': 2,
    'sort': 0,
    'category': 0,
    'resolution': 0,
    'color': 0,
    'categoryId': 0,
    'ratio': 0,
}

response = requests.post('https://api.zzzmh.cn/bz/v3/getData', headers=headers, json=json_data).json()
result = response['result']
print(f"加密数据为：{result}")

with open("jijian.js", 'r', encoding='utf-8') as f:
    analysis_js = f.read()
    ctx = execjs.compile(analysis_js)

    # console.log(_0x3ef903(_0x3ed467(_0x4207c2(data))));
    result_data = ctx.call('get_data', result)
    print(f"解密数据为：{result_data}")

    result_dict = json.loads(result_data)
    curr_page = result_dict['currPage']
    page_size = result_dict['pageSize']
    total_count = result_dict['totalCount']
    total_page = result_dict['totalPage']

    data_list = result_dict['list']
    for item in data_list[:5]:
        w = item['w']
        h = item['h']
        i = item['i']
        t = item['t']
        print(i)

        # 下载图片，可以改为协程处理
        img_location_url = f"https://api.zzzmh.cn/bz/v3/getUrl/{i}{t}9"
        print(img_location_url)
        img_data = requests.get(img_location_url, headers=headers).content
        with open(f'{i}_{w}_{h}.png', 'wb') as f:
            f.write(img_data)
