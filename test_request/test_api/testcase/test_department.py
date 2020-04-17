from test_request.test_api.api.department import Department
from test_request.test_api.api.wework import WeWork


class TestDepartment:

    def setup(self):
        self.department = Department()

    def test_token(self):
        r = WeWork.get_token("BvVKWuPLpUbTCzimY7S7YgiLjRtBAmJJ-S_MvNROhE8")
        print(r)
        assert r['errcode'] == 0

    def test_create(self):
        r = self.department.create("hello", 1)
        print(r)
        assert r['errmsg'] == "created"
