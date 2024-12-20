def sums(*args):
    sum = 0
    print(type(args))
    for item in args:
        sum = sum+item
    return sum

def prents(**kwargs):
    print(f"i got {kwargs['me']}")
    print(f"i got {kwargs['you']}")

if __name__ == "__main__":
    print(sums(3, 4, 5, 6, 7))
    print(prents(me='hh', you='lol'))
    a, *b = (3, 6, 8, 9)
    print(a, b)