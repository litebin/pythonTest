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

    def test_update(self):
        r = self.department.update(9, name="abcde")
        print(r)
        assert r['errmsg'] == "updated"

    def test_delete(self):
        rs = self.department.create("abcds", 1)
        print(rs)
        self.id = rs['id']
        r = self.department.deleted(self.id)
        print(r)
        assert r["errmsg"] == "deleted"
