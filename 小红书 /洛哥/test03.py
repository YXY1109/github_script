import requests

cookies = {
    'abRequestId': 'cea3d768-2b65-518a-bb05-d4ff31199fa6',
    'a1': '18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904',
    'webId': '99b33fb749cdbbf7986d24615b787288',
    'gid': 'yYdSYyD40yEjyYdSYyD44K744SFhyvCT4A3iI17fTJT3CUq8uijxVj888Y2Jj848JqDKDYqD',
    'xsecappid': 'xhs-pc-web',
    'web_session': '030037a125da5339c739fea96f214a39998284',
    'webBuild': '4.12.3',
    'unread': '{%22ub%22:%226600ed2f000000000d00c0ee%22%2C%22ue%22:%22660b4e1100000000040191ee%22%2C%22uc%22:34}',
    'websectiga': '3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad',
    'sec_poison_id': 'b35cf058-b787-4f92-b327-04b14f1d1c01',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'abRequestId=cea3d768-2b65-518a-bb05-d4ff31199fa6; a1=18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904; webId=99b33fb749cdbbf7986d24615b787288; gid=yYdSYyD40yEjyYdSYyD44K744SFhyvCT4A3iI17fTJT3CUq8uijxVj888Y2Jj848JqDKDYqD; xsecappid=xhs-pc-web; web_session=030037a125da5339c739fea96f214a39998284; webBuild=4.12.3; unread={%22ub%22:%226600ed2f000000000d00c0ee%22%2C%22ue%22:%22660b4e1100000000040191ee%22%2C%22uc%22:34}; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=b35cf058-b787-4f92-b327-04b14f1d1c01',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-b3-traceid': '5307f31ed8ca691b',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImE5Y2UxMGI4ZDRjOGFmMTQ1MjMwN2UyOWIyZThjMGIxOTQ0NDg5NWRhZjY4NjZiNDk0MzRlYWE3ZTA4ZmQ1N2U5YTE2NWJhZWQ3MTU4OGY1NjEwN2I1MjQ5ZmRkYmYxOGM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTkyYjcxNmUwMzNlYjI3Y2UxODFiMjU4MmE2YzM3MDNiYjQxYzQwMzg2ZmNjNmQ0MzNkOTkzOTNmYzgyMDFiNzdhNjk5ZDYxZTFiODhlN2RhODBkZWQ1YzlkZmMyOTc4ZDI1ZjQ3NzQ3MDMwY2ZiZDlhNmQ5NmVmNjZhYzc5NDIxNDQ3NWFiZWRmNjkyNzhkN2ZjMGI0ZGVkNDkwZGI0ZTNhN2RmNTVjMGY2MGU1ZWUwNjQ5MGQxZWVkZmEzNGQ2OCJ9',
    'x-s-common': '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',
    'x-t': '1713357948760',
}

json_data = {
    'cursor_score': '',
    'num': 39,
    'refresh_type': 1,
    'note_index': 25,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed_recommend',
    'search_key': '',
    'need_num': 14,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': False,
}

response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers, json=json_data)
print(response.status_code)
print(response.text)