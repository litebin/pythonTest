from appium.webdriver.common.mobileby import MobileBy

from test_appium.demoPo1.page.base_page import BasePage


class Search(BasePage):
    #使用第一种方法传递driver,每个class中都需要init方法传递值
    def __init__(self, driver):
        self._driver = driver

    def search(self, key: str):
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str):
        return float(self._driver.find_element(MobileBy.ID, "current_price").text)

