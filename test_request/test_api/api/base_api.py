import json


class BaseApi:
    # 格式化返回值,indent缩进
    def fromat(self, r):
        print(json.dumps(r.json(), indent=2))
