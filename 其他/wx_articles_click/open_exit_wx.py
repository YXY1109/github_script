import os
import subprocess
import time

import pyautogui


def get_screen():
    screen_width, screen_height = pyautogui.size()
    print(screen_width, screen_height)
    return screen_width, screen_height


def open_wx(exe_path=r"F:\software_install\WeChat\WeChat.exe"):
    """
    打开微信，自动调整微信公众号内容详情
    如果遇到问题可以将微信关闭，再打开
    :param exe_path:
    :return:
    """
    # 打开微信
    subprocess.Popen(exe_path)

    time.sleep(2)
    # 点击登录（首次需要扫码）
    width, height = get_screen()
    x = width / 2
    y = height / 2 + 70
    pyautogui.click(x, y)
    # 需要等待手机点击同意登录

    # 点击通讯录 530.350
    time.sleep(6)
    pyautogui.click(530, 350)

    # 点击公众号 680.480
    time.sleep(1)
    pyautogui.click(680, 480)

    # 点击第一个公众号
    time.sleep(1)
    pyautogui.click(920, 310)

    # 双击公众号详情页面，使其调整到左侧高度拉到和屏幕高一致
    time.sleep(1)
    y = 210
    pyautogui.doubleClick(x, y)

    # 关闭微信
    time.sleep(1)
    os.system('C:\\Windows\\System32\\taskkill /F /IM WeChat.exe')


if __name__ == '__main__':
    open_wx()
    # get_screen()
