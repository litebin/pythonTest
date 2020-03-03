# import HTMLTestRunner
import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl


class TestQQlessons(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def get_value(self, x, y):
        workbook = openpyxl.load_workbook("./test_data.xlsx")
        sheet = workbook.get_sheet_by_name("Sheet1")
        sheet_cell = sheet.cell(row=x, column=y)
        sheet_value = sheet_cell.value
        return sheet_value

    def test_search(self):
        self.driver.get("https://ke.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR, self.get_value(2, 1)).send_keys(self.get_value(2, 2))
        self.driver.find_element(By.CSS_SELECTOR, self.get_value(3, 1)).click()

    # def test_search(self):
    #     self.driver.get("https://ke.qq.com/")
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(By.CSS_SELECTOR, "#js_keyword").send_keys("霍格沃兹测试学院")
    #     self.driver.find_element(By.CSS_SELECTOR, "#js_search").click()

    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    filepath = r"D:\PycharmProjects\pythonTest\ui_unitest\report.html"
    # 实例化suite
    suite = unittest.TestSuite()
    # 跑测试用例
    suite.addTest(TestQQlessons('test_search'))
    ftp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='welcome to web')
    runner.run(suite)
    """
    suite = unittest.TestSuite()
    suite.addTest(TestQQlessons('test_search'))
    filename ='testreport.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, description='接口用例执行情况：', title='接口自动化测试报告')
    runner.run(suite)
    fp.close()
"""
