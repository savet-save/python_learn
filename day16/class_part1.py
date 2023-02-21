#类 第一部分
#类的定义 
class Turtel:
    head = 1
    eyes = 2
    legs = 4
    shell = True
    def crawl(self):
        print("a")
    
    def run(self):
        print("b")

#对象（实例化）
t1 = Turtel()
t1.crawl()
t1.run()
t1.legs = 3
print(t1.legs)

t2 = Turtel()
t2.mouth = 3
print(dir(t1))
print(dir(t2))

class C:
    #错误的函数，类的方法调用时会默认传递本身作为第一个参数
    def hello():
        print("hello")

try:
    C().hello()
except TypeError as e:
    print("error : ", e)

#继承
class A:
    x = 1
    def hello(self):
        print("hello")

class B(A):
    x = 3

b = B()
b.hello()
print(b.x)

#判断对象是属于特定类
print(isinstance(b, B))
print(isinstance(b, A))

#判断子类
print(issubclass(B, A))
print(issubclass(A, B))

class B:
    x = 3
    y = 4

#多重继承
class D(A, B):
    pass

d = D()
print(d.x)

#组合
class A:
    def hello(self):
        print("A")

class B:
    def hello(self):
        print("B")

class C:
    a = A()
    b = B()
    def hello(self):
        self.a.hello()
        self.b.hello()

C().hello()

class C:
    def set_x(self, v):
        self.x = v

c = C()
print(c.__dict__)
c.set_x(2)
print(c.__dict__)

class C:
    x = 50

c1, c2 = C(), C()
print(C.x)
print(c1.__dict__)
C.x = 200
c1.x = 100
print(C.x)
print(c1.x)
print(c2.x)
print(c1.__dict__, c2.__dict__)
print(C().x)

#构造函数
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

c = C(1, 2)
print(c.add())

#super()方法 - 避免在菱形多继承会重复调用基类构造函数的问题
#error
class A():
    def __init__(self) -> None:
        print("A")
class B1(A):
    def __init__(self) -> None:
        A.__init__(self)
        print("B1")
class B2(A):
    def __init__(self) -> None:
        A.__init__(self)
        print("B2")
class C(B1, B2):
    def __init__(self) -> None:
        B1.__init__(self)
        B2.__init__(self)
        print("C")
print("error")
C()

#ok
class A():
    def __init__(self) -> None:
        print("A")
class B1(A):
    def __init__(self) -> None:
        super().__init__()
        print("B1")
class B2(A):
    def __init__(self) -> None:
        super().__init__()
        print("B2")
class C(B1, B2):
    def __init__(self) -> None:
        super().__init__()
        print("C")
print("ok~")
C()

print(C.mro())
print(C.__mro__)