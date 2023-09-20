"""
妖神记的动漫爬虫
https://github.com/Jack-Cherish/python-spider/tree/master/2020
官网：https://www.idmzj.com/info/yaoshenji.html
公众号：https://mp.weixin.qq.com/s/wyS-OP04K3Vs9arSelRlyA

"""
import requests
from bs4 import BeautifulSoup


def get_comic_list():
    """
    可以直接使用过接口获取图片

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


def get_comic_bs():
    """
    不可用
    :return:
    """
    target_url = "https://www.dmzj.com/info/yaoshenji.html"
    r = requests.get(url=target_url)
    bs = BeautifulSoup(r.text, 'lxml')
    list_con_li = bs.find('ul', class_="list_con_li")
    comic_list = list_con_li.find_all('a')
    chapter_names = []
    chapter_urls = []
    for comic in comic_list:
        href = comic.get('href')
        name = comic.text
        chapter_names.insert(0, name)
        chapter_urls.insert(0, href)

    print(chapter_names)
    print(chapter_urls)


if __name__ == '__main__':
    """
    妖神记的动漫爬虫
    """
    # get_comic_list()
    get_comic_bs()
