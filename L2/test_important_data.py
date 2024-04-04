from selenium.webdriver.common.by import By

from Base.base import Base
from Base.log import logger


class TestImportantData(Base):
    """
    1.日志
    2.截图
    3.page source
    """

    def test_log_data_record(self):
        # 实例化self.driver
        search_content = "霍格沃兹测试开发学社"
        # 打开搜狗首页
        self.webdriver.get("https://www.sogou.com/")
        logger.debug("打开搜狗首页")
        # 输入霍格沃兹测试学院
        self.webdriver.find_element(By.CSS_SELECTOR, "#query").send_keys(search_content)
        logger.debug(f"搜索的内容为{search_content}")
        # 点击搜索
        self.webdriver.find_element(By.CSS_SELECTOR, "#stb").click()
        # 搜索结果
        search_res = self.webdriver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"搜索结果为{search_res.text}")
        # 保存截图文件
        self.webdriver.save_screenshot("test_important_data.png")
        with open("test_important_data.html", "w",encoding="utf-8") as f:
            f.write(self.webdriver.page_source)

        assert search_res.text == search_content
