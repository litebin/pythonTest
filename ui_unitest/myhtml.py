from selenium import webdriver
import unittest


class TestQQlessons:
    def setup(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

    def test_search(self):
        self.driver.get("https://ke.qq.com/")
        self.driver.implicitly_wait(2)



if __name__ == '__main__':
    unittest.main()
