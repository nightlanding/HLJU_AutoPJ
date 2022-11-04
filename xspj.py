def start(driver):
    pingkes = driver.find_elements_by_xpath(
        "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a")
    length = len(pingkes)
    for i in range(length):
        if '已完成' == pingkes[i].accessible_name:
            continue
        pingkes[i].click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[2]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[4]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[6]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[8]/div[2]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[10]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[12]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[14]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[16]/div[2]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[18]/div[1]/div/ins").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[20]/textarea").send_keys('非常满意')
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[22]/textarea").send_keys('不需要改进')
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/form/div/div[23]/input[1]").click()
        driver.find_element_by_xpath("/html/body/div[5]/div/input[1]").click()
        pingkes = driver.find_elements_by_xpath(
            "/html/body/div[4]/div[2]/table/tbody/tr[*]/td[8]/a")
