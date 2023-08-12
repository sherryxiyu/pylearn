import requests
import json


def deal_requests(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        try:
            r.raise_for_status()
            print("access success!")
            return json.loads(r.content)
        except requests.HTTPError as e:
            raise e
    return wrapper


@deal_requests
def post(url, data):
    res = requests.post(url, json=data, timeout=20)
    return res


@deal_requests
def get(url):
    res = requests.get(url)
    return res