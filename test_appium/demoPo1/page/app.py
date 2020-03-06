import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.demoPo1.page.base_page import BasePage
from test_appium.demoPo1.page.main import Main


class App(BasePage):
    _package2 = "com.xueqiu.android"
    _activity2 = ".view.WelcomeActivityAlias"

    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = self._package2
        caps["appActivity"] = self._activity2
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
        caps["chromedriverExecutable"] = r"D:\myDriver\2.20\chromedriver.exe"

        # caps['avd'] = 'Pixel_2_API_23'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        return self



    # def start(self):
    #     return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self.driver)

    # def main2(self) -> Main2 :
    #     # todo: wait main page
    #     def wait_load(driver):
    #         print(datetime.datetime.now())
    #         source = self._driver2.page_source
    #
    #         if "我的" in source:
    #             return True
    #         if "同意" in source:
    #             return True
    #         if "image_cancel" in source:
    #             return True
    #         return False
    #
    #     WebDriverWait(self._driver2, 60).until(wait_load)
    #     return Main2(self._driver2)
