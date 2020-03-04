from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExercise:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaobin"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["skipServerInstallation"] = True
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

    def test_webview2(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(By.XPATH, "//*[@text='交易'and contains(@resource-id,'tab')]").click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        self.driver.find_element(By.XPATH, "//*[@text='A股开户']").click()
        self.driver.find_element(By.XPATH, "//*[@text='平安证券开户享1年Lv2']").click()
        self.driver.find_element(By.ID, "phone-number").click()
        self.driver.find_element(By.ID, "phone-number").send_keys("18321807715")

    # def teardown(self):
    #     self.driver.quit()
    def test_webview_natvie(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        # self.driver.find_element(By.ID, 'phone-number').send_keys("15600534760")
        submit = (By.XPATH, "//*[@content-desc='立即开户']")
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(submit))
        sleep(2)

        phone = (MobileBy.XPATH, "//android.widget.EditText")
        self.driver.find_element(*phone)
        # self.driver.find_element(*phone).click()
        # self.driver.find_element(*phone).send_keys("15600534760")

        for element in self.driver.find_elements(*phone):
            try:
                # element.click()
                element.send_keys("15600534760")
            except Exception as e:
                print(element.get_attribute("class"))
                print(element.get_attribute("resource-id"))
                print(element.get_attribute("content-desc"))
                print(e)
