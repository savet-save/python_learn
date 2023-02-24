#类 part4
class C:
    def __init__(self, data) -> None:
        self.data = data
    
    def __contains__(self, item):
        print("~")
        return item in self.data

c = C([1, 2, 3, 4])
print(3 in c)

print(repr(123)) #'123'
print(repr("123")) #"'123'"

#代理property
class C:
    def __init__(self) -> None:
        self._x = 200
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx)

c = C()
print(c.x)
print(c.__dict__) #{'_x': 200}
del c.x
print(c.__dict__) #{}
#error
#c.getx()

class D:
    def __init__(self) -> None:
        self._x = 200
    @property
    def x(self):
        return self._x
    #x = property(getx)

d = D()
print(d.x)
#error
#d.x = 2

class D:
    def __init__(self) -> None:
        self._x = 200
    @property
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
d.x = 2
print(d.x)

class C:
    count = 0
    def __init__(self) -> None:
        C.count += 1
    @classmethod
    def get_count(cls):
        print(f"object count : {cls.count}")

c1, c2 = C(), C()
c1.get_count()

class C:
    count = 0
    def __init__(self) -> None:
        C.count += 1
    @staticmethod
    def get_count():
        print(f"object count : {C.count}")

c1, c2 = C(), C()
c1.get_count()