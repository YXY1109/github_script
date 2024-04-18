import requests

cookies = {
    '__ac_signature': '_02B4Z6wo00f01qum4-gAAIDDRYMnF01ekf6rhudAAM8g66',
    'tt_webid': '7348297685277492751',
    'ttcid': '710a2eb22b3947f08dda9b86d058cd1083',
    's_v_web_id': 'verify_ltzazh47_8bddljoD_jEzT_4snt_85Tt_OFwRXxUa9B4Q',
    '_ga': 'GA1.1.1336094011.1710908909',
    'local_city_cache': '%E9%87%8D%E5%BA%86',
    'csrftoken': '600152e9ace3ebe482eceb1972e43180',
    'passport_csrf_token': '6dcb2e132bf169697956584ccfd2cf51',
    'passport_csrf_token_default': '6dcb2e132bf169697956584ccfd2cf51',
    'n_mh': 'QFUuWWzeQHRY96IM6NsPHPsRpCTCL2fvE1j79PDeTDo',
    'sso_uid_tt': 'fcfd2c7f0e76fd4de78dee933477a1ba',
    'sso_uid_tt_ss': 'fcfd2c7f0e76fd4de78dee933477a1ba',
    'toutiao_sso_user': 'dfd16a34a7de92082065e7fc83cad81a',
    'toutiao_sso_user_ss': 'dfd16a34a7de92082065e7fc83cad81a',
    'sid_ucp_sso_v1': '1.0.0-KGM5ODkyYWYwOTBkOGYyMDhjNWEwYmRiY2JkYTk2YTllZGY0ZDIzOWUKHgjo1MCKyPWCAxDbjvqvBhgYIAww76qg7gU4BkD0BxoCaGwiIGRmZDE2YTM0YTdkZTkyMDgyMDY1ZTdmYzgzY2FkODFh',
    'ssid_ucp_sso_v1': '1.0.0-KGM5ODkyYWYwOTBkOGYyMDhjNWEwYmRiY2JkYTk2YTllZGY0ZDIzOWUKHgjo1MCKyPWCAxDbjvqvBhgYIAww76qg7gU4BkD0BxoCaGwiIGRmZDE2YTM0YTdkZTkyMDgyMDY1ZTdmYzgzY2FkODFh',
    'passport_auth_status': '098f5cefd5952e1ff52681ece8c911b6%2C',
    'passport_auth_status_ss': '098f5cefd5952e1ff52681ece8c911b6%2C',
    'sid_guard': '9acbffbf07d205dddc3e85995c6764ef%7C1711179612%7C5184001%7CWed%2C+22-May-2024+07%3A40%3A13+GMT',
    'uid_tt': '25823f4ac890eeb8f675c627539a80a3',
    'uid_tt_ss': '25823f4ac890eeb8f675c627539a80a3',
    'sid_tt': '9acbffbf07d205dddc3e85995c6764ef',
    'sessionid': '9acbffbf07d205dddc3e85995c6764ef',
    'sessionid_ss': '9acbffbf07d205dddc3e85995c6764ef',
    'sid_ucp_v1': '1.0.0-KDI2OTYzMGUwYzRmNWU5ZWQ1YTI0M2JmYzIxYzRjN2ExOGIxMWY5YjUKGAjo1MCKyPWCAxDcjvqvBhgYIAw4BkD0BxoCbHEiIDlhY2JmZmJmMDdkMjA1ZGRkYzNlODU5OTVjNjc2NGVm',
    'ssid_ucp_v1': '1.0.0-KDI2OTYzMGUwYzRmNWU5ZWQ1YTI0M2JmYzIxYzRjN2ExOGIxMWY5YjUKGAjo1MCKyPWCAxDcjvqvBhgYIAw4BkD0BxoCbHEiIDlhY2JmZmJmMDdkMjA1ZGRkYzNlODU5OTVjNjc2NGVm',
    'store-region': 'cn-cq',
    'store-region-src': 'uid',
    '_tea_utm_cache_24': '{%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}',
    '_tea_utm_cache_2018': '{%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}',
    'odin_tt': '63c218cec1d76a89ed2057f5da9b5df4840b7cd746bae90d4014b11bfa7b815068d7c79dd5833c9b45c02da30c3804ba',
    'msToken': '_ed5X9p4Jc4kJYwTv5tIrt1uvA6IriXiiupPWB0KpFpbW0_NiAEplOrduf3oFUy0Nb6ypc4pbWHdLGuV4oktQKhatm76WnlUDpxv96Jw',
    '_ga_QEHZPBE5HH': 'GS1.1.1713415604.22.0.1713415604.0.0.0',
    'tt_anti_token': 'kT2My8jh3fJBEVl-834e6900f4576e4319b05e7416566bb767b8aef96b1f86c88d295cd4d31536e3',
    'tt_scid': '.jfzlg1xgn1XU1a-BYj4iRb1A0pDA7EAMCk7LSlL0eJQRkRLEdU6Rjv2BBWwCyqyf64c',
    'ttwid': '1%7CEyahkr1OyQOa5xDV0gbZSG3X4y3c1KxsckTF-ba4xt8%7C1713415604%7C855a8fdb4353c282620eb0eecc61c498fd425002ea1665ffc6ffa3429eb159a0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__ac_signature=_02B4Z6wo00f01qum4-gAAIDDRYMnF01ekf6rhudAAM8g66; tt_webid=7348297685277492751; ttcid=710a2eb22b3947f08dda9b86d058cd1083; s_v_web_id=verify_ltzazh47_8bddljoD_jEzT_4snt_85Tt_OFwRXxUa9B4Q; _ga=GA1.1.1336094011.1710908909; local_city_cache=%E9%87%8D%E5%BA%86; csrftoken=600152e9ace3ebe482eceb1972e43180; passport_csrf_token=6dcb2e132bf169697956584ccfd2cf51; passport_csrf_token_default=6dcb2e132bf169697956584ccfd2cf51; n_mh=QFUuWWzeQHRY96IM6NsPHPsRpCTCL2fvE1j79PDeTDo; sso_uid_tt=fcfd2c7f0e76fd4de78dee933477a1ba; sso_uid_tt_ss=fcfd2c7f0e76fd4de78dee933477a1ba; toutiao_sso_user=dfd16a34a7de92082065e7fc83cad81a; toutiao_sso_user_ss=dfd16a34a7de92082065e7fc83cad81a; sid_ucp_sso_v1=1.0.0-KGM5ODkyYWYwOTBkOGYyMDhjNWEwYmRiY2JkYTk2YTllZGY0ZDIzOWUKHgjo1MCKyPWCAxDbjvqvBhgYIAww76qg7gU4BkD0BxoCaGwiIGRmZDE2YTM0YTdkZTkyMDgyMDY1ZTdmYzgzY2FkODFh; ssid_ucp_sso_v1=1.0.0-KGM5ODkyYWYwOTBkOGYyMDhjNWEwYmRiY2JkYTk2YTllZGY0ZDIzOWUKHgjo1MCKyPWCAxDbjvqvBhgYIAww76qg7gU4BkD0BxoCaGwiIGRmZDE2YTM0YTdkZTkyMDgyMDY1ZTdmYzgzY2FkODFh; passport_auth_status=098f5cefd5952e1ff52681ece8c911b6%2C; passport_auth_status_ss=098f5cefd5952e1ff52681ece8c911b6%2C; sid_guard=9acbffbf07d205dddc3e85995c6764ef%7C1711179612%7C5184001%7CWed%2C+22-May-2024+07%3A40%3A13+GMT; uid_tt=25823f4ac890eeb8f675c627539a80a3; uid_tt_ss=25823f4ac890eeb8f675c627539a80a3; sid_tt=9acbffbf07d205dddc3e85995c6764ef; sessionid=9acbffbf07d205dddc3e85995c6764ef; sessionid_ss=9acbffbf07d205dddc3e85995c6764ef; sid_ucp_v1=1.0.0-KDI2OTYzMGUwYzRmNWU5ZWQ1YTI0M2JmYzIxYzRjN2ExOGIxMWY5YjUKGAjo1MCKyPWCAxDcjvqvBhgYIAw4BkD0BxoCbHEiIDlhY2JmZmJmMDdkMjA1ZGRkYzNlODU5OTVjNjc2NGVm; ssid_ucp_v1=1.0.0-KDI2OTYzMGUwYzRmNWU5ZWQ1YTI0M2JmYzIxYzRjN2ExOGIxMWY5YjUKGAjo1MCKyPWCAxDcjvqvBhgYIAw4BkD0BxoCbHEiIDlhY2JmZmJmMDdkMjA1ZGRkYzNlODU5OTVjNjc2NGVm; store-region=cn-cq; store-region-src=uid; _tea_utm_cache_24={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}; _tea_utm_cache_2018={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}; odin_tt=63c218cec1d76a89ed2057f5da9b5df4840b7cd746bae90d4014b11bfa7b815068d7c79dd5833c9b45c02da30c3804ba; msToken=_ed5X9p4Jc4kJYwTv5tIrt1uvA6IriXiiupPWB0KpFpbW0_NiAEplOrduf3oFUy0Nb6ypc4pbWHdLGuV4oktQKhatm76WnlUDpxv96Jw; _ga_QEHZPBE5HH=GS1.1.1713415604.22.0.1713415604.0.0.0; tt_anti_token=kT2My8jh3fJBEVl-834e6900f4576e4319b05e7416566bb767b8aef96b1f86c88d295cd4d31536e3; tt_scid=.jfzlg1xgn1XU1a-BYj4iRb1A0pDA7EAMCk7LSlL0eJQRkRLEdU6Rjv2BBWwCyqyf64c; ttwid=1%7CEyahkr1OyQOa5xDV0gbZSG3X4y3c1KxsckTF-ba4xt8%7C1713415604%7C855a8fdb4353c282620eb0eecc61c498fd425002ea1665ffc6ffa3429eb159a0',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo0090151rPfAAAIDCc075DSnwk6-dTzlAAIGCmMZ0gburFb7ikTrcJ6mdb7ZzPRmFjQP7gzLKbe5WHob4w-jkvYXuB7fWtSgz.sw8nSN9nR0laiATo8nsyshGK5CjlW.NtqjvUAiG21',
    # cookies=cookies,
    # headers=headers,
)

response2 = requests.get(
    "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&app_name=toutiao_web")

print(response2.text)
