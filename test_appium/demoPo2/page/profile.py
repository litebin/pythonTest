from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.demoPo2.page.base_page import BasePage


class Profile(BasePage):
    def login_by_error_password(self,phone,passwd):
        # 帐号密码登陆
        self.find(By.XPATH, "//*[contains(@resource-id, 'rl_login')]//*[@index='1']").click()
        self.find(By.ID, "login_account").send_keys(phone)
        self.find(By.ID, "login_password").send_keys(passwd)
        self.find(By.ID, "button_next").click()
        msg = self.find(By.ID, "md_content").text
        self.find(By.ID, "md_buttonDefaultPositive").click()
        return msg
