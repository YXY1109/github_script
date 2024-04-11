import json
import execjs
import requests

cookies = {
    'a1': '18d40069d4fa8j0x8fqaddxl85ic2h97a2bchdy7i50000356250',
    'web_session': '030037a2817ab4019ea28c68ca224accd515e7',
}

headers = {
    'content-type': 'application/json;charset=UTF-8', }

json_data = {
    'cursor_score': '',
    'num': 31,
    'refresh_type': 1,
    'note_index': 24,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.career_v3',
    'search_key': '',
    'need_num': 6,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
}

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
