import datetime
import random
import re
import time
from ctypes import windll

import numpy as np
import pyautogui
import win32api
import win32con
from PIL import Image

from constant import screen_dir


def sleep_random(time_sec=2):
    """
    随机延迟时间
    :param time_sec:
    :return:
    """
    delay = random.uniform(time_sec, time_sec + 1)
    time.sleep(delay)


def mouse_click(x, y, time_sec=2):
    """
    鼠标移动到xy，点击
    :param x: x坐标
    :param y: y坐标
    :param time_sec: 延迟时间
    :return:
    """
    # 鼠标移动到制定位置
    windll.user32.SetCursorPos(x, y)
    # 鼠标点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
    sleep_random(time_sec)


def get_screen_by_autogui(width, height):
    """
    保存公众号的文章列表的截图
    从左上角(0,0)坐标开始
    :param width: 截图宽
    :param height: 截图高
    :return: 截图图片的全路径
    """
    img = pyautogui.screenshot(region=[0, 0, width, height])  # 截图
    # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # 转换色值
    img = Image.fromarray(np.uint8(img))
    file_name = f"{screen_dir}{datetime.datetime.now().strftime('%Y%m%d%H%M%S_%f')}_wx.jpg"
    # file_name = f"D:/python_project/dingding_send/picture/test_wx.jpg"
    img.save(file_name)  # 保存为文件路径+文件名
    return file_name


def is_date(text):
    """
    判断文本是否是年月日或者月日的样式
    :param text:
    :return:
    """
    # 定义月日格式的正则表达式
    month_day = r'^\d{1,2}月\d{1,2}日'

    # 定义年月日格式的正则表达式
    year_month_day = r'^\d{4}年\d{1,2}月\d{1,2}日'

    if re.match(month_day, text) or re.match(year_month_day, text):
        return True
    else:
        return False
