import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.demoPo2.page.base_page import BasePage
from test_appium.demoPo2.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 如果driver不存在即为None,直接创建
        # 如果driver存在复用原来的driver
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            # caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
            caps["chromedriverExecutable"] = r"D:\myDriver\2.20\chromedriver.exe"

            # caps['avd'] = 'Pixel_2_API_23'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            print(self._driver)
            self._driver.start_activity(self._package, self._activity)
        return self

    # def start(self):
    #     return self

    def restart(self):
        pass

    def stop(self):
        pass

    # 改造第一次,加载首页出现
    # def main(self) -> Main:
    #     WebDriverWait(self._driver, 30).until(lambda x: "我的" in self._driver.page_source)
    #     return Main(self._driver)

    def main(self) -> Main:
        # todo: wait main page
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source

            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False
        WebDriverWait(self._driver, 60).until(wait_load)
        return Main(self._driver)
