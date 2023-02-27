#类 part4
#描述符
class A:
    def __get__(self, instance, owner):
        print(f"get -> self : {self}, instance : {instance}, owner : {owner}")
    def __set__(self, instance, value):
        print(f"set - > self : {self}, instance : {instance}, value : {value}")
    def __delete__(self, instance):
        print(f"del - > self : {self}, instance : {instance}")

class B:
    x = A()

b = B()
b.x = 200
b.x
del b.x
b.x

class MyProPerty():
    def __init__(self, fget=None, fset=None, fdel=None) -> None:
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)
    def getter(self, func):
        self.fget = func
        return self
    def setter(self, func):
        self.fset = func
        return self
    def deleter(self, func):
        self.fdel = func
        return self

class C:
    def __init__(self) -> None:
        self._x = 250
    @MyProPerty #x = MyProPerty(x)
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

c = C()
print(c.x)
print(c.__dict__)
c.x = 20
print(c.x)
del c.x
print(c.__dict__)

class D:
    def __init__(self) -> None:
        self._x = 250
    x = MyProPerty()
    @x.getter
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

d = D()
print(d.x)
print(d.__dict__)
d.x = 30
print(d.x)
del d.x
print(d.__dict__)


#__set_name__
class E:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        print("get~")
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        print("set~")
        instance.__dict__[self.name] = value

class F:
    x = E()

f = F()
print(f.x)
f.x = 200
print(f.x)


#类装饰器
def report(cls):
    def oncall(*args, **kwargs):
        print("start")
        _ = cls(*args, **kwargs)
        print("end")
        return _
    return oncall

@report
class C:
    pass

c = C()


class Call:
    def __init__(self, func) -> None:
        self.x = 0
        self.func = func
    def __call__(self, *args, **kwds):
        self.x = self.x + 1
        print(self.x)
        return self.func(*args, **kwds)

@Call
def func():
    print("func")

print(func)
func()
func()

def call(func):
    class OnCall:
        def __init__(self) -> None:
            pass

#type
class C:
    pass
C = type('C', (), {})
c = C()
print(c.__class__)
print(C.__bases__)
print(type(C))
print(type(type))

#元类 - metaclass
class MetaC(type):
    pass

class C(metaclass = MetaC):
    pass
c = C()
print(type(c))
print(type(C))
print(type(type))

#单实例类
class SimpleInstance(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        type.__init__(cls, *args, **kwargs)
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kwargs)
            return cls.__instance
        else: 
            return cls.__instance

class C(metaclass = SimpleInstance):
    pass
c1 = C()
c2 = C()
print(c1 is c2)
print(dir(C))

#抽象基类
from abc import ABCMeta, abstractmethod
class Fruit(metaclass = ABCMeta):
    def __init__(self, name) -> None:
        self.name = name
    @abstractmethod
    def eat(self):
        pass

try:
    f = Fruit("f")
except TypeError as e:
    print("error : ", e)

class Banana(Fruit):
    pass

try:
    b = Banana("f")
except TypeError as e:
    print("error : ", e)

class Banana(Fruit):
    def eat(self):
        print("eat")

b = Banana("b")
b.eat()