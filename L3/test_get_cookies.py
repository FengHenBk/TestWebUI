from time import sleep
import yaml

from Base.base import Base


class TestGetCookies(Base):
    # 获取cookies
    def test_get_cookies(self):
        self.webdriver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(10)
        cookies = self.webdriver.get_cookies()
        with open("cookies.yaml", "w") as file:
            yaml.safe_dump(cookies, file)
            file.close()

    def test_add_cookie(self):
        # 1. 访问企业微信主页面
        self.webdriver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("cookies.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.webdriver.add_cookie(c)
        sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.webdriver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
