from time import sleep

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from Base.base import Base


class TestLiteMall(Base):
    # def click_excepion(self, by, element, max_attempts=50):
    #     def _inner(webdriver):
    #         auto_attempts = 0
    #         while auto_attempts < max_attempts:
    #             auto_attempts += 1
    #             try:
    #                 ActionChains(webdriver).move_to_element(self.webdriver.find_element(by, element)).click(
    #                     self.webdriver.find_element(by, element).click())
    #                 # self.webdriver.find_element(by, element).click()
    #                 return True
    #             except Exception as e:
    #                 print("点击元素时报错")
    #             raise Exception("超出点击最大次数")
    #
    #     return _inner

    @pytest.fixture
    def login(self):
        self.webdriver.get('https://litemall.hogwarts.ceshiren.com/#/login')
        self.webdriver.find_element(By.NAME, 'username').clear()
        self.webdriver.find_element(By.NAME, 'username').send_keys("manage")
        self.webdriver.find_element(By.NAME, 'password').clear()
        self.webdriver.find_element(By.NAME, 'password').send_keys("manage123")
        self.webdriver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()

    def logout(self):
        # WebDriverWait(self.webdriver, 10, 10).until(self.click_excepion(By.CLASS_NAME, 'user-avatar'))
        # self.webdriver.implicitly_wait(10)
        sleep(10)
        ActionChains(self.webdriver).move_to_element(
            self.webdriver.find_element(By.CLASS_NAME, 'user-avatar')).click(
            self.webdriver.find_element(By.CLASS_NAME, 'user-avatar')).perform()
        self.webdriver.find_element(By.XPATH, '//*[text()="退出"]').click()

    def test_add_products(self, login):
        """
        添加商品类目
        前提条件：
        1. 登录并进入用户管理后台
        2. 登录账号有商场管理的权限

        用例步骤：
        1. 点击增加
        2. 输入类目名称
        3. 点击确定

        预期结果：
        1. 跳转商品类目列表
        2. 新增在最后一行，新增成功
        :return:
        """
        # 点击商品管理
        self.webdriver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        # 点击商品类目
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li').click()

        # 点击添加
        self.webdriver.find_element(By.CLASS_NAME, "el-icon-edit").click()
        # 输入品牌商名称
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div['
                                    '1]/input').send_keys(
            "测试")
        # 输入介绍
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "测试")
        # 输入底价
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input').send_keys(
            "200")
        # 点击确定
        # ele = self.webdriver.find_element(By.XPATH, "//*[text()='确定']")
        ActionChains(self.webdriver).move_to_element(self.webdriver.find_element(By.XPATH, "//*[text()='确定']")).click(
            self.webdriver.find_element(By.XPATH, "//*[text()='确定']")).perform()
        # self.webdriver.save_screenshot("test.png")

        # 断言,
        result = self.webdriver.find_element(By.XPATH, "//*[text()='测试']")
        # 删除脏数据
        self.webdriver.find_element(By.XPATH, "//*[text()='测试']/../..//*[text()='删除']").click()
        assert result != []
        self.logout()

    def test_delete_products(self, login):
        """
        添加商品类目
        前提条件：
        1. 进入用户管理后台
        2. 商品列表里面有已存在的商品（新增）

        用例步骤：
        1. 点击删除按钮

        预期结果：
        1. 是否有删除成功提示
        2. 被删除商品不在商品类目列表展示
        :return:
        """
        sleep(4)
        # 点击商品管理
        self.webdriver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        # 点击商品类目
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li').click()

        # 点击添加
        self.webdriver.find_element(By.CLASS_NAME, "el-icon-edit").click()
        # 输入品牌商名称
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div['
                                    '1]/input').send_keys(
            "测试")
        # 输入介绍
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "测试")
        # 输入底价
        self.webdriver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input').send_keys(
            "200")
        # 点击确定
        # ele = self.webdriver.find_element(By.XPATH, "//*[text()='确定']")
        ActionChains(self.webdriver).move_to_element(self.webdriver.find_element(By.XPATH, "//*[text()='确定']")).click(
            self.webdriver.find_element(By.XPATH, "//*[text()='确定']")).perform()
        self.webdriver.find_element(By.XPATH, "//*[text()='测试']/../..//*[text()='删除']").click()
        sleep(2)
        result = self.webdriver.find_elements(By.XPATH, "//*[text()='测试']")
        assert result == []

    # def test_logout(self, login):
    #     sleep(3)
    #     ActionChains(self.webdriver).move_to_element(
    #         self.webdriver.find_element(By.CLASS_NAME, 'user-avatar')).click(
    #         self.webdriver.find_element(By.CLASS_NAME, 'user-avatar')).perform()
    #     sleep(4)
    #     self.webdriver.find_element(By.XPATH, '//*[text()="退出"]').click()
