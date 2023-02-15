#函数 part2
#闭包
def funcA():
    x = 123
    def funcB():
        print("B is " , x)
    return funcB

b = funcA()
b()

def power(exp):
    x = 123
    def exp_of(base):
        return base ** exp
    return exp_of

b2 = power(2)
b3 = power(3)
print(b2(2))
print(b3(2))

def create(defValue):
    x = defValue
    def move(value=0):
        nonlocal x
        x += value
        return x
    return move

player = create(1)
print(player())
print(player(-1))
print(player(+3))

#装饰器
def funcA():
    print("A")

def funcB(call):
    print("B")
    call()
    return None

funcB(funcA)

import time
def time_master(call):
    start = time.time()
    call()
    end = time.time()
    print("time sum ",end-start)

def funcA():
    time.sleep(2)

#time_master(funcA)

import time
def time_master(call):
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

funcA() #funcA = time_maset(funcA)

#装饰器嵌套
def y(call):
    def z():
        x = call()
        return x + 1
    return z

def q(call):
    def z():
        x = call()
        return x * 9
    return z

@y
@q
def funcA():
    return 3

print(funcA())

#带参装饰器
import time
def logger(msg):
    def time_master(call):
        def call_func():
            start = time.time()
            print("start..")
            call()
            print("end")
            end = time.time()
            print(f"msg{msg} time sum ",end-start)
            return None
        return call_func
    return time_master

@logger(msg=3)
def funcA():
    time.sleep(1)
    print("A")

@logger(msg=1)
def funcB():
    time.sleep(2)
    print("B")

funcA() #funcA = logger(msg=3)()
funcB() #funcB = logger(msg=1)()