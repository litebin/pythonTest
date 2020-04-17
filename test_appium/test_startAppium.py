import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppium:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True


        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_search_hk_price(self):
        stock_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]/*[@text='股票']")
        price_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        price = self.driver.find_element(*price_locator).text
        assert float(price) < 218

    def test_check_add_status(self):
        stock_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]/*[@text='股票']")
        optional_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'follow_btn')]")
        already_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'followed_btn')]")
        next_time_locator = (MobileBy.XPATH, "//*[@text='下次再说' and contains(@resource-id, 'tv_left')]")

        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.ID, "tv_agree")))
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        self.driver.find_element(*optional_locator).click()
        next_time_element = self.driver.find_elements(*next_time_locator)
        if len(next_time_element) != 0:
            next_time_element[0].click()

        self.driver.find_element(MobileBy.ID, "action_close").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        optional_status = self.driver.find_element(*already_locator).get_attribute("text")
        print(optional_status)
        assert "已添加" == optional_status