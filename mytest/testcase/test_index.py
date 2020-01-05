from mytest.page.index import Index
# from mytest.page.register import Register


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_index2(self):
        self.index.goto_register().register()

    # def teardown(self):
    #     self.index.close()
    def test_register(self):
        register_page = self.index.goto_register().register()
        assert "请填写正确的验证码" == register_page.get_massage()
