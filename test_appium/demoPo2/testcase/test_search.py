import pytest

from test_appium.demoPo2.page.app import App


class TestSearch:
    def setup(self):
        # App().start()点main方法点不出来,不能链式调用
        # 检查发现没有继承class App(BasePage)
        # 检查发现start()方法没有返回return self
        # 返回self后可在App类中调用 main方法
        # self.main=App().start().main()
        self.main = App().start().main()

    def test_search_single(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 200

    def test_select(self):
        assert "已添加" in self.main.goto_search_page().search("JD").add_select().get_msg()

    @pytest.mark.parametrize("key,stock_type,price", [
        ("alibaba", "BABA", 200),
        ("JD", "JD", 20)])
    def test_search(self, key, stock_type, price):
        assert float(self.main.goto_search_page().search(key).get_price(stock_type)) > price
