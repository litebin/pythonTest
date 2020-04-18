import requests

from test_request.test_api.api.wework import WeWork


class Department(WeWork):
    secret = "BvVKWuPLpUbTCzimY7S7YgiLjRtBAmJJ-S_MvNROhE8"

    def create(self, name, id, **kwargs):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": name, "parentid": id}
        data.update(kwargs)
        r = requests.post(base_url,
                          params={"access_token": WeWork.get_token(self.secret)},
                          json=data)
        return r.json()

    def update(self, id, **kwargs):
        base_usrl = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {"id": id}
        data.update(kwargs)
        r = requests.post(base_usrl,
                          params={"access_token": WeWork.get_token(self.secret)},
                          json=data)
        return r.json()

    def deleted(self, id):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(base_url,
                         params={"access_token": WeWork.get_token(self.secret),
                                 "id": id})
        return r.json()