import requests

from test_request.api.department import Department
from test_request.api.wework import WeWork


class TestWeWork:

    @classmethod
    def setup_class(cls):
        cls.department = Department()

    # def test_gettoken(self):
    #     r = WeWork.get_token("N2dOmURuQy5rWiLBHDPPJuyQPiNNUQeJlp5vDTvt7jM")
    #     print(r)
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww56ffa69b5ce468c7"
    secret = "BvVKWuPLpUbTCzimY7S7YgiLjRtBAmJJ-S_MvNROhE8"
    access_token = ""

    def test_gettoken(self):
        r = requests.get(self.token_url,
                         params={"corpid": self.corpid, "corpsecret": self.secret})
        assert r.json()["errcode"] == 0
        print(r.json())
        self.access_token = r.json()["access_token"]

    def test_department(self):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": "广州研发中心", "parentid": 1}
        r = requests.post(base_url,
                          params={"access_token": self.access_token},
                          json=data)
        print(r.json())
    # def test_groupchat_get(self):
    #     r = self.department.create_department()
    #     assert r['errcode'] == 0
