from test_appium.demoPo3.page.app import App
from test_appium.demoPo3.page.base_page import BasePage


class TestDD:
    def test_dd(self):
        base = BasePage()
        base.steps("../testcase/step.yaml")

    def test_ddSearch(self):
        App().start().main().goto_search().search("alibaba")
