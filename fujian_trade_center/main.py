import requests

cookies = {
    'ASP.NET_SessionId': 'o0yhrzzegq1qaocqqsnvbdaw',
    'Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30': '1710549418',
    'Hm_lpvt_9d1de05cc99f08ddb5dc6d5e4d32ad30': '1710549418',
    'Hm_lvt_db393520fa240b442a13a6d1c5ae95c1': '1710549418',
    'Hm_lpvt_db393520fa240b442a13a6d1c5ae95c1': '1710549418',
    '_qddagsx_02095bad0b': '1ec70fe2fd94f0fc56d7412771ebb2eb0c9aee25538bcf1b9ec4836a26b5fa794fe96e8dcd758538e1dadd16305796e50c6a63dc89cdeaf332fa411f622f5090177041b536c40b80812158ca4f6b51cb28b63f4ae283c9b9963fcb11022a3b395af1016c8d9ff25505568f0c659d596cbba63248247f9a35928d2b956cf743b2',
    'Hm_lvt_94bfa5b89a33cebfead2f88d38657023': '1710549418',
    'Hm_lpvt_94bfa5b89a33cebfead2f88d38657023': '1710549418',
    '__root_domain_v': '.fujian.gov.cn',
    '_qddaz': 'QD.649510549418585',
    '_qdda': '4-1.1qo7ru',
    '_qddab': '4-cqewnr.lttcyiks',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=o0yhrzzegq1qaocqqsnvbdaw; Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30=1710549418; Hm_lpvt_9d1de05cc99f08ddb5dc6d5e4d32ad30=1710549418; Hm_lvt_db393520fa240b442a13a6d1c5ae95c1=1710549418; Hm_lpvt_db393520fa240b442a13a6d1c5ae95c1=1710549418; _qddagsx_02095bad0b=1ec70fe2fd94f0fc56d7412771ebb2eb0c9aee25538bcf1b9ec4836a26b5fa794fe96e8dcd758538e1dadd16305796e50c6a63dc89cdeaf332fa411f622f5090177041b536c40b80812158ca4f6b51cb28b63f4ae283c9b9963fcb11022a3b395af1016c8d9ff25505568f0c659d596cbba63248247f9a35928d2b956cf743b2; Hm_lvt_94bfa5b89a33cebfead2f88d38657023=1710549418; Hm_lpvt_94bfa5b89a33cebfead2f88d38657023=1710549418; __root_domain_v=.fujian.gov.cn; _qddaz=QD.649510549418585; _qdda=4-1.1qo7ru; _qddab=4-cqewnr.lttcyiks',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'portal-sign': 'ef626869179660d73f1aef257e959127',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'pageNo': 2,
    'pageSize': 20,
    'total': 3605,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2023-09-16 00:00:00',
    'EndTime': '2024-03-16 23:59:59',
    'createTime': [],
    'ts': 1710550538773,
}

response = requests.post(
    'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)

"""
搜索关键词：decrypt(
"""

print(response.text)
print(response.status_code)
