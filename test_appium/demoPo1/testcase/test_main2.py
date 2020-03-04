from test_appium.demoPo1.page.app import App


class TestMain2:
    def setup(self):
        # self.main2=App2().start()
        self.main2 = App().start()
    def test_main2(self):
        self.main2.goto_stocks2()
        # self.main2.gotoStocks2()