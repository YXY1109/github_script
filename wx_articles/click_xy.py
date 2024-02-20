import time
import pyautogui

width, height = pyautogui.size()
print("屏幕分辨率：", width, height)
# 获取鼠标实时位置
for _ in range(30):
    x, y = pyautogui.position()
    print("当前鼠标点击位置：", x, y)
    time.sleep(1)
