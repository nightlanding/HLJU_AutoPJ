import time
from selenium import webdriver
import xspj
import xxtydc


def main():
    username = input("请输入学号：")
    password = input("请输入密码：")
    driver = webdriver.Chrome()
    driver.get('http://jxpj.hlju.edu.cn/')
    driver.implicitly_wait(10)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_id("dlan").click()
    driver.find_element_by_link_text("学习体验调查与评教").click()
    xspj.start(driver)
    time.sleep(1)
    xxtydc.start(driver)

if __name__ == '__main__':
    main()