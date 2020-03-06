from selenium.webdriver.common.by import By

from test_appium.demoPo3.page.base_page import BasePage
from test_appium.demoPo3.page.search import Search


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, "tv_search").click()
        self.steps("../testcase/step.yaml")
        return Search(self._driver)
