import requests


class TestWework:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww56ffa69b5ce468c7"
    secret = "N2dOmURuQy5rWiLBHDPPJuyQPiNNUQeJlp5vDTvt7jM"
    token = None

    # classmethod变量 使用setup_class在类执行之前运行一次,传递token给后面

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={"corpid": cls.corpid, "corpsecret": cls.secret})
        assert r.json()["errcode"] == 0
        print(r.json())
        cls.token = r.json()["access_token"]

    def test_get_token(self):
        r = requests.get(self.token_url,
                         params={"corpid": self.corpid, "corpsecret": self.secret})
        assert r.json()["errcode"] == 0
        print(r.json())
        self.token = r.json()["access_token"]

    def test_get_token_exist(self):
        assert self.token is not None

    def test_groupchat_get(self):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(base_url,
                          params={"access_token": self.token},
                          json={"offset": 0, "limit": 10})
        print(r.json())
        assert r.json()['errcode'] == 0
