import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Testtesterhomework():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.vars = {}

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def teardown_method(self, method):
        time.sleep(2)
        self.driver.quit()

    def test_testerhome_work(self):
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1222, 823)
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # time.sleep(2)
        element = (By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".topic-21848 .title > a").click()
