import datetime
import time

import pyperclip
from paddleocr import PaddleOCR

from click_utils import is_date, mouse_click, get_screen_by_autogui, sleep_random
from constant import wx_click_xy, screen_y, screen_x, min_coordinate, max_coordinate, copy_x, copy_y, \
    san_x, san_y
from mysql_db import Article, db

# https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md
# nvidia-smi
# nvcc -V
# python -m pip install paddlepaddle-gpu==2.6.0.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
paddle_ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True, ocr_version="PP-OCRv4")


def ocr_image(img_path):
    """
    OCR识别文章列表图片
    :param img_path: 截图图片
    :return: 标题列表
    """
    result = paddle_ocr.ocr(img_path, cls=True)

    # 可能是文章标题，可能是阅读数
    may_article = False
    # 今天的文章列表和对应坐标
    titles_list = []
    for idx in range(len(result)):
        # 文章的标题
        title_all = ''
        # 原始数据
        res = result[idx]
        for data in res:  # 每一行的数据
            # data:[[[132.0, 97.0], [147.0, 97.0], [147.0, 114.0], [132.0, 114.0]], ('2', 0.5771653652191162)]
            # data，依次是：左上，右上，右下，坐下，文本，置信度
            # 左上角x坐标
            x_coordinate = data[0][0][0]
            # 右上角x坐标
            x_top_right = data[0][1][0]
            # 右上角y坐标
            y_top_right = data[0][1][1]
            # ocr内容
            ocr_text = data[1][0]
            # 先通过坐标过滤，在这个范围的有可能是文章标题
            print(f"文本左上角坐标为：{x_coordinate}，文本内容：{ocr_text}")
            if min_coordinate <= x_coordinate <= max_coordinate:
                # 说明可能是文章的日期文本，再通过文本过滤
                # 找到文本是“今天”的坐标
                if ocr_text == '今天':
                    print("-------")
                    may_article = True
                elif (ocr_text in ['昨天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六',
                                   '星期日']) or is_date(ocr_text):
                    may_article = False
                    print("非今天的日期文本，跳过处理")
                    break
                else:
                    if may_article:
                        # todo OCR识别错误，导致数据异常
                        # todo 数据问题，可以结合数据库处理
                        if ocr_text.startswith("阅读"):
                            print("-------------------结束")
                            # 获取当前文本两个x坐标的中间值
                            point_x = (x_top_right - x_coordinate) / 2 + x_coordinate
                            title_dict = {"title": title_all, "point_x": point_x, "point_y": y_top_right}
                            titles_list.append(title_dict)
                            # 清空文本
                            title_all = ""
                        else:
                            # 点击获取文章列表
                            print("-------")
                            title_all = title_all + ocr_text
    print(f"OCR结果列表：{titles_list}")
    return titles_list


def handle_data(title_list, name):
    """
    通过标题查询数据库，存在跳过；不存在，单击获取文章链接，保存数据库
    [{'title': '跑步机里藏666万黄金！落马厅官出镜忏悔', 'point_x': 93.0, 'point_y': 627.0}]
    :param title_list: 标题列表
    :param name: 公众号名称
    :return:
    """
    insert_list = []
    for item in title_list:
        title_str = item.get("title")
        click_x = int(item.get("point_x"))
        click_y = int(item.get("point_y"))
        # 查询
        try:
            # 存在
            article = Article.get(Article.title == title_str)
            print(f"存在文章，id为：{article.id}；标题为：{title_str}")
            continue
        except Article.DoesNotExist as e:
            print(f"不存在文章，标题为：{title_str}")
            mouse_click(click_x, click_y)
            # 点击右上角三个点
            mouse_click(san_x, san_y)
            # 点击复制链接按钮
            mouse_click(copy_x, copy_y)
            # 获取复制的链接，粘贴板
            title_url = pyperclip.paste()
            # 不存在，新增数据，单个循环插入
            # article = Article(title=title_str, url=title_url, name=name)
            # article.save()
            # print("新增完成")
            insert_list.append({'title': title_str, 'url': title_url, 'name': name})

    print(f"批量入库的数据：{insert_list}")
    if len(insert_list) > 0:
        if db.is_closed():
            print("数据库重新连接")
            db.connect()
        # 批量插入
        with db.atomic():
            Article.insert_many(insert_list).execute()


def main():
    for item in wx_click_xy:
        start_time = time.time()
        sleep_random(1)
        name = item.get("name")
        print(f"1：开始点击的公众号名称：{name}")
        x_axis = item.get("x_axis")
        y_axis = item.get("y_axis")

        sleep_random(1)
        print("2：点击微信公众号的xy坐标，显示文章列表")
        mouse_click(x_axis, y_axis)

        print("3：截图：公众号文章列表")
        save_pic = get_screen_by_autogui(screen_x, screen_y)

        print("4：处理ocr识别的文字内容")
        title_list = ocr_image(save_pic)

        sleep_random(2)
        print("5：标题获取完成，开始入库")
        handle_data(title_list, name)

        print(f"公众号名称：{name}，处理完成。")
        print('共耗时约 {:.2f} 秒'.format(time.time() - start_time))
        print("=" * 100)


if __name__ == '__main__':
    while 1:
        print(f"循环体执行的时间：{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}")
        main()
        print("大循环间隔一分钟执行")
        sleep_random(1 * 60)
