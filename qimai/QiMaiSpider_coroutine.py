import ast
import json
import time
import execjs
import httpx
import requests
from fake_useragent import UserAgent

import asyncio


class QiMaiSpider(object):
    def __init__(self, appid_list):
        # 需要爬哪些app的下载量
        self.appid_list = appid_list
        # 需要爬哪些渠道
        # 6=华为；4=小米；8=VIVO；9=OPPO；7=魅族；3=应用宝；2=百度；1=360
        self.market_list = [6, 4, 8, 9, 7, 3, 2, 1]
        # 生成加密串的JS文件，参考视频：https://www.bilibili.com/video/BV1q8411m7xq/
        self.js_path = "qimai_analysis.js"
        # 请求头
        self.headers = {'user-agent': UserAgent().random}
        # 数据保存
        self.data_list = list()
        # 数据上报
        self.TO_TIAN_POST_URL = ""
        # 代理参数, 七脉反扒比较严，需要使用代理
        self.spiderId = ''
        self.orderNo = ''

    @staticmethod
    def set_url_params(appid, market):
        """
        加密拼接参数
        :param appid:
        :param market:
        :return:
        """
        params = {"url": "/andapp/info", "params": {"appid": f"{appid}", "market": f"{market}"},
                  "baseURL": "https://api.qimai.cn"}
        return params

    def get_analysis(self, appid, market):
        """
        生成加密串
        :param appid:
        :param market:
        :return:
        """
        t_params = self.set_url_params(appid, market)
        print(f"1，接口参数：{t_params}")
        with open(self.js_path, 'r', encoding='utf-8') as f:
            analysis_js = f.read()
            ctx = execjs.compile(analysis_js)
            js_analysis = ctx.call('getAnalysis', t_params)
            # print(f"execjs调用JS返回的analysis：{js_analysis}")
        return js_analysis

    def get_proxy_ip(self):
        """
        获取代理IP
        http://www.xdaili.cn/api/yz?orderno=YZ20229220931NJlWlV
        10036/10038/10055   提取过快，请至少5秒提取一次
        10032   今日提取已达上限，请隔日提取或额外购买
        :return: 106.111.233.130:43841
        """
        proxy_ip = (requests.get(
            url=f'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?'
                f'spiderId={self.spiderId}&orderno={self.orderNo}&returnType=1&count=1').text).strip()

        # 频繁状态：{"ERRORCODE":"10055","RESULT":"提取太频繁,请按规定频率提取!"}
        # 正常状态：117.86.14.132:37942
        print(f"代理IP:{proxy_ip}")
        try:
            proxy_dict = ast.literal_eval(proxy_ip)
            # print(f"proxy_dict:{proxy_dict}")
            if proxy_dict.get("ERRORCODE") == "10055":
                print("睡眠5秒")
                time.sleep(5)
                return self.get_proxy_ip()
        except Exception as e:
            print(f"解析异常说明是正常返回IP，直接返回：{e}")
            return proxy_ip

    async def get_app_down_num(self, appid, market, app_name, proxy_ip):
        """
        生成接口参数，获取下载量
        :param appid: 应用id
        :param market: 市场id
        :param app_name: 应用名称
        :param proxy_ip: 代理IP
        :return:
        """
        try:
            params = {
                'analysis': self.get_analysis(appid, market),
                'appid': appid,
                'market': market,
            }
            proxies = {"http://": proxy_ip, "https://": proxy_ip}
            async with httpx.AsyncClient(proxies=proxies) as client:
                response = await client.get('https://api.qimai.cn/andapp/info',
                                            params=params, headers=self.headers, timeout=20)
            html = response.text
            print(f"response，text:{html}")
            html = html.encode('utf-8').decode('raw_unicode_escape')
            html_dict = json.loads(html)
            print(f"2，返回数据dict:{html_dict}")
            if html_dict.get("code") == 10000:
                download_num = int(html_dict.get("appInfo").get("app_download_num"))
                # print(f"下载量为：{download_num}")
                channel_name = self.get_channel_name(market)
                print(f"应用市场为：{channel_name}；应用名称：{app_name}；下載量：{download_num}；APPID：{appid}")
                print("-" * 100)
                if download_num > 0:
                    post_data = {"appname": app_name, "channelname": channel_name,
                                 "log_time": time.strftime("%Y%m%d%H%M%S", time.localtime()),
                                 "num": download_num,
                                 "appid": appid}
                    self.data_list.append(post_data)
            else:
                # {'code': 10605, 'msg': '当前网络或账号异常，请半小时后重试', 'is_logout': 0, 'banip': '183.230.167.245'}
                # 说明IP被ban，使用新的IP。先重置IP，再请求
                print("IP被ban,先重置IP，再请求")
        except Exception as e:
            print(f"获取下载量异常,get_app_down_num()：{e}")

    @staticmethod
    def get_channel_name(market):
        """
        获取应用市场名称
        :param market:
        :return:
        """
        channel_name = 0
        if market == 6:
            channel_name = '华为'
        if market == 4:
            channel_name = '小米'
        if market == 8:
            channel_name = 'VIVO'
        if market == 9:
            channel_name = 'OPPO'
        if market == 7:
            channel_name = '魅族'
        if market == 3:
            channel_name = '应用宝'
        if market == 2:
            channel_name = '百度'
        if market == 1:
            channel_name = '360'
        return channel_name

    def save_data(self):
        """
        获取下载量，保存数据
        :return:
        """
        loop = asyncio.get_event_loop()
        tasks = []

        ip_count = len(self.appid_list)
        proxy_url = f"http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?" \
                    f"spiderId={self.spiderId}&orderno={self.orderNo}&returnType=1&count={ip_count}"

        proxy_ip = requests.get(url=proxy_url).text.strip()
        # 频繁状态：{"ERRORCODE":"10055","RESULT":"提取太频繁,请按规定频率提取!"}
        # 正常状态：117.86.14.132:37942
        print(f"代理IP:{proxy_ip}")
        proxy_ip_list = proxy_ip.split('\r\n')

        for index, appid_dict in enumerate(self.appid_list):
            app_id = appid_dict.get("appid")
            app_name = appid_dict.get("appname")
            http_proxy_ip = "http://{}".format(proxy_ip_list[index])
            print(f"应用名称：《{app_name}》的代理IP为：{http_proxy_ip}")
            for market in self.market_list:
                tasks.append(self.get_app_down_num(app_id, market, app_name, http_proxy_ip))
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        print(f"上报的数据：{self.data_list}")

    def upload_data(self):
        """
        数据上报
        :return:
        """
        post_data_dict = json.dumps({"jobName": "app_download", "versionNo": "V1",
                                     "datas": self.data_list})
        headers = {"h1": "v1", "h2": "v2"}
        result_dict = {"headers": headers, "body": post_data_dict}
        new_post_data = "[" + json.dumps(result_dict) + "]"
        print(f"新的-上报的JSON数据：{new_post_data}")

        # post_result = requests.post(
        #     url=self.TO_TIAN_POST_URL,
        #     data=new_post_data,
        #     verify=False,
        #     headers={'content-type': 'application/json'})
        # print(f"2上报数据结果：{post_result.status_code}")
        # print(f"3上报数据结果：{post_result.text}")


if __name__ == '__main__':
    """
    httpx 异步协程
    问题：
    同一个IP被全部请求使用，导致靠近后边的ip失效
    加入到协程中，IP失效就无法使用了
    方案1：
    每个app用一个ip，一次性获取N个ip，测试问题不大
    """
    start = time.time()
    # 测试直播游仙和甘洛融媒1014137
    appid_dict_list = [{"appname": "直播游仙", "appid": 4435278}, {"appname": "甘洛融媒", "appid": 7764243},
                       {"appname": "直播绵阳", "appid": 1014137}, {"appname": "美丽阿坝", "appid": 8932947}]
    qi_mai = QiMaiSpider(appid_dict_list)
    qi_mai.save_data()
    qi_mai.upload_data()

    # 12秒
    print("耗时：{}秒".format(time.time() - start))
