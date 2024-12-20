import pytest
from autobench import AutoBench
import random
#写一个带addoption的用例
@pytest.fixture(scope='function')
def autobench():
    autobench = AutoBench()
    return autobench

@pytest.fixture(scope='module')
def printname(request):
    print("now running", request.module)
    a = random.randint(1, 1000)
    yield a
    print("case finish")

def pytest_addoption(parser):
    parser.addoption("--arch", action='store', default="npu-v1", help="selet v1 v2")
    parser.addoption("--stringinput", action='append', default=[], help="parameterize input")

@pytest.fixture(scope="session")
def arch(request):
    return request.config.getoption("arch")

#入参转参数
def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:#需要确认fixturenames的用法
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
