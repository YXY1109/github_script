import hashlib
import time

import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID': '620436524@10.110.96.153',
    'OUTFOX_SEARCH_USER_ID_NCOO': '531791071.5702876',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=620436524@10.110.96.153; OUTFOX_SEARCH_USER_ID_NCOO=531791071.5702876',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_sign(localtime):
    d = "fanyideskweb"
    # e = "asdjnjfenknafdfsdfsd"
    e = "fsdsogkndfokasodnaso"  # 通过webtranslate/key获取的
    u = "webfanyi"
    data = f"client={d}&mysticTime={localtime}&product={u}&key={e}"
    print(f"data:{data}")
    sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
    print(f"sign:{sign}")
    return sign


localtime = str(int(time.time() * 1000))
# localtime = 1699447999854
print(f"location:{localtime}")

data = {
    'i': 'hello',
    'from': 'auto',
    'to': '',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    # 'sign': '2a05c5811dae5c88043f4a9d5a7a11be',  # 变化
    'sign': get_sign(localtime),  # 变化
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    # 'mysticTime': '1699434044237',
    'mysticTime': str(localtime),
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
print(response)
print(response.text)
print(response.status_code)
