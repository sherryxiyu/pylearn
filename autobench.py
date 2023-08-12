import random
import requests_util


class AutoBench:
    def __init__(self):
        self.hp = HttpBin()
        self.gd = GenData()


class HttpBin:
    __post_url = 'http://httpbin.org/post'
    __get_url = 'http://httpbin.org/get'

    def httpbin_post(self, data):
        res = requests_util.post(self.__post_url, data)
        return res

    def httpbin_get(self):
        res = requests_util.get(self.__get_url)
        return res

class GenData:
    def gen_http_bin_data(self, cus_name, size):
        size_dic = {
            's': "small", 'm': 'medium', 'l': 'large'
        }
        topping = ['Bacon', 'Extra Cheese', 'Onion', 'Mushroom']
        biz = {
            "comments": "",
            "custemail": "",
            "custname": cus_name,
            "custtel": "",
            "delivery": "",
            "size": size_dic[size],
            "topping": topping[random.randint(0, len(topping)-1)],
        }
        return biz