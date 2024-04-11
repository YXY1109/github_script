import hashlib
import time


def md5_str(str_msg):
    md5 = hashlib.md5()
    md5.update(str_msg.encode('utf-8'))
    return md5.hexdigest()


def jimu_token_time():
    """
    计算极目新闻的token
    :return:
    """
    salt = "hbrb-app-amc"
    h5_str = "h5Client-id"
    # 毫秒时间戳
    time_s = int(time.time()) * 1000
    print(time_s)

    str_1 = salt + "$" + str(time_s)
    str_1 = md5_str(str_1)
    str_1 = h5_str + "$" + str_1 + "$" + str(time_s)
    str_1 = md5_str(str_1)
    print(str_1)
    return time_s, str_1


if __name__ == '__main__':
    """
    获取了极目新闻的加密方式，可以直接使用接口处理
    """
    jimu_token_time()
