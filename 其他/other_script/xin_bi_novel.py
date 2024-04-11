import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

"""
参考的文章：
https://github.com/Jack-Cherish/python-spider/tree/master/2020

新笔趣阁的小说爬虫

"""


def get_content(target='http://www.xinbqg.cn/63_63011/11422569.html'):
    """
    小说爬虫页面：
    http://www.xinbqg.cn/63_63011/11422569.html
    :return:
    """
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)
    return content


def main():
    """
    小说：明末大军阀
    :return:
    """
    server = 'http://www.xinbqg.cn'
    book_name = '明末大军阀.txt'
    target = f"{server}/63_63011/"
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapters = bs.find_all('div', class_="section-box")
    chapters = chapters[1].find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')


if __name__ == '__main__':
    """
    参考文章：
    https://mp.weixin.qq.com/s/5e2_r0QXUISVp9GdDsqbzg
  
    """
    main()
