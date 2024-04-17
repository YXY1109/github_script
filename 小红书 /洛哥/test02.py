import json
import re

import execjs
import requests

# todo,需要替换值才能获取到数据
# 第一步：获取cookie,替换：cookie_input
cookie_input = 'abRequestId=cea3d768-2b65-518a-bb05-d4ff31199fa6; a1=18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904; webId=99b33fb749cdbbf7986d24615b787288; gid=yYdSYyD40yEjyYdSYyD44K744SFhyvCT4A3iI17fTJT3CUq8uijxVj888Y2Jj848JqDKDYqD; web_session=030037a125da5339c739fea96f214a39998284; webBuild=4.12.3; unread={%22ub%22:%2265ff2336000000001302559b%22%2C%22ue%22:%226604eb04000000000d00dc9e%22%2C%22uc%22:34}; acw_tc=443b0c576c341e388e108ee5f48e3b5636f255ab48879ac268b0b90bc63bf56e; websectiga=9730ffafd96f2d09dc024760e253af6ab1feb0002827740b95a255ddf6847fc8; sec_poison_id=1be4f91b-6ad7-4738-99b7-4e132ef4bb7e; xsecappid=xhs-pc-web'

keys_to_extract = ['a1', 'web_session']
pattern = re.compile(r';\s*({})=(.*?)(?:;|$)'.format('|'.join(keys_to_extract)))
matches = pattern.findall(cookie_input)
extracted_values = {key: value for key, value in zip(keys_to_extract, matches)}

a1 = extracted_values.get('a1')[1]
web_session = extracted_values.get('web_session')[1]

cookies = {
    'a1': a1,
    'web_session': web_session,
}

headers = {'content-type': 'application/json;charset=UTF-8'}

json_data = {
    'cursor_score': '',
    'num': 39,
    'refresh_type': 1,
    'note_index': 35,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.career_v3',
    'search_key': '',
    'need_num': 14,
    'image_formats': ['jpg', 'webp', 'avif']
}

c = '/api/sns/web/v1/homefeed'

with open('补环境版.js', 'r', encoding='utf-8') as fp:
    js_code = fp.read()
    result = execjs.compile(js_code).call('get_header', (c, json_data))
    print(result)
    headers['X-S'] = result.get('X-s')
    # base64
    # headers['X-S-Common'] = base64.b64encode(result.encode(encoding='utf-8')).decode()
    # headers['X-t'] = str(result.get('X-t'))
    data = json.dumps(json_data, separators=(',', ':'))
    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                             data=data)
    print(response.text)
    data_dict = json.loads(response.text)
    pass
