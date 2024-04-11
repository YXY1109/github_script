import requests

headers = {
    'referer': 'https://bz.zzzmh.cn/',  # 这个是必须
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

# 下载图片，可以改为协程处理
img_location_url = 'https://api.zzzmh.cn/bz/v3/getUrl/cee1b243880411ebb6edd017c2d2eca219'
print(img_location_url)
img_location_headers = requests.get(img_location_url, headers=headers, allow_redirects=False)
# 重定向地址
location_url = img_location_headers.headers.get('Location')
img_data = requests.get(location_url, headers=headers).content
# with open(f'{i}_{w}_{h}.png', 'wb') as f:
with open(f'b.png', 'wb') as f:
    f.write(img_data)
