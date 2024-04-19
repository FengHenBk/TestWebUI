from time import sleep

from selenium.webdriver.common.by import By

from Base.base import Base


class TestSwitch(Base):

    def test_switch_window(self):
        # 打开百度页面
        self.webdriver.get("https://www.baidu.com/")
        # 点击登录
        self.webdriver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
        # 点击立即注册
        self.webdriver.find_element(By.ID, 'TANGRAM__PSP_11__regLink').click()
        # 切换handle
        self.webdriver.switch_to.window(self.webdriver.window_handles[1])

        # 注册页面，输入用户名
        self.webdriver.find_element(By.NAME, "userName").send_keys("baidu")
        # 注册页面，输入手机号
        self.webdriver.find_element(By.NAME, "phone").send_keys("18092240647")
        # # 注册页面，输入密码
        # self.webdriver.find_element(By.NAME, "password").send_keys("baidu")
        # # 注册页面，点击获取验证码
        # self.webdriver.find_element(By.ID, "TANGRAM__PSP_4__verifyCodeSend").click()
        # # 注册页面，输入验证码
        # self.webdriver.find_element(By.NAME, "verifyCode").send_keys("baidu")
        sleep(3)
        # 切换handle
        self.webdriver.switch_to.window(self.webdriver.window_handles[0])

        # 百度首页，输入用户名
        self.webdriver.find_element(By.NAME, "userName").send_keys("baidu")
        # 百度首页，输入密码
        self.webdriver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("18092240647")

#
