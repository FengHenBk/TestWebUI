import pytest
from selenium.webdriver.common.by import By

from Base.base import Base


class TestCeshiren(Base):

    # def setup_class(self):
    #     # 初始化浏览器
    #     self.webdriver = webdriver.Chrome(service=Service(r'D:\tools\webdriver\chromedriver.exe'))
    #
    # def teardown_class(self):
    #     # 关闭浏览器
    #     self.webdriver.quit()

    @pytest.mark.parametrize("search_value", ["Selenium", "Appium", "面试"])
    def test_search_selenium(self,search_value):
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
        # self.webdriver.find_element(By.ID, 'ember15').send_keys("Selenium")
        self.webdriver.find_element(By.ID, 'ember15').send_keys(search_value)
        # 3.点击搜索按钮
        self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
        # 断言
        text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
        assert search_value in text

    # def test_search_appium(self):
    #     """
    #     测试 https://ceshiren.com/ 的搜索功能
    #
    #     1.打开 https://ceshiren.com/
    #     2.输入框输入
    #     3.点击搜索
    #     :return:
    #     """
    #     # 1.进入 https://ceshiren.com/search页面
    #     self.webdriver.get('https://ceshiren.com/search')
    #     self.webdriver.maximize_window()
    #     self.webdriver.implicitly_wait(3)
    #     # 2.输入框输入
    #     self.webdriver.find_element(By.ID, 'ember15').send_keys("Appium")
    #     # 3.点击搜索按钮
    #     self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
    #     # 断言
    #     text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
    #     assert "Appium" in text
    #
    # def test_search_mianshi(self):
    #     """
    #     测试 https://ceshiren.com/ 的搜索功能
    #
    #     1.打开 https://ceshiren.com/
    #     2.输入框输入
    #     3.点击搜索
    #     :return:
    #     """
    #     # 1.进入 https://ceshiren.com/search页面
    #     self.webdriver.get('https://ceshiren.com/search')
    #     self.webdriver.maximize_window()
    #     self.webdriver.implicitly_wait(3)
    #     # 2.输入框输入
    #     self.webdriver.find_element(By.ID, 'ember15').send_keys("面试")
    #     # 3.点击搜索按钮
    #     self.webdriver.find_element(By.XPATH, '//*[@id="ember13"]/div[2]/div[1]/button/span').click()
    #     # 断言
    #     text = self.webdriver.find_element(By.CSS_SELECTOR, '.topic-title').text
    #     assert "面试" in text
