import requests


class TestDepartment:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww56ffa69b5ce468c7"
    secret = "BvVKWuPLpUbTCzimY7S7YgiLjRtBAmJJ-S_MvNROhE8"
    token = None

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={"corpid": cls.corpid, "corpsecret": cls.secret})
        assert r.json()["errcode"] == 0
        print(r.json())
        cls.token = r.json()["access_token"]

    def test_department(self):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": "广州研发中心", "parentid": 1}
        r = requests.post(base_url,
                          params={"access_token": self.token},
                          json=data)
        print(r.json())
