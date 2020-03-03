from test_appium.page.app import App



class TestStock:
    def setup(self):
        self.main = App().start().main()

    def test_stocks_earch(self):
        self.main.goto_stocks().search().add_select().cancel()
