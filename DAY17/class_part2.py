#函数 第二部分
#多态
class Shape:
    def __init__(self, name) -> None:
        self.name = name
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__("Square")
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
s = Square(4)
c = Circle(5)
print(s.name, s.area(), c.name, c.area())

class A:
    def __init__(self, name) -> None:
        self.name = name
    def say(self):
        print(f"A is {self.name}")

class B:
    def __init__(self, name) -> None:
        self.name = name
    def say(self):
        print(f"B is {self.name}")

class C:
    def __init__(self, name) -> None:
        self.name = name
    def say(self):
        print(f"C is {self.name}")

def qwq(x):
    x.say()
    return None

a = A("a")
b = B("b")
c = C("c")
qwq(a)
qwq(b)
qwq(c)

#私有变量（名字改编）
class A:
    def __init__(self, x) -> None:
        self.__x = x

a = A(2)
try:
    print(a.__x)
except:
    print("error")
print(a.__dict__)
print(a._A__x)

#__slots__
class B:
    __slots__ = ["x", "y"]
    def __init__(self, x) -> None:
        self.x = x
b = B(2)
b.x = 3
b.y = 4
try:
    b.z = 5
except AttributeError as e:
    print("error : ", e)

#魔法方法
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)

c = CapStr("hello")
print(c)
