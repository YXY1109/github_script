import json
import re

import execjs
import requests

# todo,需要替换值才能获取到数据
# 第一步：获取cookie,替换：cookie_input
cookie_input = 'abRequestId=cea3d768-2b65-518a-bb05-d4ff31199fa6; a1=18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904; webId=99b33fb749cdbbf7986d24615b787288; gid=yYdSYyD40yEjyYdSYyD44K744SFhyvCT4A3iI17fTJT3CUq8uijxVj888Y2Jj848JqDKDYqD; xsecappid=xhs-pc-web; web_session=030037a125da5339c739fea96f214a39998284; webBuild=4.12.3; acw_tc=a1e3a5361169e6638b17db884eae9fc4d8ae4767afe46320f2f70902b6d27d20; unread={%22ub%22:%226610a6af000000001b00f0c8%22%2C%22ue%22:%2266083c89000000001a00e08b%22%2C%22uc%22:34}; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=de07fa04-79bd-4274-b456-10a7e3523b7c'

keys_to_extract = ['a1', 'web_session']
pattern = re.compile(r';\s*({})=(.*?)(?:;|$)'.format('|'.join(keys_to_extract)))
matches = pattern.findall(cookie_input)
extracted_values = {key: value for key, value in zip(keys_to_extract, matches)}

a1 = extracted_values.get('a1')[1]
web_session = extracted_values.get('web_session')[1]

cookies2 = {
    'a1': a1,
    'web_session': web_session,
}

cookies = {
    'abRequestId': 'cea3d768-2b65-518a-bb05-d4ff31199fa6',
    'a1': '18ec81b444crv1yxk4qifdk2kixzf9hjw6np9u4lu30000852904',
    'webId': '99b33fb749cdbbf7986d24615b787288',
    'gid': 'yYdSYyD40yEjyYdSYyD44K744SFhyvCT4A3iI17fTJT3CUq8uijxVj888Y2Jj848JqDKDYqD',
    'xsecappid': 'xhs-pc-web',
    'web_session': '030037a125da5339c739fea96f214a39998284',
    'webBuild': '4.12.3',
    'acw_tc': 'a1e3a5361169e6638b17db884eae9fc4d8ae4767afe46320f2f70902b6d27d20',
    'unread': '{%22ub%22:%226610a6af000000001b00f0c8%22%2C%22ue%22:%2266083c89000000001a00e08b%22%2C%22uc%22:34}',
    'websectiga': '8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee',
    'sec_poison_id': 'de07fa04-79bd-4274-b456-10a7e3523b7c',
}


headers = {'content-type': 'application/json;charset=UTF-8',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', }

json_data = {
    'cursor_score': '',
    'num': 39,
    'refresh_type': 1,
    'note_index': 33,
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

s = "/api/sns/web/v1/homefeed"

with open('补环境版.js', 'r', encoding='utf-8') as fp:
    js_code = fp.read()
    result = execjs.compile(js_code).call('get_header', (json_data, s))
    print(result)
    headers['X-S'] = result.get('X-s')
    # base64
    # headers['X-S-Common'] = base64.b64encode(result.encode(encoding='utf-8')).decode()
    headers['X-t'] = str(result.get('X-t'))
    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                             data=json_data)
    print(response.text)
    data_dict = json.loads(response.text)
    pass
