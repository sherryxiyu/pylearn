import pytest
from time import sleep

params = [
    {'form': {'custname': [(1,1), (2,2)], 'custemail': 0}},
    {'form': {'custname': [(2,1), (2,2)], 'custemail': 1}},
]


@pytest.mark.parametrize('dics', params)
def test_case0727(dics, autobench, printname):
    print(dics)
    autobench.hp.httpbin_post(dics)


@pytest.mark.repeat(2)
def test_case0728(autobench, printname):
    print("count:", printname)
    data = autobench.gd.gen_http_bin_data('ming', 's')
    sleep(2)
    autobench.hp.httpbin_post(data)
    print(data)


def test_case0728_02(autobench):
    res = autobench.hp.httpbin_get()
    print(res)


def test_case0803(arch):
    print(arch)


#to do:添加上传文件的用例
#to do:尝试链接容器存储测试用例到redis