from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.demoPo2.page.base_page import BasePage


class Stock2(BasePage):
    def search(self):
        self.find(MobileBy.ID, "action_search").click()
        self.find(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.find(By.XPATH, "//*[@text='BABA']").click()
        self.find(By.XPATH, "//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        return self