from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver2: WebDriver

    def __init__(self, driver2: WebDriver = None):
        self._driver2 = driver2

    def find2(self, locator, value: str = None):
        if isinstance(locator, tuple):
            return self._driver2.find_element(*locator)
        else:
            return self._driver2.find_element(locator, value)
    def get_toast(self):
        return self.find2(By.XPATH, "//*[@text='行情']").click()
