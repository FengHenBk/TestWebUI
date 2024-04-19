from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
定义基本工具类，setup(),teardown()方法
"""


class Base(object):
    # def __init__(self):
    #     self.webdriver = None

    def setup_class(self):
        # 初始化浏览器
        self.webdriver = webdriver.Chrome(service=Service(r'D:\tools\webdriver\chromedriver.exe'))
        self.webdriver.implicitly_wait(3)
        self.webdriver.maximize_window()

    def teardown_class(self):
        # 关闭浏览器
        self.webdriver.quit()


