#元组
tuple1 = (1, 2, 3, "4")
tuple2 = 5, 6, 8, "1"
print(tuple1)
print(tuple2)

tuple1 = (1, 2, 3, "4")
tuple1 = (3 , 5, 6)
print(tuple1)

#切片
tuple1 = (1, 2, 3, "4")
tuple2 = tuple1[::2]
tuple3 = tuple1[:3]
print(tuple2)
print(tuple3)

#方法
#计数
tuple1 = (1, 2, 3, "4", 3)
print(tuple1.count(3))

#查找索引
tuple1 = (1, 2, 3, "4", 3)
print(tuple1.index(2))

#嵌套
tuple1 = ((1, 2), (3, 4))
print(tuple1)

#单元素
tuple1 = (1, )
print(type(tuple1))

#打包与解包
t = (123, "Savet" , 233)
x, y, z = t
print(x)
print(y)
print(z)

t = (123, "Savet" , 233)
x, *y = t
print(x)
print(y)