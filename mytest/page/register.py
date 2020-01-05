from time import sleep

from selenium.webdriver.common.by import By

from mytest.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self._driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys("企业微信")
        self._driver.find_element(By.CSS_SELECTOR, '#corp_industry').click()
        self._driver.implicitly_wait(2)
        self._driver.find_element(By.CSS_SELECTOR, '[data-name="IT服务"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '[data-name="计算机软件/硬件/信息服务"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '#corp_scale_btn').click()
        self._driver.find_element(By.CSS_SELECTOR,
                                   '.qui_dropdownMenu.ww_dropdownMenu ul li:nth-child(2)[data-value="2002"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys("mike")  # 输入管理员姓名
        self._driver.find_element(By.CSS_SELECTOR, '#register_tel').send_keys("13688889999")  # 输入管理员手机号
        # self._driver1.find_element(By.CSS_SELECTOR, '#vcode').send_keys("123456")  # 输入短信验证码
        self._driver.find_element(By.CSS_SELECTOR, '#iagree').click()
        self._driver.find_element(By.CSS_SELECTOR, '#submit_btn').click()
        return self

    def get_massage(self):
        sleep(3)
        res = self._driver.find_element(By.CSS_SELECTOR,
                                        ".register_column_item_cnt.ww_inputWithTips.ww_inputWithTips_WithErr div div.js_error_msg").text
        return res
