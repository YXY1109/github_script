import json

import execjs
import requests

cookies = {
    'a1': '18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904',
    'web_session': '030037a125da5339c7396bc86e214a5966e52c',
}

headers = {
    'content-type': 'application/json;charset=UTF-8',
    # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

json_data = {
    'cursor_score': '',
    'num': 39,
    'refresh_type': 1,
    'note_index': 35,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.fashion_v3',
    'search_key': '',
    'need_num': 14,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': 'false',
}

# response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
#                          data=json_data)
# print(response.text)

c = '/api/sns/web/v1/homefeed'

with open('vm.js', 'r', encoding='utf-8') as fp:
    js_code = fp.read()
    result = execjs.compile(js_code).call('get_encrypt', (c, json_data))
    print(result)
    headers['x-s'] = result
    data = json.dumps(json_data, separators=(',', ':'))
    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                             data=data)
    print(response.text)
