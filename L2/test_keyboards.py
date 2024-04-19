from time import sleep

from selenium.webdriver.common import keys

from Base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains


class TestKeyboards(Base):
    def test_keyboards(self):
        """
        1.打开 https://ceshiren.com/ 网站
        2.点击搜索按钮
        3.输入测试内容后回车
        :return:
        """
        self.webdriver.get("https://ceshiren.com/")
        self.webdriver.find_element(By.ID, "search-button").click()
        # 3.输入测试内容后回车
        # self.webdriver.find_element(By.ID, "search-term").send_keys("appium")
        # 3.输入内容时，按住 shift 键位，以保证输入内容为大写字母
        ele = self.webdriver.find_element(By.ID, "search-term")
        ActionChains(self.webdriver).key_down(keys.Keys.SHIFT).send_keys("selenium").perform()
        ele.send_keys(keys.Keys.ENTER)
        # ActionChains(self.webdriver).key_down(keys.Keys.ENTER).perform()
        sleep(10)

    # 剪切+复制
    def test_copy_and_paste(self):
        self.webdriver.get("https://ceshiren.com")
        self.webdriver.find_element(By.ID, "search-button").click()
        ele = self.webdriver.find_element(By.ID, "search-term")
        (ActionChains(self.webdriver)
         .key_down(keys.Keys.SHIFT)
         .send_keys("selenium")
         .send_keys(keys.Keys.ARROW_LEFT)
         .key_down(keys.Keys.CONTROL)
         .send_keys("xvvvvvvv")
         .perform())
        sleep(3)

    # 鼠标双击
    def test_double_click(self):
        self.webdriver.get("https://vip.ceshiren.com/#/ui_study/frame")
        ele = self.webdriver.find_element(By.ID, "primary_btn")
        ActionChains(self.webdriver).double_click(ele).perform()
        # sleep(3)
        assert "该弹框点击两次后才会弹出" in self.webdriver.find_element(By.CLASS_NAME, "el-message-box__title").text

    def test_drag_and_drop(self):
        self.webdriver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 获取起始元素位置
        start_ele = self.webdriver.find_element(By.CLASS_NAME, "item1")
        # 获取目标元素位置
        target_ele = self.webdriver.find_element(By.CLASS_NAME, "item3")
        ActionChains(self.webdriver).drag_and_drop(start_ele, target_ele).perform()
        sleep(3)

    # 悬浮选择框选择输入
    def test_move_to_element(self):
        self.webdriver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.webdriver.find_element(By.CLASS_NAME, "title")
        ActionChains(self.webdriver).move_to_element(ele).perform()
        ActionChains(self.webdriver).click(
            self.webdriver.find_element(By.XPATH, '//*[@id="panel"]/div/div[2]/div[4]')).perform()
        sleep(3)

    # 滑动到目标元素上方
    def test_scroll_to_element(self):
        self.webdriver.get("https://ceshiren.com/")
        # 目标元素
        ele = self.webdriver.find_element(By.XPATH, '//*[text()="Chrome浏览器F12设置无网疑问"]')
        ActionChains(self.webdriver).scroll_to_element(ele).perform()
        sleep(3)

    # 坐标滑动
    def test_scroll_by_amount(self):
        self.webdriver.get("https://ceshiren.com/")
        ActionChains(self.webdriver).scroll_by_amount(0, 1000).perform()
        sleep(10)

