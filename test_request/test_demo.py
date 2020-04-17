import requests
from requests import Response, Session

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}

url_get = "http://47.98.220.165:6001/get"


def test_request():
    r = requests.get('https://home.testing-studio.com/categories.json')
    # print(r.content)
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post('http://47.98.220.165:6001/post',
                      params={"a": 1, "b": 2, "c": "ccccc"},
                      data={"a": 11, "b": 22, "c": "222ccccc"})
    print(r.json())
    assert r.status_code == 200


def test_upload():
    r = requests.post('http://47.98.220.165:6001/post',
                      files={"file": open("__init__.py", 'rb')})
    print(r.json())
    assert r.status_code == 200


def test_session():
    s = Session()
    s.proxies = proxies
    # s.verify = False
    s.get(url_get)
    s.mount()


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        # r.content = "OK HOOK SUCCESS"
        r.decode_content = "demo content"
        # rn = Response()

        return r

    r = requests.get(
        "http://47.98.220.165:6001/get",
        params={
            "a": 1,
            "b": 2,
            "c": "cccc"
        },
        hooks={"response": [modify_response]}
    )

    print(r.json())
    print(r.decode_content)
    r.text
    assert r.decode_content == "demo content"
    assert r.status_code == 200
