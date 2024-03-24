def outer(a):               #定义函数要一杯不同类型的饮料
    def inner(b):            #定义内层函数，饮料的容量
        print(f'要一杯{a}')
        print(f'容量是{b}毫升')
    return inner
   #执行内层函数
blacktea=outer('红茶')                 #调用外层函数，并把结果赋值给f
greentea=outer('绿茶')
blacktea(300)
greentea(500)

#装饰器解包
#尝试用装饰器检测函数执行时间
import time
def cautime(func):
    st = time.time()
    def wrapper(*args, **kwrags):
        t = func(*args, **kwrags)
        dtt = st-t
        print(f"during {dtt} time.")
        return t
    return wrapper

@cautime
def waiting(ti):
    time.sleep(ti)
    a = time.time()
    return a

if __name__ == '__main__':
    waiting(2)