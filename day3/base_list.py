list1 = [1, 2, 3, 4, "5"]
print(list1[2])
print(list1[-1]) 

print(list1[1:3])
print(list1[:2])
print(list1[3:])
print(list1[1:4:2])

#添加
list1.append("6")
print(list1)

list1.extend(["6"])
print(list1)

list1[len(list1):] = ["6"]
list1[len(list1):] = ["7", "8", "9"]
print(list1)

list1 = [1, 2, 3, 4, "5"]
list1.insert(0, 20)
print(list1)

#删除
list1.remove(1)
print(list1)

list1.clear()
print(list1)

#修改
list1 = [1, 2, 3, 4, "5"]
list1[2] = 30
print(list1)

list1 = [1, 2, 3, 4, "5"]
list1 = [1, 2, 3, 4, "5"]
list1[3:] = [5, "6", "10"]
print(list1)

#其他方法
#排序
num = [1, 0, 20, -2, 4]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

#反转
num = [1, 0, 20, -2, 4]
num.reverse()
print(num)

#计数
num = [1, 1, 2, 2, 3, 2]
print(num.count(2))

#查找
num = [1, 1, 2, 2, 3, 2]
print(num.index(2))

#拷贝
nums = [1, 1, 2, 2, 3, 2]
nums_copy1 = nums.copy()
nums_copy2 = num[:]
nums_copy3 = num[2:]
print(nums_copy1)
print(nums_copy2)
print(nums_copy3)