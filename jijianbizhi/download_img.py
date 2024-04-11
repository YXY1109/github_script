import requests

headers = {
    'referer': 'https://bz.zzzmh.cn/',  # 这个是必须
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

img_location_url = 'https://api.zzzmh.cn/bz/v3/getUrl/cee1b243880411ebb6edd017c2d2eca219'

# request下载图片，保存到本地
img_data = requests.get(img_location_url, headers=headers).content
with open('a.png', 'wb') as f:
    f.write(img_data)
