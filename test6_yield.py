# 迭代器：
# https://blog.csdn.net/Jairoguo/article/details/104483824
# 生成器：
# https://blog.csdn.net/Jairoguo/article/details/104508721
# 当一个生成器函数被调用的时候，它返回一个迭代器，称为生成器或者生成器对象。
def get_odds(length):
    for i in range(length):
        yield i*2


def get_input(inputs):
    for i in range(5):
        res = yield inputs+i
        print(res)  # 这里已经被返回了，从这里继续执行局部变量res未被赋值
        # yield res


if __name__ == "__main__":
    a = [i for i in get_odds(10)]
    print(a)
    d = [i for i in get_input(3)]
    print(d)