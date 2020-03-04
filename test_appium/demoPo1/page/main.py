from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_appium.demoPo1.page.base_page import BasePage
from test_appium.demoPo1.page.search import Search


class Main(BasePage):
    _driver: WebDriver

    def __init__(self, driver):
        self._driver = driver

    def goto_search_page(self):
        self._driver.find_element(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    def goto_stocks2(self):
        # self._driver2.find_element(By.XPATH, "//*[@text='行情']").click()
        # self._driver2.find2(By.XPATH, "//*[@text='行情']")
        self.find2(By.XPATH, "//*[@text='行情']").click()
        return self
        # return Stock2(self._driver2)

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass

    def goto_messages(self):
        pass
