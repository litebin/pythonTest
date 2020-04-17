from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaobin"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        caps["skipServerInstallation"] = True
        # 指向chromeDriver的目录
        # caps["chromedriverExecutableDir"] = r"D:\myDriver\2.20"
        # 直接指向chromeDriver
        caps["chromedriverExecutable"] = r"D:\myDriver\2.20\chromedriver.exe"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(20)

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (By.XPATH, "//*[contains(@resource-id,'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        price = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")
        print(type(self.driver.find_element(*price).text))
        assert float(self.driver.find_element(*price).text) < 219
        print(self.driver.find_element(*price).get_attribute("resourceId"))

    def test_open_acount_webview(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "港美股开户").click()

        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        sleep(5)
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # 切换到webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.page_source)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="请输入手机号"]')))
        # WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="请输入手机号"]')))
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入手机号"]').send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入验证码"]').send_keys("555555")
        # 切换回原生native
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.ID, "action_bar_back").click()
