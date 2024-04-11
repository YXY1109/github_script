from datetime import datetime

import execjs
import requests
from fake_useragent import UserAgent

from 福建省公共资源交易电子公众服务平台.jiemi_response import decrypt_data

# 当前时间戳
ts = int(datetime.now().timestamp() * 1000)

header_js = "jiemi_headers.js"
response_js = "jiemi_response.js"

json_data = {
    "ts": ts,
    "pageNo": 1,
    "pageSize": 20,
    "total": 3575,
    "KIND": "GCJS",
    "GGTYPE": "1",
    "timeType": "6",
    "BeginTime": "2023-10-11 00:00:00",
    "EndTime": "2024-04-11 23:59:59",
    "createTime": []
}

# 获取header，portal_sign加密值
with open(header_js, 'r', encoding='utf-8') as f:
    analysis_js = f.read()
    ctx = execjs.compile(analysis_js)
    portal_sign = ctx.call('d', json_data)

headers = {
    'User-Agent': UserAgent().random,
    'portal-sign': portal_sign,
}

response_json = requests.post(
    'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo',
    # cookies=cookies,
    headers=headers,
    json=json_data,
).json()

# 获取加密体
data = response_json['Data']
print(data)
# python
decrypted_message = decrypt_data(data)
print(decrypted_message)

print("*" * 200)

# js
with open(response_js, 'r', encoding='utf-8') as f:
    analysis_js = f.read()
    ctx = execjs.compile(analysis_js)
    decrypted_message = ctx.call('b', data)
    print(decrypted_message)
