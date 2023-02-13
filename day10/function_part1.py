#函数 第一部分
#创建
def myfunc():
    print("savet")

def myfunc(name):
    print("my name is " + name)

#调用
#myfunc()

myfunc("savet")

#函数的返回
def div(x, y):
    return x / y

print(div(1, 2))

def div(x, y):
    if y == 0:
        return 0
    return x / y

print(div(1, 0))

#关键字参数
def myfunc(vo, vi, vt):
    return "+".join((vt, vi, vo))

print(myfunc(vt="1", vi="2", vo="3"))

#error
#print(myfunc(vt="1", "2", "3"))

print(myfunc("1", vt="2", vi="3"))

def myfunc(vo, vi, vt="4"):
    return "+".join((vt, vi, vo))
print(myfunc("1", "2"))

help(myfunc)

#禁用关键字参数
def myfunc(vo, /, vi, vt):
    print(vo , vi, vt)

#myfunc(vo="1", vi="2", vt="3") #error
myfunc("1", vi="2", vt="3")
myfunc("1", "2", "3")

#禁用位置参数
def myfunc(vo, *, vi, vt):
    print(vo , vi, vt)

#myfunc("1", "2", "3") #error
myfunc(vo="1", vi="2", vt="3")
myfunc("1", vi="2", vt="3")

#收集参数(元组参数)
def myfunc(*args):
    print("args has {} numbers".format(len(args)))
    print("args is {} type".format(type(args)))

myfunc(1, 2, 3)

#help(print)

#收集参数-字典类型
def myfunc(**args):
    print(args)

myfunc(a=1, b=2, c=3)

#解包参数
def myfunc(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
#myfunc(args) #error
myfunc(*args)

#解包参数-字典类型
def myfunc(a, b, c):
    print(a, b, c)

args = {"a": 1, "b": 2, "c": 3}
#myfunc(args) #error
myfunc(**args)

#global语句（定义全局变量）
def myfunc():
    global x
    x = 12
    return None

x = 11
myfunc()
print(x)

#嵌套函数
def funcA():
    num = 123
    def funcB():
        num = 521
        #num += 1 #error
        print("B is " , num)
    funcB()
    print("A is " , num)

#funcB() #error
funcA()


def funcA():
    num = 123
    def funcB():
        nonlocal num 
        num += 1 #ok
        print("B is " , num)
    funcB()
    print("A is " , num)

funcA()