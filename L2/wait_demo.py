import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 初始化浏览器
webdriver = webdriver.Chrome(service=Service(r'D:\tools\webdriver\chromedriver.exe'))

# 1.进入 https://ceshiren.com/search页面
webdriver.get('https://ceshiren.com/search')
webdriver.maximize_window()
WebDriverWait(webdriver, 10).until()
# 2.输入框输入
# self.webdriver.find_element(By.ID, 'ember15').send_keys("Selenium")
webdriver.find_element(By.ID, 'ember15').send_keys()
# 3.点击搜索按钮
webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
# 断言
text = webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text

webdriver.quit()
driver = "AAA"



if __name__ == '__main__':

    def faker_condition(driver):
        print("当前的时间：", time.time())


    WebDriverWait(driver, 10).until(faker_condition, "霍格沃兹测试开发")


