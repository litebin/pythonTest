import requests

from test_request.test_api.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "ww56ffa69b5ce468c7"
    # 把方法改成类方法,可以不用实例化
    @classmethod
    def get_token(cls, secrete):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(base_url,
                         params={"corpid": cls.corpid, "corpsecret": secrete})
        return r.json()['access_token']
