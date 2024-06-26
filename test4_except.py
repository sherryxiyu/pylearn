import argparse
import pytest

def get_args():
    parser = argparse.ArgumentParser(description='命令行中传入一个数字')
    parser.add_argument("num", help="input number")
    return parser

def test_except():
    try:
        raise TypeError
    except TypeError as e:
        print("im joking~", e)
    finally:
        print("clearning...")

params = [3, 4, 5, "beep"]
@pytest.mark.parametrize('cus_in', params)
def test_except_else(cus_in):
    try:
        assert isinstance(cus_in, int)
    except AssertionError as e:
        print("oh no not int", e)
    else:
        print("ahh,yes", cus_in)

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
@pytest.mark.smoke
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ == "__main__":
    args = get_args().parse_args()
    print("input number is", args.num)
