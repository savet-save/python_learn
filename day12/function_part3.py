#函数 part3
#lambda
def squareX(x):
    return x * x

print(squareX(2))

squareY = lambda y : y * y
print(squareY(2))

y = [squareX, squareY]
print(y[0](2), y[1](2))

y = [lambda x : x * 2, 2, 3]
print(y[0](y[2]))

#generator（生成器）
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1

print(counter())
for i in counter():
    print(i)

def test():
    i = 0
    yield i
    print("a", end=" ")
    i += 1
    yield i
    print("b", end=" ")
    i += 1
    yield i

for i in test():
    print(i)

#生成器推导式
t = (i ** i for i in range(10))
print(list(t))

#recursion(递归)
def funcA(i):
    if (i <= 0):
        return None
    print("QWE")
    funcA(i - 1)

funcA(10)
