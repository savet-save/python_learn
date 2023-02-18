#函数 part4
#函数文档 - help
def funcA():
    """
    not thing
    """
    return "No thing"

help(funcA)

#类型注释
def funcB(num:int, default:str = "qwe") -> int:
    print(default)
    return num

funcB("1", 2)

def funcB(num:list[int], default:str = "qwe") -> list[int]:
    print(default)
    return num

print(funcB([1, 2], 2))

#内省
print(funcA.__name__)
print(funcB.__annotations__)

#高阶函数
def add(a:int, b:int) -> int:
    return a + b

#reduce
import functools
print(functools.reduce(add, [1, 2, 3, 4, 5]))

#partial
import functools
square = functools.partial(pow, exp=2)
print(square(3))

#wraps
import time
import functools
def time_master(call):
    @functools.wraps(call)
    def call_func():
        start = time.time()
        print("start..")
        call()
        print("end")
        end = time.time()
        print("time sum ",end-start)
        return None
    return call_func

@time_master
def funcA():
    time.sleep(2)
    print("hello")

print(funcA.__name__)