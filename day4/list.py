#拼接
s = [1, 2, 3]
t = [4, 5, 6]
print(s + t)
b = [s , t]
print(b)

#重复
print(s * 3)

#嵌套
list1 = [[1, 2, 3], [2, 3], [5]]
print(list1)
list1 = [[1, 2, 3], 
        [2 , 3],
        [5]]
print(list1)

#嵌套重复
#错误的创建
list1 = [[0] * 3] * 3
list1[0][0] = 1
print(list1)

#正确的创建
list1 = [0] * 3
for i in range(len(list1)):
    list1[i] = [0] * 3
list1[0][0] = 1
print(list1)

#拷贝
#引用拷贝（仅拷贝地址）
list1 = [1, 2, 3]
list2 = list1
list1[1] = 0
print(list2)

#浅拷贝（只拷贝一层）
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = list1.copy()
list1[1][1] = 0
print(list2)

import copy
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = copy.copy(list1)
list1[1][1] = 0
print(list2)

#深拷贝（完全拷贝）
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = copy.deepcopy(list1)
list1[1][1] = 0
print(list2)

#列表迭代器
list1 = [i for i in range(10)]
print(list1)

list1 = [ord(i) for i in "Savet"]
print(list1)

#条件列表迭代器
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

#嵌套列表迭代器
list1 = [i * k for i in range(10)
        for k in range(2)]
print(list1)

#嵌套条件列表迭代器
list1 = [i * k for i in range(10) if i % 2 == 0
        for k in range(4) if k % 2 == 1]
print(list1)

#打包与解包
list1 = [1, 2, 3]
x, y, z = list1
print(x)
print(y)
print(z)

l = [123, "Savet" , 233]
x, *y = l
print(x)  #123
print(y)  #['Savet', 233]