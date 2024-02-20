# 点击微信公众号XY坐标列表
wx_click_xy = [
    {
        "name": "鸟哥笔记",
        "x_axis": 1008,
        "y_axis": 658
    }, {
        "name": "澎湃新闻",
        "x_axis": 1075,
        "y_axis": 658
    }, {
        "name": "人民日报",
        "x_axis": 1145,
        "y_axis": 658
    }, {
        "name": "央视新闻",
        "x_axis": 940,
        "y_axis": 767
    },
]

"""准备流程
1：登录PC微信(微信版本是：3.9.8.25，需要关闭自动更新)
2：点击通讯录->公众号
3：点击任意一个公众号，将公众号详情界面，移动到左上角。
   调整大小：宽度至最宽(screen_x=550)，高度至屏幕高度(screen_y=1080)
4：运行click_xy.py文件，移动鼠标到日期文本左上角，观察x坐标
5：点击任意文章，调整文章详情宽度为最窄，移动到详情页面的右侧，居顶对齐

"""

# 公众号详情的整个截图，宽度为：screen_x，高度为：screen_y
# 手动调整大小
screen_x = 550
screen_y = 1080

# 文章列表，日期文本(今天/昨天/1月19日等等)的左上角x坐标返回
# 通过click_xy.py获取日期文本的左上角x坐标，并放大范围
# 例如：x=105,范围就是103-108区间
min_coordinate = 100
max_coordinate = 110

# 文章详情，右上角的三个点
# 手动调整大小， 通过click_xy.py获取
san_x = 870
san_y = 20
# 手动调整大小， 通过click_xy.py获取
copy_x = 780
copy_y = 170

# 截图保存的目录
screen_dir = "D:/python_project/weixin_click/picture/"
