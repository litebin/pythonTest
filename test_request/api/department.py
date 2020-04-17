import requests

from test_request.api.wework import WeWork


class Department(WeWork):
    secret = "BvVKWuPLpUbTCzimY7S7YgiLjRtBAmJJ-S_MvNROhE8"

    def create_department(self, name, parentid, **kwargs):
        base_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # data = {"name": "广州研发中心", "name_en": "RDGZ", "parentid": 1, "order": 1, "id": 2324}
        data = {"name": name, "parentid": parentid}
        data.update(kwargs)
        r = requests.post(base_url,
                          params={"access_token": WeWork.get_token(self.secret)},
                          json=data)
        self.format(r)
        return r.json()

    def update_department(self):
        pass

    def delet_department(self):
        pass
