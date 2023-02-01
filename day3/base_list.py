list = [1, 2, 3, 4, "5"]
print(list[2])
print(list[-1]) 

print(list[1:3])
print(list[:2])
print(list[3:])
print(list[1:4:2])

#添加
list.append("6")
print(list)

list.extend(["6"])
print(list)

list[len(list):] = ["6"]
list[len(list):] = ["7", "8", "9"]
print(list)

list = [1, 2, 3, 4, "5"]
list.insert(0, 20)
print(list)

#删除
list.remove(1)
print(list)

list.clear()
print(list)

#修改
list = [1, 2, 3, 4, "5"]
list[2] = 30
print(list)

list = [1, 2, 3, 4, "5"]
list = [1, 2, 3, 4, "5"]
list[3:] = [5, "6", "10"]
print(list)

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