import json

import requests

from test_request.api.wework import WeWork


class GroupChat(WeWork):
    secret = 'N2dOmURuQy5rWiLBHDPPJuyQPiNNUQeJlp5vDTvt7jM'

    def list(self, offset=0, limit=1000, **kwargs):
        data = {"offset": offset, "limit": limit}
        print(kwargs)
        print(data)
        data.update(kwargs)
        print(data)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    def get(self, chat_id):
        detail_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        r = requests.post(
            detail_url,
            params={'access_token': self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        self.format(r)
        return r.json()
