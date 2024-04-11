import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By

from config import global_config


def xie_cheng():
    open_url = "https://hotels.ctrip.com/hotels/list?countryId=1&city=-1&checkin=2024/02/21&checkout=2024/02/22&optionId=24&optionType=Province&directSearch=0&display=%E5%B9%BF%E8%A5%BF%2C%20%E4%B8%AD%E5%9B%BD&crn=1&adult=1&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1&"
    print(f"开始:{open_url}")

    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # 针对新版ChromeDriver可能需要此项
    options.add_argument(f"user-agent={ua.random}")

    driver = webdriver.Chrome(options=options)
    driver.get(open_url)
    time.sleep(3)

    print("开始写入账号密码")
    phone = global_config.get("xie_cheng", "phone")
    password = global_config.get("xie_cheng", "password")
    phone_pass_path = '//*[@id="bbz_accounts_pc_lg_box"]/div/div/div[1]/div[1]/form/dl[{}]/dd/input'
    driver.find_element(By.XPATH, phone_pass_path.format(1)).send_keys(phone)
    time.sleep(1)
    driver.find_element(By.XPATH, phone_pass_path.format(2)).send_keys(password)
    time.sleep(1)

    print("点击同意阅读")
    # driver.find_element(By.XPATH, '//*[@id="checkboxAgreementInput"]').click()
    driver.find_element(By.XPATH, '//*[@id="bbz_accounts_pc_lg_box"]/div/div/div[1]/div[4]/div/div[1]').click()
    time.sleep(1)

    print("点击登录")
    driver.find_element(By.XPATH, '//*[@id="bbz_accounts_pc_lg_box"]/div/div/div[1]/div[1]/form/dl[3]/dd/input').click()
    time.sleep(1)

    time.sleep(300)


if __name__ == '__main__':
    xie_cheng()
