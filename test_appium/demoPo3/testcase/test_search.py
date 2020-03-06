import pytest
import yaml

from test_appium.demoPo3.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_main(self):
        App().start().main().goto_search().search("JD")

    def test_select(self):
        assert "已添加" in App().start().main().goto_search().search("JD").add_select().get_msg()

    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data.yaml")))
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search().search(key).get_price(stock_type) > price