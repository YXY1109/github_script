import execjs
import requests

from fake_useragent import UserAgent

data = {'tag': '', 'unionid': ''}

response = requests.post('https://vipapi.qimingpian.cn/Search/industryFieldVip',
                         headers={'user-agent': UserAgent().random}, data=data).json()
encrypt_data = response['encrypt_data']

with open('qimingpian.js', 'r', encoding='utf-8') as f:
    js = f.read()
    ctx = execjs.compile(js)
    data = ctx.call('s', encrypt_data)
"""
# {'list': ['企业服务', '医疗健康', '生活服务', '人工智能', '大数据', '区块链', '教育培训', '文娱传媒', '金融', '电子商务', 'VR/AR', '旅游户外', '餐饮业', '房产家居', '汽车交通', '体育健身', '食品饮料', '物联网', '硬件', '游戏', '生产制造', '物流运输', '农业', '批发零售', '先进制造', '社交社区', '工具软件', '服装纺织', '建筑', '开采', '环保', '能源电力', '政务及公共服务', '科研及技术服务', '消费升级', '新基建', '硬科技']}
"""
print(data)
