import json
import urllib.parse

import requests
from fake_useragent import UserAgent
from lxml import etree


def get_result_url():
    """
    获取结果的请求地址,中文url编码
    :return:
    """
    url_name = "结果"
    url_encoded = urllib.parse.quote(url_name)
    # %E7%BB%93%E6%9E%9C
    print(f"url_encoded:{url_encoded}")
    result_url = f"https://www.16personalities.com/ch/{url_encoded}"
    print(f"result_url:{result_url}")
    return result_url


def get_16personalities_type(my_answer=2, gender="Female"):
    """
    answer:从左到右，-3，-2，-1，0，1，2，3
    :param my_answer: 答案
    :param gender: 性别
    :return: 人格类型
    """
    # 上传答案的请求地址，post
    result_url = get_result_url()
    # 问题和答案
    result_json = {
        "extraData": [],
        "gender": gender,
        "inviteCode": "",
        "questions": [
            {
                "text": "您经常交新朋友。",
                "answer": my_answer
            },
            {
                "text": "您花了很多空闲时间探索各种激起您兴趣的随机主题。",
                "answer": my_answer
            },
            {
                "text": "看到别人哭很容易让您觉得自己也想哭。",
                "answer": my_answer
            },
            {
                "text": "您通常会为备份计划制定备份计划。",
                "answer": my_answer
            },
            {
                "text": "您通常保持冷静，即使在很大的压力下。",
                "answer": my_answer
            },
            {
                "text": "在社交活动中，您很少尝试向新人介绍自己，而主要是与您已经认识的人交谈。",
                "answer": my_answer
            },
            {
                "text": "您更喜欢在开始另一个项目之前完全完成本个项目。",
                "answer": my_answer
            },
            {
                "text": "您很多愁善感。",
                "answer": my_answer
            },
            {
                "text": "您喜欢使用组织工具，如日程表和列表。",
                "answer": my_answer
            },
            {
                "text": "即使是一个小错误也会让您怀疑自己的整体能力和知识水平。",
                "answer": my_answer
            },
            {
                "text": "只要走到一个您觉得有趣的人身边，然后开始一段谈话，您就会觉得很舒服。",
                "answer": my_answer
            },
            {
                "text": "您对讨论创意作品的各种诠释和分析不太感兴趣。",
                "answer": my_answer
            },
            {
                "text": "您更倾向于跟随您的头脑而不是您的心。",
                "answer": my_answer
            },
            {
                "text": "您通常更喜欢在任何给定时刻做自己想做的事情，而不是计划特定的日常工作。",
                "answer": my_answer
            },
            {
                "text": "您很少担心您是否给您遇到的人留下好印象。",
                "answer": my_answer
            },
            {
                "text": "您喜欢参加集体活动。",
                "answer": my_answer
            },
            {
                "text": "您喜欢使您对结局做出自我诠释的书籍和电影。",
                "answer": my_answer
            },
            {
                "text": "您的幸福更多地来自帮助别人完成事情，而不是您自己的成就。",
                "answer": my_answer
            },
            {
                "text": "您对很多事情感兴趣，您发现很难选择下一步尝试什么。",
                "answer": my_answer
            },
            {
                "text": "您很容易担心事情会变得更糟。",
                "answer": my_answer
            },
            {
                "text": "您避免在小组环境中扮演领导角色。",
                "answer": my_answer
            },
            {
                "text": "您绝对不是艺术类型的人。",
                "answer": my_answer
            },
            {
                "text": "您认为，如果人们更多地依靠理性而更少地依靠自己的感受，世界将会变得更美好。",
                "answer": my_answer
            },
            {
                "text": "在让自己放松之前，您更喜欢做家务。",
                "answer": my_answer
            },
            {
                "text": "您喜欢观看人们的争论。",
                "answer": my_answer
            },
            {
                "text": "您倾向于避免把注意力吸引到自己身上。",
                "answer": my_answer
            },
            {
                "text": "您的情绪会很快改变。",
                "answer": my_answer
            },
            {
                "text": "您对效率不如您的人会失去耐心。",
                "answer": my_answer
            },
            {
                "text": "您经常在最后截止日期前做事情。",
                "answer": my_answer
            },
            {
                "text": "您一直着迷于死后会发生什么的问题(如果真的会发生的话)。",
                "answer": my_answer
            },
            {
                "text": "您通常更喜欢和别人在一起，而不是独自一人。",
                "answer": my_answer
            },
            {
                "text": "当讨论变得高度理论化时，您会觉得变得无聊或失去兴趣。",
                "answer": my_answer
            },
            {
                "text": "您发现很容易同情一个与您的经历非常不同的人。",
                "answer": my_answer
            },
            {
                "text": "您通常会尽可能长时间地推迟最终决定。",
                "answer": my_answer
            },
            {
                "text": "您很少狐疑您所做的选择。",
                "answer": my_answer
            },
            {
                "text": "经过漫长而疲惫的一周，一场热闹的社交活动正是您所需要的。",
                "answer": my_answer
            },
            {
                "text": "您喜欢去艺术博物馆。",
                "answer": my_answer
            },
            {
                "text": "您经常很难理解别人的感受。",
                "answer": my_answer
            },
            {
                "text": "您喜欢有一份每天的待办事项清单。",
                "answer": my_answer
            },
            {
                "text": "您很少感到没有安全感。",
                "answer": my_answer
            },
            {
                "text": "您会避免打电话。",
                "answer": my_answer
            },
            {
                "text": "您经常花很多时间试图理解与您自己截然不同的观点。",
                "answer": my_answer
            },
            {
                "text": "在您的社交圈里，您经常是联系您的朋友并发起活动的人。",
                "answer": my_answer
            },
            {
                "text": "如果您的计划被打断，您的首要任务是尽快回到正轨。",
                "answer": my_answer
            },
            {
                "text": "您仍然被您很久以前犯的错误所困扰。",
                "answer": my_answer
            },
            {
                "text": "您很少考虑人类存在的原因或生命的意义。",
                "answer": my_answer
            },
            {
                "text": "您的情绪控制您胜过您控制他们。",
                "answer": my_answer
            },
            {
                "text": "您非常小心地不让别人难堪，即使这完全是他们的错。",
                "answer": my_answer
            },
            {
                "text": "您的个人工作风格比有组织和一致的努力更接近自发的能量爆发。",
                "answer": my_answer
            },
            {
                "text": "当有人对您评价很高时，您会想知道他们需要多长时间就会对您感到失望。",
                "answer": my_answer
            },
            {
                "text": "您会喜欢一份大部分时间都需要您独自操作的工作。",
                "answer": my_answer
            },
            {
                "text": "您认为思考抽象的哲学问题是浪费时间。",
                "answer": my_answer
            },
            {
                "text": "与安静、私密的地方相比，您更喜欢繁忙、熙熙攘攘的地方。",
                "answer": my_answer
            },
            {
                "text": "您乍一看就知道某人的感受。",
                "answer": my_answer
            },
            {
                "text": "您经常感到不知所措。",
                "answer": my_answer
            },
            {
                "text": "您有条不紊地完成事情，而不跳过任何步骤。",
                "answer": my_answer
            },
            {
                "text": "您对被标记为有争议的事情很感兴趣。",
                "answer": my_answer
            },
            {
                "text": "如果您认为别人更需要它，您会把一个好机会让出去。",
                "answer": my_answer
            },
            {
                "text": "您会在最后期限上挣扎。",
                "answer": my_answer
            },
            {
                "text": "您对事情会向对自己有利的方向发展有信心。",
                "answer": my_answer
            }
        ],
        "teamInviteKey": ""
    }
    # fake ua
    ua = UserAgent()
    result_headers = {
        "Authority": "www.16personalities.com",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.16personalities.com",
        "Referer": "https://www.16personalities.com/ch/%E4%BA%BA%E6%A0%BC%E6%B5%8B%E8%AF%95",
        "User-Agent": ua.chrome,
    }
    result_response = requests.post(result_url, headers=result_headers, json=result_json)
    # 获取cookies全部
    result_cookies = result_response.headers.get("set-cookie")
    # 截取cookies
    result__results = result_cookies[result_cookies.find("testResults="):]
    result_test_results = result__results[:result__results.find("; expires")]

    session_headers = {
        "Accept": "application/json, text/plain, */*",
        "Cookie": result_test_results,
        "user-agent": ua.chrome
    }

    # 拿到cookies，再请求下一个接口，get
    session_url = "https://www.16personalities.com/api/session"
    session_response = requests.get(session_url, headers=session_headers)
    # 转为字典
    response_dict = json.loads(session_response.text)
    print(f"response_dict:{response_dict}")
    # 人格类型
    personality = ''
    try:
        # 获取性格类型：ENFJ
        personality = response_dict.get('user').get("personality")
        # 获取详细内容
        get_personality_content(personality)
    except Exception as e:
        print(f'获取结果异常：{e}')

    # 拿到结果页面后，使用selenium请求结果页面，拿到结果
    # 可以自己手动复制保存到自己的库中
    return personality


def get_personality_content(personality="infp"):
    """
    获取人格类型的详细内容
    :param personality: 性格类型
    :return:
    """
    name = "人格"
    name_encoded = urllib.parse.quote(name)
    # 结果页面：
    personality_url = f"https://www.16personalities.com/ch/{personality}-{name_encoded}"
    # 人格结果页面：https://www.16personalities.com/ch/ENFJ-%E4%BA%BA%E6%A0%BC
    print(f"人格结果页面：{personality_url}")

    content_response = requests.get(personality_url)
    html_per = etree.HTML(content_response.text)

    # 两者相同
    # title_ele = html_per.xpath('//*[@id="main-app"]/main/div[1]/div/article/blockquote/p')[0]
    title_ele = html_per.xpath('///blockquote/p')[0]

    title = title_ele.text
    print(f"title:{title}")


if __name__ == '__main__':
    """
    可直接运行
    """
    user_type = get_16personalities_type()
    print(f"user_type:{user_type}")
