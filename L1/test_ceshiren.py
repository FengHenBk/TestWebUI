import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestCeshiren:

    def setup_class(self):
        # 初始化浏览器
        self.webdriver = webdriver.Chrome(service=Service(r'D:\tools\webdriver\chromedriver.exe'))

    def teardown_class(self):
        # 关闭浏览器
        self.webdriver.quit()


    def test_search_selenium(self):
        """
        测试 https://ceshiren.com/ 的搜索功能

        1.打开 https://ceshiren.com/
        2.输入框输入
        3.点击搜索
        :return:
        """
        # 1.进入 https://ceshiren.com/search页面
        self.webdriver.get('https://ceshiren.com/search')
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(3)
        # 2.输入框输入
        self.webdriver.find_element(By.ID, 'ember15').send_keys("Selenium")
        # 3.点击搜索按钮
        self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
        # 断言
        text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
        assert "Selenium" in text

    def test_search_appium(self):
        """
        测试 https://ceshiren.com/ 的搜索功能

        1.打开 https://ceshiren.com/
        2.输入框输入
        3.点击搜索
        :return:
        """
        # 1.进入 https://ceshiren.com/search页面
        self.webdriver.get('https://ceshiren.com/search')
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(3)
        # 2.输入框输入
        self.webdriver.find_element(By.ID, 'ember15').send_keys("Appium")
        # 3.点击搜索按钮
        self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
        # 断言
        text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
        assert "Appium" in text

    def test_search_mianshi(self):
        """
        测试 https://ceshiren.com/ 的搜索功能

        1.打开 https://ceshiren.com/
        2.输入框输入
        3.点击搜索
        :return:
        """
        # 1.进入 https://ceshiren.com/search页面
        self.webdriver.get('https://ceshiren.com/search')
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(3)
        # 2.输入框输入
        self.webdriver.find_element(By.ID, 'ember15').send_keys("面试")
        # 3.点击搜索按钮
        self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
        # 断言
        text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
        assert "面试" in text
