import time
from selenium import webdriver


class HLJU_AutoPJ:
    def __init__(self):
        username = input("请输入学号：")
        password = input("请输入密码：")
        self.driver = webdriver.Chrome()
        self.driver.get('http://jxpj.hlju.edu.cn/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id("dlan").click()
        self.driver.find_element_by_link_text("学习体验调查与评教").click()
        self.xspj_start()
        time.sleep(1)
        self.xxtydc_start()

    def xspj_start(self):
        pingkes = self.driver.find_elements_by_xpath(
            "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a")
        length = len(pingkes)
        for i in range(length):
            if '已完成' == pingkes[i].accessible_name:
                continue
            pingkes[i].click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[2]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[4]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[6]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[8]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[10]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[12]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[14]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[16]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[18]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[20]/textarea").send_keys('非常满意')
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[22]/textarea").send_keys('不需要改进')
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[23]/input[1]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[5]/div/input[1]").click()
            pingkes = self.driver.find_elements_by_xpath(
                "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a")

    def xxtydc_start(self):
        pingkes = self.driver.find_elements_by_xpath(
            "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[7]/a")
        length = len(pingkes)
        for i in range(length):
            if '已完成' == pingkes[i].accessible_name:
                continue
            pingkes[i].click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[2]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[4]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[6]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[8]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[10]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[12]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[14]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[16]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[18]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[20]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[22]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[24]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[26]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[28]/div[1]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[30]/div[2]/div/ins").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[32]/textarea").send_keys('非常满意')
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[34]/textarea").send_keys('不需要改进')
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/form/div/div[35]/input[1]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[5]/div/input[1]").click()
            pingkes = self.driver.find_elements_by_xpath(
                "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[7]/a")


def main():
    HLJU_AutoPJ()


if __name__ == '__main__':
    main()
