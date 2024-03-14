import requests

"""headers，不同的地方
x-emas-gw-c-traceid
crequestid
cclientrequestid
x-emas-gw-sign
x-emas-gw-t

"""
headers = {
    'appVersion': '9.16.0',
    'x-emas-gw-nq': 'WIFI',
    'x-emas-gw-utdid': 'ZfKPQc3Udx0DAKxoKzKNhk1v',
    'channel': '702006',
    'seerSdkVersion': '2.0.1.0',
    'ua': 'Android/12 (Redmi cn.cntvnews;zh_CN) App/4.5.15 AliApp() 22021211RC/11358758 Channel/702006 language/zh-CN Device/CCNews CCNews/9.16.0',
    'resolution': '1080*1920',
    'x-emas-gw-features': '27',
    'queryFlag': '0',
    'x-emas-gw-auth-ticket': '20000008',
    'model': '22021211RC',
    'appKey': 'cctvnews_app',
    'x-emas-gw-c-traceid': 'ZfKPQc3Udx0DAKxoKzKNhk1v1710423772552008215392',
    'cache-control': 'no-cache',
    'brand': 'Redmi',
    'seerSessionId': 'f_69221630-1459-4361-ba72-2974bc422d66_1710409440192',
    'x-emas-gw-appkey': '20000008',
    'app': 'cctvnews_app',
    'f-refer': 'mtop',
    'crequestid': '1710423773614539281',
    'netType': '1',
    'utdid': 'ZfKPQc3Udx0DAKxoKzKNhk1v',
    'cclientrequestid': 'zB+ZPxAWypATqnR3w/EpAVljSqDrNtdcLoLHTfIvd8jbq3EQd31aik4YYbw8h2fxXgN9f/YbnGF/j4uHgJtVycUfaoA+4EejS+8YMfunxy8MjDKB0fsPW2CLC8bTWGEu',
    'vc': '91600',
    'vn': '9.16.0',
    'crequestfrom': '1',
    'x-emas-gw-sign': 'fa75353f0f1aaafb2455dfa766b0d6cebec232dde285c4afe6e8a4a6c99d1169',
    'pull_type': '7',
    'x-emas-gw-nettype': 'WIFI',
    'x-emas-gw-pv': '6.1',
    'timezone': '28800',
    'network': 'wifi',
    'uTag': '0',
    'osVersion': '12',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'os': 'Android',
    'x-emas-gw-ttid': '702006%40CCNews_Android_9.16.0',
    'capplaunchid': '6dbb70e6-e73a-48a2-8a3d-ad5f797e8dc8_1710406157427',
    'platformId': '1',
    'uPrefRes': '0',
    'userId': '531621056977444871',
    'x-emas-gw-app-ver': '9.16.0',
    'carrier': '%E7%A7%BB%E5%8A%A8',
    'ahasFlag': '0',
    'x-emas-gw-t': '1710423772',
    'ahasExpire': '0',
    'deviceModel': '22021211RC',
    'x-emas-gw-app-conf-v': '0',
    'user-agent': 'MTOPSDK%2F3.0.6+%28Android%3B12%3BRedmi%3B22021211RC%29',
    'Host': 'emas-api.cctvnews.cctv.com',
}

"""params，不同的地方
x-emas-gw-t
recoid
"""
params = {
    'auto': '0',
    'pull_type': '7',
    'method': 'new',
    'latitude': '0.0',
    'dn': 'test_uid',
    'itime': '1710422778790',
    'platform': '0',
    'transfer_info': '20|0[iflowEnd]CAESFwgBEIPUy68GGOCE4O7-3aDUpgEgACgAGhgxMDI5MGM2MTk0NDRhYzE3MDI0NTAwMHEgADAAOgIIAUgBUhgxMDI5MGM2MTk0NDRhYzE3MDI0NTAwMHFiGggBEPr1y68GGK7098OIzv-j4gEgACjMmbNmag0IrvT3w4jO_6PiARgZagwIzbW_hpmujcRDGBlqDQic3ZabgYWC8osBGBlqDAjigZuoy5PrjiEYGWoMCK7Opq65rIGKdxgZag0ImevBorimj7KkARgZagwIn-zervT-zYJiGBlqDAj55dbR1bnirRQYGWoMCLGe2q6Q2cmLGxgZag0I-8S6svHJ_ZKZARgZag0I1IbNyICZlfPYARgZag0I5aOXtf-x1r7yARgZag0I8u2-q9jXsIbZARgZagwIwbKhmKrJ_bEWGBlqDAjxv5KM-7nI-jcYGWoMCJnfobSlv_zUXxgZagwIqoykxdSjw5lFGBlqDAi3uIG2pvK72HoYGWoNCM2ItJuvwYyC9wEYGWoNCOCE4O7-3aDUpgEYGYoBFwgBEPr1y68GGK7098OIzv-j4gEgACgAkAEB',
    'tab': '16',
    'cur_page_index': '1',
    'recoid': '10290c619444ac170245000q',
    'cache_count': '20',
    'channelId': '1119',
    'longitude': '0.0',
}

response = requests.get(
    'https://emas-api.cctvnews.cctv.com/gw/emas.feed.iflow.server.getchannelitems/1.0.0/',
    params=params,
    headers=headers,
)

print(response.status_code)
print(response.text)
