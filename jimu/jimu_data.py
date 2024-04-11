import requests
from fake_useragent import UserAgent

from jimu.jimu_token import jimu_token_time

request_time, request_token = jimu_token_time()

headers = {
    'requesttime': str(request_time),
    'token': request_token,
    'user-agent': UserAgent().random,
}

data = {
    'focusNo': '5',
    'publishFlag': '1',
    'pageNo': '0',  # 从第0页开始
    'pageSize': '20',
    'column': '1476',  # 栏目=推荐
}

response = requests.post('https://yth.ctdsb.net/amc/client/listContentByColumn', headers=headers, data=data).json()
print(response)
# 顶部数据
for item in response['data']['focusList']:
    print(item['title'])

print("*" * 100)
# 列表数据
for item in response['data']['contentList']:
    print(item['title'])
