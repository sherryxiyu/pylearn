# https://blog.csdn.net/yilulvxing/article/details/85374142
class A:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b
        self.c = 1

    def print_vals(self):
        print(self.a,self.b,self.c)

class B(A):
    def __init__(self):
        super().__init__()
        self.a = 9

class C(A):
    def __init__(self, a, b):
        A.__init__(self, a, b)
        self.a = 7

class D(A):
    def __init__(self, c):
        A.__init__(self)
        self.c = c

if __name__ == "__main__":
    d1 = D(c=10)
    d1.print_vals()
    b1 = B()
    b1.print_vals()
    c1 = C(a=5, b=6)
    c1.print_vals()
