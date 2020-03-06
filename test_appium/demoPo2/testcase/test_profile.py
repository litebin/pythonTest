from test_appium.demoPo2.page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().start().main().goto_profile()

    def test_login(self):
        assert "错误" in self.profile.login_by_error_password("18321635241", "1234567")
