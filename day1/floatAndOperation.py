# float
print(0.3)
print(0.1 + 0.2)
print(0.3 == 0.1 + 0.2)

# decimal数
import decimal
a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
c = decimal.Decimal("0.3")
print(a + b == c)

# 指数
print(0.00005)

# 虚数
x = 1 + 2j
print(x.real)
print(x.imag)

# 运算符

# '//' 是向下取整
print(3 / 2) #1.5
print(3 // 2) #1
print(-3 // 2) #-2 

print(float('+1E5')) #100000.0
print(pow(2, 3)) #8
print(2 ** 3) #8
print(2 ** -3) #0.125
print(pow(2, 3, 5)) #2^3 % 5 =3