import requests

cookies = {
    'bizuin': '3900220402',
    'data_bizuin': '3900220402',
    'data_ticket': 'Aop7cz4HbcQN+OYN8R3pvxdeaxhk9Cw9IMNIYTomjp2UZuBZnjYl7+6rYXC1QtNJ',
    'rand_info': 'CAESIMwHNlWJFDBpVFCPlXgV177iZ7pfmpbY37rGYCv/1Oas',
    'slave_bizuin': '3900220402',
    'slave_sid': 'RG5HU2JFTkU4VHhYcFdwdkh2WmtNejJQdUFNS3czU1Q5UVZJd05GODVEaFBma0QyUEdtUm1aQkRaZ1FVSmFMMTVManpOTzRmY0dma2k5RGhuVHBhVXJTaHVpUzdnMHRaWHFNMlZPT0x3bHp6NkJJUFI5UU43Wm5NeWw4eGdBYVZDWGNnN1ptbDhHZXdXV3ZC',
    'slave_user': 'gh_5edeee428f9b',
    '_clsk': '1vf5tep|1705641750721|2|1|mp.weixin.qq.com/weheat-agent/payload/record',
    'mm_lang': 'zh_CN',
    'ua_id': 'RpWqrvmDpTx0HcLqAAAAAOJkUVzkIglQB8e1zyYQPus=',
    'xid': 'dbfad326cd3345942875c7772c982be6',
    'uuid': '6909cdbee768e564c3f3a3b6c5218266',
    '_clck': '1ka1fpj|1|fij|0',
    'wxuin': '05641617905127',
    'RK': 'ReO9vP5cG1',
    'qq_domain_video_guid_verify': '636f225bac2d1be8',
}

headers = {
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'mp.weixin.qq.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=0&token=346446751&lang=zh_CN&timestamp=1705641749438',
    # 'Cookie': 'bizuin=3900220402; data_bizuin=3900220402; data_ticket=Aop7cz4HbcQN+OYN8R3pvxdeaxhk9Cw9IMNIYTomjp2UZuBZnjYl7+6rYXC1QtNJ; rand_info=CAESIMwHNlWJFDBpVFCPlXgV177iZ7pfmpbY37rGYCv/1Oas; slave_bizuin=3900220402; slave_sid=RG5HU2JFTkU4VHhYcFdwdkh2WmtNejJQdUFNS3czU1Q5UVZJd05GODVEaFBma0QyUEdtUm1aQkRaZ1FVSmFMMTVManpOTzRmY0dma2k5RGhuVHBhVXJTaHVpUzdnMHRaWHFNMlZPT0x3bHp6NkJJUFI5UU43Wm5NeWw4eGdBYVZDWGNnN1ptbDhHZXdXV3ZC; slave_user=gh_5edeee428f9b; _clsk=1vf5tep|1705641750721|2|1|mp.weixin.qq.com/weheat-agent/payload/record; mm_lang=zh_CN; ua_id=RpWqrvmDpTx0HcLqAAAAAOJkUVzkIglQB8e1zyYQPus=; xid=dbfad326cd3345942875c7772c982be6; uuid=6909cdbee768e564c3f3a3b6c5218266; _clck=1ka1fpj|1|fij|0; wxuin=05641617905127; RK=ReO9vP5cG1; qq_domain_video_guid_verify=636f225bac2d1be8',
    'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'action': 'list_ex',
    'fakeid': 'MjM5MzI5NTU3MQ==',
    'query': '',
    'begin': '0',
    'count': '4',
    'type': '9',
    'need_author_name': '1',
    'token': '346446751',
    'lang': 'zh_CN',
    'f': 'json',
    'ajax': '1',
}

response = requests.get('https://mp.weixin.qq.com/cgi-bin/appmsg', params=params, cookies=cookies, headers=headers,
                        verify=False)
print(response)
