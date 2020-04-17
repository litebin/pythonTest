import os

from appium import webdriver
from appium.webdriver.common import mobileby
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True
        # 在mac下获取udid,在windows下需要set udid的值,且需要管理员模式才可以运行
        # set udid= emulator-5554 &&pytest test_appium.py
        # caps['udid'] = os.getenv("udid")
        # # caps['udid'] = "emulator-5554"
        # self.driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def test_shell(self):
        result = self.driver.execute_script('mobile: shell', {
            'command': 'echo',
            'args': ['arg1', 'arg2'],
            'includeStderr': True,
            'timeout': 5000
        })
        print(result)

    def test_search(self):
        self.driver.find_element(By.ID, 'tv_search').click()
        self.driver.find_element(By.ID, 'search_input_text').send_keys("alibaba")
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id, "follow_btn")]').click()
        self.driver.find_element(By.ID, 'action_delete_text').click()
        self.driver.find_element(By.ID, 'search_input_text').send_keys("alibaba")
        self.driver.find_element(By.XPATH, '//*[@text="BABA"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        res = self.driver.find_element(By.XPATH,
                                       '//*[@text="09988"]/../../..//*[contains(@resource-id, "followed_btn")]').get_attribute(
            "text")
        self.driver.hide_keyboard()

        mobileby
        assert "已添加" == res
