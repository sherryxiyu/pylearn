# https://blog.csdn.net/Jairoguo/article/details/104508721
def get_odds(length):
    for i in range(length):
        yield i*2

if __name__ == "__main__":
    a = [i for i in get_odds(10)]
    print(a)
    b = [('b', 8), ('a', 5), ('n', 3), ('y', 7), ('5', 2), ('o', 8)]
    b = sorted(b, key=lambda x:x[0])
    print(b)
    c = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
    print(c)