#类 部分3
#算数魔法方法
class S(str):
    def __init__(self, strings) -> None:
        self.lenght = len(self)

    def __add__(self, other):
        return self.lenght + other.lenght
    
    def __lt__(self, other):
        return self.lenght < other.lenght
    
    def __getattr__(self, key):
        return key


s1 = S("savet")
s2 = S("hello")
print(s1 + s2)
print(s1 < s2)
print(s1.qwe)

class S1(str):
    def __add__(self, other):
        return NotImplemented

class S2(str):
    def __radd__(self, other):
        return len(self) + len(other)

s1 = S1("savet")
s2 = S2("hello")
print(s1 + s2)

class C:
    def __index__(self):
        print("__index__")
        return 0
c = C()
s = "savet"
print(s[c])

class C:
    def __init__(self, x, y) -> None:
        self.x = x
        self.__y = y
    def __getattribute__(self, __name):
        print("__getattribute__")
        return super().__getattribute__(__name)
    def __getattr__(self, __name):
        print("__getattr__")
        return __name

c = C(1, 2)
c.savet

class C:
    def __getitem__(self, index):
        print(index)
        return index
c = C()
c[1]

#slice
s = "savet"
print(s[2:4])
print(s[(slice(2, 4))])

class D:
    def __init__(self, start, stop) -> None:
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2

d = D(1, 10)
for i in d:
    print(i, end=" ")
