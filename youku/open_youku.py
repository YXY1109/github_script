import json
import random
import re
import time
from urllib.parse import quote

import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def get_tracks(distance):
    """
    /Users/cj/PycharmProjects/github_scrapy/utils/zhihu_login_code.py
    根据偏移量获取移动轨迹
    :param distance:偏移量
    :return:移动轨迹
    """
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 5
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        tracks.append(round(move))
    return tracks


def get_slide_locus(distance):
    """
    计算出一个滑动轨迹
    :param distance:
    :return:
    """
    distance += 8
    v = 0
    m = 0.3
    # 保存0.3内的位移
    tracks = []
    current = 0
    mid = distance * 4 / 5
    while current < distance:
        if current < mid:
            a = 30
        else:
            a = -40
        v0 = v
        s = v0 * m + 0.5 * a * (m ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * m
    return tracks


def handle_slide_code_1(youku_driver, slider_width=0):
    """
    处理优酷验证码的滑动
    :param youku_driver:
    :param slider_width: x轴滑动距离
    :return:
    """

    # 滑块元素
    slider_element = youku_driver.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')

    # 滑动
    action = ActionChains(youku_driver)
    action.click_and_hold(slider_element).perform()  # 模拟按下鼠标左键
    locus = get_slide_locus(slider_width)
    for loc in locus:
        time.sleep(0.01)
        action.move_by_offset(loc, random.randint(-5, 5)).perform()
    time.sleep(0.5)
    action.release().perform()

    print("开始判断")
    try:
        print("进入页面，判断播放按钮是否存在")
        play_element = youku_driver.find_element(
            By.XPATH, "//div[@data-spm='PhoneSokuProgram_1']//a[contains(@class,'continue-play')]")
        return play_element
    except NoSuchElementException as e:
        print(f"不存在，还要滑动，点击重试")
        red_click_element = youku_driver.find_element(By.XPATH, '//*[@id="`nc_1_refresh2`"]')
        red_click_element.click()
        time.sleep(4)
        return ''


def handle_slide_code_2(youku_driver, slider_width=0):
    """
    处理优酷验证码的滑动
    :param youku_driver:
    :param slider_width: x轴滑动距离
    :return:
    """

    # 滑块元素

    slider_element = youku_driver.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')

    # 滑动
    action = ActionChains(youku_driver)
    action.click_and_hold(slider_element).perform()  # 模拟按下鼠标左键
    locus = get_slide_locus(slider_width)
    for loc in locus:
        time.sleep(0.01)
        action.move_by_offset(loc, random.randint(-5, 5)).perform()
    time.sleep(0.5)
    action.release().perform()

    print("开始判断")
    try:
        print("进入视频播放页面，判断是否存在")
        play_element = youku_driver.find_element(
            By.XPATH, "//div[@data-spm='PhoneSokuProgram_1']//a[contains(@class,'continue-play')]")
        return play_element
    except NoSuchElementException as e:
        print(f"不存在，还要滑动，点击重试")
        red_click_element = youku_driver.find_element(By.XPATH, '//*[@id="`nc_1_refresh2`"]')
        red_click_element.click()
        time.sleep(1)
        return ''


def youku(movie_name="战狼"):
    open_url = f"https://so.youku.com/search_video/q_{quote(movie_name)}?searchfrom=1"
    print(f"开始:{open_url}")

    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # 针对新版ChromeDriver可能需要此项
    options.add_argument(f"user-agent={ua.random}")

    http_ip = get_http_ip()
    # {"code":121,"data":[],"msg":"您的该套餐已经过期了"}
    print(f"代理ip:{http_ip}")
    options.add_argument(f"--proxy-server={http_ip}")  # 设置代理ip

    driver = webdriver.Chrome(options=options)
    driver.get(open_url)
    time.sleep(3)
    # 检测是否有滑块
    try:
        # 滑块背景元素
        slider_back_element = driver.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')
        # 需要滑动300
        slider_width = slider_back_element.size['width']

        print("开始处理滑块。。。")
        play_element = ''
        while 1:
            try:
                play_element = handle_slide_code_1(driver, slider_width)
                if play_element:
                    break
            except:
                continue
    except Exception as e:
        print(f"没有滑块，点击播放:{e}")
        play_element = driver.find_element(
            By.XPATH, "//div[@data-spm='PhoneSokuProgram_1']//a[contains(@class,'continue-play')]")

    # 精彩信息数据："https://v.youku.com/v_nextstage/id_7edea84a006911e59e2a.html"
    movie_play_url = play_element.get_attribute("href")
    print(f"movie_play_url:{movie_play_url}")
    driver.close()
    return movie_play_url


def get_http_ip():
    """
    使用的是太阳代理
    :return:
    """
    ip_url = "http://http.tiqu.alibabaapi.com/getip?num=1&type=1&pack=131185&port=1&lb=1&pb=45&regions="
    http_ip = requests.get(ip_url).text
    return http_ip


def get_chrome_driver():
    """获取chrome driver"""
    print("chrome 准备连接")

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-web-security')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    http_ip = get_http_ip()
    print(f"代理ip:{http_ip}")
    options.add_argument(f"--proxy-server={http_ip}")  # 设置代理ip

    driver = webdriver.Chrome(options=options)
    print("chrome 连接成功")
    return driver


def handle_html_high_data(html_str):
    """
    将接口请求的数据进行清洗，解析出亮点数据
    :param html_str:
    :return:
    """
    try:
        # 提取亮点数据的数组字符
        regex_1 = '"point":(.*),"vertical_style"'
        match_1 = re.compile(regex_1).findall(html_str)
        if match_1:
            val = match_1[0]
            # 处理title字段中存在双引号的情况
            data_str = re.sub('"title":"(.*?)",', "'title':'\\1',", val)
            point_list = eval(data_str)
            print(f"数据解析正常：{point_list}")
            return point_list
        else:
            print("没有找到亮点数据")
            return []
    except Exception as e:
        print(f"正则匹配异常：{e}")
        return []


def handle_html_mtopjsonp1(html_str):
    """
    无法直接解析，按照自己的需求，通过正则获取即可
    :param html_str:
    :return:
    """
    regex_1 = 'mtopjsonp1\((.*)\)</pre></body></html>'
    match_1 = re.compile(regex_1).findall(html_str)
    if match_1:
        val = match_1[0]
        # todo 需要再次处理才行，无法直接解析
        point_dict = json.loads(val)
        print(f"数据解析正常：{point_dict}")
        return point_dict
    else:
        print("没有匹配全部数据")
        return []


def catch_ups_appinfo(url: str):
    """
    打开指定的网页
    获取远程chrome的网络日志信息，解析出所需的请求地址
    :param url:
    :return: url
    """
    print("开始请求")
    driver = get_chrome_driver()
    driver.get(url)
    # 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
    for i in range(3):
        print(f"chrome 正在等待请求, 第{i + 1}次")
        time.sleep(1)

    # 获取精彩片段的url地址
    high_light_url = ""

    # driver.log_types
    # ['performance', 'browser', 'driver']
    log_list = driver.get_log('performance')
    # print(f"log_list:{log_list}")
    for log in log_list:
        x = json.loads(log['message'])['message']
        x_str = json.dumps(x)
        if 'https://acs.youku.com/h5/mtop.youku.play.ups.appinfo.get' in x_str and '"url": ' in x_str:
            print(f"x:{x}")
            print(f"x_str:{x_str}")
            if 'request' in x['params']:
                high_light_url = x['params']['request']['url']
            elif 'response' in x['params']:
                high_light_url = x['params']['response']['url']
            break

    # print("关闭浏览器驱动")
    # driver.close()
    print(f"获取视频精彩片段的地址:{high_light_url}")
    driver.get(high_light_url)

    high_text = driver.page_source
    print(f"亮点数据html:{high_text}")

    # 解析亮点数据
    data_list = handle_html_high_data(high_text)
    print(data_list)


def test():
    # 通过html页面获取数据
    high_text = """
    <html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;"> mtopjsonp1({"api":"mtop.youku.play.ups.appinfo.get","data":{"cost":0.109000005,"data":{"preview":{"thumb_hd":["http://m.ykimg.com/052500095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052501095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052502095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052503095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052504095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052505095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052506095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052507095F03DAAC8B295F1AC209611C","http://m.ykimg.com/052508095F03DAAC8B295F1AC209611C"],"thumb":["http://m.ykimg.com/052500095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052501095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052502095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052503095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052504095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052505095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052506095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052507095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg","http://m.ykimg.com/052508095F03DAAC8B295F1AC209611C?x-oss-process=image/resize,m_fill,limit_0,h_720,w_1280/format,jpg"],"timespan":"6000"},"clientAbility":{"dts":0,"n4k":0,"imax":0,"fps120":0,"dolby_atmos":0,"z8k":0,"dolby":0,"z10bit":0,"audio_51":0,"dolby_around":0,"dtsc":0,"z4k":0,"fps60":1,"z2k":0,"h265":0,"h266":0,"dolby_vision":0,"hdr10":0,"n10bit":0,"z1080":1},"controller":{"comment_disable":false,"yi_plus":"false","download_disable_tudou":false,"stream_config":true,"download_disable":true,"app_disable":false,"new_core":true,"post_process":false,"buy_guide":false,"continuous":false,"tipSwitch":false,"download_status":"[\"vip_allowed\"]","share_disable":false,"is_phone_stream":"0","play_mode":2,"like_disabled":false,"baipai_source":"","circle":false,"pay_info_ext":"{\"stage\":\"1\",\"can_play\":false,\"is_vip\":false,\"library_tag\":\"100001\",\"idens\":[],\"seq\":\"1\",\"sub_stage\":0}","stream_mode":1,"video_capture":true},"ad":{"VAL":[],"P":1,"VER":"3.0","REQID":"213ee5330006581107250a4200002d0b"},"watermark":[{"displayDTOS":[{"duration":0,"posX":28.0,"posY":28.0,"start":0,"width":149.0,"height":24.0}],"rsUrl":"https://ykimg.alicdn.com/product/image/2024-01-29/776b8f848181770bac479ec75841989d.png","alpha":1.0,"watermarkImgListDTOS":[],"type":17,"refWnd":1,"displayMode":0,"rsType":0,"autoScale":0,"refCoord":1},{"displayDTOS":[{"duration":0,"posX":44.0,"posY":44.0,"start":0,"width":248.0,"height":40.0}],"rsUrl":"https://ykimg.alicdn.com/product/image/2024-01-29/9f31dae2790e3e98799df87082231dee.png","alpha":1.0,"watermarkImgListDTOS":[],"type":17,"refWnd":1,"displayMode":1,"rsType":0,"autoScale":0,"refCoord":1},{"displayDTOS":[{"duration":10000,"posX":30.0,"posY":70.0,"start":0,"width":240.0,"height":20.0}],"textSize":16.0,"alpha":0.2,"watermarkImgListDTOS":[],"text":"电审故字[2014]第569号","type":3,"refWnd":0,"textColor":"#FFFFFF","displayMode":0,"rsType":1,"autoScale":1,"refCoord":2}],"playlog":{"includeHistoryRecordAd":false,"lastpoint":"0"},"fee":{"own_channel_id":0,"ad":0,"trial_type":"time","paid":1,"paid_type":["mon"],"video_type":0},"show":{"copyright":"1","show_thumburl":"http://m.ykimg.com/050B000062207F812037DD08F9D53401","show_vthumburl_huge":"http://m.ykimg.com/0534000062207F7A2037DD08F9C54213","license_num":"电审故字[2014]第569号","show_videotype":"正片","is_medium_show":false,"pay":1,"show_vthumburl_big_jpg":"http://m.ykimg.com/050E000062207F7A2037DD08F9C54213","completed":1,"show_thumburl_huge":"http://m.ykimg.com/0535000062207F812037DD08F9D53401","title":"战狼","encodeid":"117b9abc00c311e38b3f","show_vthumburl":"http://m.ykimg.com/050D000062207F7A2037DD08F9C54213","video_type":1,"stage":1,"exclusive":false,"pay_type":["mon"],"id":279682,"showcategory":"电影","video_pay":1,"show_thumburl_big_jpg":"http://m.ykimg.com/050C000062207F812037DD08F9D53401","episode_total":1},"pay":{"duration":2,"can_play":false,"discount_price":"","price":"1"},"video":{"privacy":"anybody","stream_types":{"default":["cmfv4hd3","cmfv4hd2","cmfv4hd","cmfv4sd","cmfv4ld"]},"source":5,"title":"战狼","type":["show","dvd","share","bullet","bVideoinfo","fee"],"userid":97454045,"encodeid":"XOTU5OTUwMDI4","uid":97454045,"seconds":5403.52,"category_id":96,"weburl":"http://v.youku.com/v_show/id_XOTU5OTUwMDI4.html","audioOnly":0,"logo":"https://m.ykimg.com/054101015F06DAB88E182E9AB570496D","id":239987507,"st_sorted":1,"category_letter_id":"c","limited":0,"stream_ext":{"default":{"cmfv4sd":{"codec":"H264","bitdepth":8,"size":188083304,"colorspace":"","resolu":360,"clarity_title":"流畅 360P","fps":23,"clarity_short_title":"360P","vip":0,"vr":"","mediatype":"cmfv","quality":2},"cmfv4hd":{"codec":"H264","bitdepth":8,"size":332740052,"colorspace":"","resolu":540,"clarity_title":"标清 540P","fps":23,"clarity_short_title":"540P","vip":0,"vr":"","mediatype":"cmfv","quality":3},"cmfv4hd3":{"codec":"H264","bitdepth":8,"size":1006870369,"colorspace":"","resolu":1080,"clarity_title":"高清 SDR 1080P","fps":23,"clarity_short_title":"1080P","vip":0,"vr":"","mediatype":"cmfv","quality":5},"cmfv4hd2":{"codec":"H264","bitdepth":8,"size":561222848,"colorspace":"","resolu":720,"clarity_title":"准高清 720P","fps":23,"clarity_short_title":"720P","vip":0,"vr":"","mediatype":"cmfv","quality":4},"cmfv4ld":{"codec":"H264","bitdepth":8,"size":106712484,"colorspace":"","resolu":270,"clarity_title":"省流","fps":23,"clarity_short_title":"省流","vip":0,"vr":"","mediatype":"cmfv","quality":1}}},"tags":["战狼"],"ctype":"媒资","drm_type":"cbcs","smart_tile":0,"videoid_play":239987507,"subcategories":[{"name":"大陆","id":"2034"},{"name":"动作","id":"2060"},{"name":"战争","id":"2063"}],"username":"优酷会员"},"ykad":{"VER":"3.0","REQID":"213ee5330006581107250a4200002d07"},"trial":{"trial_str":"您可以免费试看前6分钟","trial_str_end":"您可以免费试看前6分钟","time":360,"type":"time","episodes":"0","look_ten_type":2},"network":{"country_code":"CN","province":"四川省","area_code":"511100","isp":"联通","dma_code":"4837"},"dvd":{"video_features":["is_operator_drm","hdr_10","z_real","dolby_5_1"],"is_sp_pay":false,"match_show_category":"电影","show_videotype":"正片","show_video_ep":1,"point":[{"ctype":"cut","startLongVal":0,"start":"0","title":"","desc":""},{"ctype":"story","startLongVal":245821,"start":"245821","title":"吴京擅自连开三枪 击毙匪首救战友","desc":""},{"ctype":"story","startLongVal":686989,"start":"686989","title":"血性吴京吐真言 被余男召入麾下","desc":""},{"ctype":"story","startLongVal":1597993,"start":"1597993","title":"狙击手吴京远程击中敌方指挥官","desc":""},{"ctype":"standard","startLongVal":1966005,"start":"1966005","title":"","desc":""},{"ctype":"story","startLongVal":2015792,"start":"2015792","title":"夜半遇野狼围攻 白刃搏杀击退狼群","desc":""},{"ctype":"story","startLongVal":2320591,"start":"2320591","title":"战狼丛林穿越 遭荷枪实弹分子突袭","desc":""},{"ctype":"story","startLongVal":2591297,"start":"2591297","title":"外籍军团非法入境 战狼遇重重挑战","desc":""},{"ctype":"story","startLongVal":3159572,"start":"3159572","title":"中外猛男集结边境丛林 猛火力交战","desc":""},{"ctype":"story","startLongVal":3688385,"start":"3688385","title":"吴京丛林飞速移动 躲避敌方狙击手","desc":""},{"ctype":"standard","startLongVal":4117318,"start":"4117318","title":"","desc":""},{"ctype":"story","startLongVal":4153739,"start":"4153739","title":"吴京追敌踩中地雷 用妙招成功脱身","desc":""},{"ctype":"story","startLongVal":4421751,"start":"4421751","title":"吴京VS阿金斯 近身搏杀刚硬狠辣","desc":""},{"ctype":"epilogue","startLongVal":5137516,"start":"5137516","title":"影片将尽，留住精彩","desc":""},{"ctype":"story","startLongVal":5152871,"start":"5152871","title":"片尾彩蛋 NG片段吴京吐舌头卖萌","desc":""}],"vertical_style":false,"show_version_type":["默认版"],"match_show_id":279682,"is_display_hdr":true,"multi_shows_video_types":["正片"],"notsharing":"0","cast_screen_forbid_flag":"0","is_ip_play":false},"stream":[{"audio_lang":"default","milliseconds_audio":5403000,"milliseconds_video":5403000,"segs":[{"size":106712484,"total_milliseconds_video":5403000,"total_milliseconds_audio":5403000,"key":"bfe8bb7af5b207ca2415b5d9","fileid":"oss://yk-flv-sh/0300370000641A9622904C26677A04E093F1E2-4867-42CA-85CC-07EA6BD2E73D.m3u8"}],"streamLang":"default","stream_ext":{"codecs":"avc1.640015","hlsTags":"EXT-X-PRIVINF","fps":23,"hls_duration":5403000,"transPoints":"0","audioGroupId":"aac_ld","frameAlign":2,"iv":"7d79da282f0fdf6f7cb4ee12d2d27317","uri":"https://drm-license.youku.com/ups/drm.json?drmType=cbcs&amp;token=CqFLHyR3erYgTaNO5gBvRx6d0bOCC42ieej3Pw5fdJWqdwOHKi6PN4UfhNOIL84oS9NqeCkXsSKTz-KrVvXylFSx_5GRFq2p&amp;vid=XOTU5OTUwMDI4&amp;utdid=KVhLHu8okjUCAXcHtLBp5smi&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;ccode=0502&amp;mac=&amp;network=&amp;brand=&amp;osVer=&amp;appVer=&amp;clientIp=192.168.1.1&amp;clientTs=1707371054","hls_subtitle":"default","subtitle_lang":"default","hls_size":106712484,"hls_oss_bucket":2,"hls_logo":"none","oss_bucket":2},"size":106712484,"subtitle_lang":"default","media_type":"video","sourceAuidoEffect":false,"drm_type":"cbcs","stream_type":"cmfv4ld","width":480,"logo":"none","m3u8_url":"http://pl-ali.youku.com/playlist/m3u8?vid=XOTU5OTUwMDI4&amp;type=cmfv4ld&amp;ups_client_netip=7707b4b0&amp;utid=KVhLHu8okjUCAXcHtLBp5smi&amp;ccode=0502&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;streamcoding=cmfva4&amp;app_ver=9.4.60&amp;duration=5403&amp;expire=18000&amp;drm_type=19&amp;drm_device=7&amp;drm_default=16&amp;sm=1&amp;nt=1&amp;media_type=standard&amp;hotvt=1&amp;dyt=0&amp;ups_ts=1707371066&amp;onOff=48&amp;encr=0&amp;ups_key=861ff357a4940931072b931c7a14ed40&amp;cmfvType=cmfv4ld&amp;cmfaType=cmfa1ld&amp;cmfvFileId=0300370000641A9622904C26677A04E093F1E2-4867-42CA-85CC-07EA6BD2E73D-12-268238292&amp;cmfaFileId=0700060000641A961BECA0C56EC3C5E8050F92-FE10-4AA0-AE18-C4A9DECF4012-12-267833718&amp;ckt=5&amp;m_onoff=0&amp;pn=&amp;app_key=24679788&amp;drm_type_value=cbcs","height":202},{"audio_lang":"default","milliseconds_audio":5403000,"milliseconds_video":5403000,"segs":[{"size":188083304,"total_milliseconds_video":5403000,"total_milliseconds_audio":5403000,"key":"bfe8bb7af5b207ca2415b5d9","fileid":"oss://yk-flv-sh/0300380000641A965DFB62662D8F540E40D08C-1299-4588-B43A-79AD42463A19.m3u8"}],"streamLang":"default","stream_ext":{"codecs":"avc1.640015","hlsTags":"EXT-X-PRIVINF","fps":23,"hls_duration":5403000,"transPoints":"0","audioGroupId":"aac_sd","frameAlign":2,"iv":"7d79da282f0fdf6f7cb4ee12d2d27317","uri":"https://drm-license.youku.com/ups/drm.json?drmType=cbcs&amp;token=CqFLHyR3erYgTaNO5gBvRx6d0bOCC42ieej3Pw5fdJWqdwOHKi6PN4UfhNOIL84oS9NqeCkXsSKTz-KrVvXylFSx_5GRFq2p&amp;vid=XOTU5OTUwMDI4&amp;utdid=KVhLHu8okjUCAXcHtLBp5smi&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;ccode=0502&amp;mac=&amp;network=&amp;brand=&amp;osVer=&amp;appVer=&amp;clientIp=192.168.1.1&amp;clientTs=1707371054","hls_subtitle":"default","subtitle_lang":"default","hls_size":188083304,"hls_oss_bucket":2,"hls_logo":"none","oss_bucket":2},"size":188083304,"subtitle_lang":"default","media_type":"video","sourceAuidoEffect":false,"drm_type":"cbcs","stream_type":"cmfv4sd","width":640,"logo":"none","m3u8_url":"http://pl-ali.youku.com/playlist/m3u8?vid=XOTU5OTUwMDI4&amp;type=cmfv4sd&amp;ups_client_netip=7707b4b0&amp;utid=KVhLHu8okjUCAXcHtLBp5smi&amp;ccode=0502&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;streamcoding=cmfva4&amp;app_ver=9.4.60&amp;duration=5403&amp;expire=18000&amp;drm_type=19&amp;drm_device=7&amp;drm_default=16&amp;sm=1&amp;nt=1&amp;media_type=standard&amp;hotvt=1&amp;dyt=0&amp;ups_ts=1707371066&amp;onOff=48&amp;encr=0&amp;ups_key=2924a1d0b92acb936cf52457a7936106&amp;cmfvType=cmfv4sd&amp;cmfaType=cmfa1sd&amp;cmfvFileId=0300380000641A965DFB62662D8F540E40D08C-1299-4588-B43A-79AD42463A19-12-263958020&amp;cmfaFileId=0700000000641A961502E3EEEBDAB36F66456F-DABD-48A3-9BFB-7F3A5EBCA081-12-263958021&amp;ckt=5&amp;m_onoff=0&amp;pn=&amp;app_key=24679788&amp;drm_type_value=cbcs","height":268},{"audio_lang":"default","milliseconds_audio":5403000,"milliseconds_video":5403000,"segs":[{"size":332740052,"total_milliseconds_video":5403000,"total_milliseconds_audio":5403000,"key":"8733b2a89f5a4f732415b5d9","fileid":"oss://yk-flv-sh/0500CB0000641A96FFB358A3FF65BDBA9A430C-CEC9-4173-A39F-3D088DDE4E23.m3u8"}],"streamLang":"default","stream_ext":{"codecs":"avc1.64001f","hlsTags":"EXT-X-PRIVINF","fps":23,"hls_duration":5403000,"transPoints":"0","audioGroupId":"aac_sd","frameAlign":2,"iv":"7d79da282f0fdf6f7cb4ee12d2d27317","uri":"https://drm-license.youku.com/ups/drm.json?drmType=cbcs&amp;token=CqFLHyR3erYgTaNO5gBvRx6d0bOCC42ieej3Pw5fdJWqdwOHKi6PN4UfhNOIL84oS9NqeCkXsSKTz-KrVvXylFSx_5GRFq2p&amp;vid=XOTU5OTUwMDI4&amp;utdid=KVhLHu8okjUCAXcHtLBp5smi&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;ccode=0502&amp;mac=&amp;network=&amp;brand=&amp;osVer=&amp;appVer=&amp;clientIp=192.168.1.1&amp;clientTs=1707371054","hls_subtitle":"default","subtitle_lang":"default","hls_size":332740052,"hls_oss_bucket":2,"hls_logo":"none","oss_bucket":2},"size":332740052,"subtitle_lang":"default","media_type":"video","sourceAuidoEffect":false,"drm_type":"cbcs","stream_type":"cmfv4hd","width":960,"logo":"none","m3u8_url":"http://pl-ali.youku.com/playlist/m3u8?vid=XOTU5OTUwMDI4&amp;type=cmfv4hd&amp;ups_client_netip=7707b4b0&amp;utid=KVhLHu8okjUCAXcHtLBp5smi&amp;ccode=0502&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;streamcoding=cmfva4&amp;app_ver=9.4.60&amp;duration=5403&amp;expire=18000&amp;drm_type=19&amp;drm_device=7&amp;drm_default=16&amp;sm=1&amp;nt=1&amp;media_type=standard&amp;hotvt=1&amp;dyt=0&amp;ups_ts=1707371066&amp;onOff=48&amp;encr=0&amp;ups_key=9ba8c30964d8b4b46c662415c1a44088&amp;cmfvType=cmfv4hd&amp;cmfaType=cmfa1sd&amp;cmfvFileId=0500CB0000641A96FFB358A3FF65BDBA9A430C-CEC9-4173-A39F-3D088DDE4E23-12-268238293&amp;cmfaFileId=0700000000641A961502E3EEEBDAB36F66456F-DABD-48A3-9BFB-7F3A5EBCA081-12-263958021&amp;ckt=5&amp;m_onoff=0&amp;pn=&amp;app_key=24679788&amp;drm_type_value=cbcs","height":404},{"audio_lang":"default","milliseconds_audio":5403000,"milliseconds_video":5403000,"spd":1,"segs":[{"size":561222848,"total_milliseconds_video":5403000,"total_milliseconds_audio":5403000,"key":"8088081acbc130d426242f14","fileid":"oss://yk-flv-sh/0500CC0000641A96DA161BD18B1905163C1734-AD6D-493A-A72E-D3322C81F18C.m3u8"}],"streamLang":"default","stream_ext":{"codecs":"avc1.64001f","hlsTags":"EXT-X-PRIVINF","fps":23,"hls_duration":5403000,"transPoints":"0","audioGroupId":"aac_sd","frameAlign":2,"iv":"7d79da282f0fdf6f7cb4ee12d2d27317","uri":"https://drm-license.youku.com/ups/drm.json?drmType=cbcs&amp;token=CqFLHyR3erYgTaNO5gBvRx6d0bOCC42ieej3Pw5fdJWqdwOHKi6PN4UfhNOIL84oS9NqeCkXsSKTz-KrVvXylFSx_5GRFq2p&amp;vid=XOTU5OTUwMDI4&amp;utdid=KVhLHu8okjUCAXcHtLBp5smi&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;ccode=0502&amp;mac=&amp;network=&amp;brand=&amp;osVer=&amp;appVer=&amp;clientIp=192.168.1.1&amp;clientTs=1707371054","hls_subtitle":"default","subtitle_lang":"default","hls_size":561222848,"hls_oss_bucket":2,"hls_logo":"none","oss_bucket":2},"codec":"h264","fs_error":{"note":"音视频分离流不支持FS","code":-2109},"size":561222848,"subtitle_lang":"default","media_type":"video","sourceAuidoEffect":false,"drm_type":"cbcs","stream_type":"cmfv4hd2","width":1280,"logo":"none","m3u8_url":"http://pl-ali.youku.com/playlist/m3u8?vid=XOTU5OTUwMDI4&amp;type=cmfv4hd2&amp;ups_client_netip=7707b4b0&amp;utid=KVhLHu8okjUCAXcHtLBp5smi&amp;ccode=0502&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;streamcoding=cmfva4&amp;app_ver=9.4.60&amp;duration=5403&amp;expire=18000&amp;drm_type=19&amp;drm_device=7&amp;drm_default=16&amp;sm=1&amp;nt=1&amp;media_type=standard&amp;hotvt=1&amp;dyt=0&amp;ups_ts=1707371066&amp;onOff=48&amp;encr=0&amp;ups_key=a689661dd4250668ed512ebc68e40b71&amp;cmfvType=cmfv4hd2&amp;cmfaType=cmfa1sd&amp;cmfvFileId=0500CC0000641A96DA161BD18B1905163C1734-AD6D-493A-A72E-D3322C81F18C-12-268957255&amp;cmfaFileId=0700000000641A961502E3EEEBDAB36F66456F-DABD-48A3-9BFB-7F3A5EBCA081-12-263958021&amp;ckt=5&amp;m_onoff=0&amp;pn=&amp;app_key=24679788&amp;drm_type_value=cbcs","height":538},{"audio_lang":"default","milliseconds_audio":5403000,"milliseconds_video":5403000,"segs":[{"size":1006870369,"total_milliseconds_video":5403000,"total_milliseconds_audio":5403000,"key":"bfe8bb7af5b207ca2415b5d9","fileid":"oss://yk-flv-sh/03003B0000641A98D2D66334EDE85514C14E92-F8BA-455B-9DDD-6EFA3C2488BD.m3u8"}],"streamLang":"default","stream_ext":{"codecs":"avc1.640032","hlsTags":"EXT-X-PRIVINF","fps":23,"hls_duration":5403000,"transPoints":"0","audioGroupId":"aac_hd","frameAlign":2,"iv":"7d79da282f0fdf6f7cb4ee12d2d27317","uri":"https://drm-license.youku.com/ups/drm.json?drmType=cbcs&amp;token=CqFLHyR3erYgTaNO5gBvRx6d0bOCC42ieej3Pw5fdJWqdwOHKi6PN4UfhNOIL84oS9NqeCkXsSKTz-KrVvXylFSx_5GRFq2p&amp;vid=XOTU5OTUwMDI4&amp;utdid=KVhLHu8okjUCAXcHtLBp5smi&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;ccode=0502&amp;mac=&amp;network=&amp;brand=&amp;osVer=&amp;appVer=&amp;clientIp=192.168.1.1&amp;clientTs=1707371054","hls_subtitle":"default","subtitle_lang":"default","hls_size":1006870369,"hls_oss_bucket":2,"hls_logo":"none","oss_bucket":2},"size":1006870369,"subtitle_lang":"default","media_type":"video","sourceAuidoEffect":false,"drm_type":"cbcs","stream_type":"cmfv4hd3","width":1920,"logo":"none","m3u8_url":"http://pl-ali.youku.com/playlist/m3u8?vid=XOTU5OTUwMDI4&amp;type=cmfv4hd3&amp;ups_client_netip=7707b4b0&amp;utid=KVhLHu8okjUCAXcHtLBp5smi&amp;ccode=0502&amp;psid=adf7efe39920ac66fcfd7b74bde39f9741346&amp;streamcoding=cmfva4&amp;app_ver=9.4.60&amp;duration=5403&amp;expire=18000&amp;drm_type=19&amp;drm_device=7&amp;drm_default=16&amp;sm=1&amp;nt=1&amp;media_type=standard&amp;hotvt=1&amp;dyt=0&amp;ups_ts=1707371066&amp;onOff=48&amp;encr=0&amp;ups_key=274837ea5e399743b5b15696a179dc82&amp;cmfvType=cmfv4hd3&amp;cmfaType=cmfa1hd&amp;cmfvFileId=03003B0000641A98D2D66334EDE85514C14E92-F8BA-455B-9DDD-6EFA3C2488BD-12-263958022&amp;cmfaFileId=0700070000658C1262E9B58EA84A38CDA2801C-589F-4986-B21F-F825977E8EE7-12-268238291&amp;ckt=5&amp;m_onoff=0&amp;pn=&amp;app_key=24679788&amp;drm_type_value=cbcs","height":806}],"uploader":{"crm_level":1,"reason":"","uid":"UMzg5ODE2MTgw","fan_count":12355405,"avatar":{"small":"https://image.9xsecndns.cn/image/uicon/9a999c0cd11e0ebe8b08f30bbb4d24975b527b1792da71.jpg","big":"https://image.9xsecndns.cn/image/uicon/9a999c0cd11e0ebe8b08f30bbb4d24975b527b1792da71.jpg","middle":"https://image.9xsecndns.cn/image/uicon/9a999c0cd11e0ebe8b08f30bbb4d24975b527b1792da71.jpg","large":"https://image.9xsecndns.cn/image/uicon/9a999c0cd11e0ebe8b08f30bbb4d24975b527b1792da71.jpg","xlarge":"https://image.9xsecndns.cn/image/uicon/9a999c0cd11e0ebe8b08f30bbb4d24975b527b1792da71.jpg"},"show_brand":0,"certification":false,"homepage":"https://www.youku.com/profile/index/?uid=UMzg5ODE2MTgw","username":"优酷会员"},"subtitle":[{"vid":"XOTU5OTUwMDI4","subtitle_lang":"default","drm_type":"default","url":"http://sub.ykimg.com/0100640100609B3591AB6D1CA651D37ED98BAB-B33B-4112-BD72-515CAB849CC3.ass"}],"ups":{"ups_ts":"1707371066","pcad":true,"ups_client_netip":"119.7.180.176","strf":true,"refVer":1,"psid":"adf7efe39920ac66fcfd7b74bde39f9741346"},"remoteDebug":[],"user":{"uid":"","partnerVip":false,"ip":"119.7.180.176","ytid":""},"adDomain":{"wifi":"vali-g1.cp31.ott.cibntv.net","cellular":"m-vali.cp31.ott.cibntv.net"}},"e":{"code":0,"provider":"hsfprovider","desc":""}},"ret":["SUCCESS::调用成功"],"v":"1.1"})</pre></body></html>
    """
    # data_list = handle_html_high_data(html_text)
    # print(data_list)

    # handle_html_mtopjsonp1(html_text)


def main():
    # 获取播放按钮那里的href，视频播放地址
    movie_url = youku("战狼1")
    # 打开这个页面，解析数据
    catch_ups_appinfo(movie_url)


if __name__ == '__main__':
    main()
