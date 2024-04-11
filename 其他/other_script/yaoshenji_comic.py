"""
妖神记的动漫爬虫
https://github.com/Jack-Cherish/python-spider/tree/master/2020
官网：https://www.idmzj.com/info/yaoshenji.html
公众号：https://mp.weixin.qq.com/s/wyS-OP04K3Vs9arSelRlyA

"""
import requests


def get_comic_list():
    """
    可以直接使用接口获取图片

    :return:
    """
    server_url = "https://www.idmzj.com/api/v1/comic1/comic/detail?channel=pc&app_name=dmzj&" \
                 "version=1.0.0&timestamp=1695002334241&uid&comic_py=yaoshenji"
    response = requests.get(server_url)
    response_dict = response.json()
    # print(response_dict)
    # 章节列表
    chapter_list = response_dict.get("data").get("comicInfo").get("chapterList")[0].get("data")
    print(chapter_list[:2])

    for chapter in chapter_list[:20]:
        chapter_id = chapter.get("chapter_id")
        detail_url = f"https://www.idmzj.com/api/v1/comic1/chapter/detail?channel=pc&app_name=dmzj&version=1.0.0&" \
                     f"timestamp=1695002334241&uid&comic_id=20926&chapter_id={chapter_id}"
        response = requests.get(detail_url)
        response_dict = response.json()

        page_url = response_dict.get("data").get("chapterInfo").get("page_url")
        print(page_url)


if __name__ == '__main__':
    """
    妖神记的动漫爬虫
    """
    get_comic_list()
