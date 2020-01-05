from selenium.webdriver.common.by import By

from mytest.page.base_page import BasePage
from mytest.page.register import Register

class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

