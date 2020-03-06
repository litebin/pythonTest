import logging

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, 'image_cancel'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 10
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    #
    # def find(self, locator, value: str = None):
    #     if isinstance(locator, tuple):
    #         return self._driver.find_element(*locator)
    #     else:
    #         return self._driver.find_element(locator, value)

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").click()

    # todo: 当有广告、评价、升级各种弹窗出现的时候,要进行异常流程处理
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 常规写法
            # if isinstance(locator, tuple):
            #     return self._driver.find_element(*locator)
            # else:
            #     return self._driver.find_element(locator, value)

            # 寻找控件,if判断简写方式
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element

        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数+1
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 寻找原来的正常控件
                    return self.find(locator, value)
            # 如果黑名单也没有就报错
            logging.warn("black list no on found")
            raise e

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))
