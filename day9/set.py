#集合 - set
print(type("set"))
#error
#print(type("set", "set"))

s = {i for i in "range(10)"}
print(s)

print(set("savet"))

s = set("savet")
for i in s:
    print(i)

#唯一性
#去重
print(set([1, 1, 2, 2, 3]))

#判断是否有重复元素
li = [1, 2, 3, 3, 4]
print(len(li) == len(set(li)))

#浅拷贝
s = {1, 2, 3}
print(s.copy())

#是否是互斥
s1 = {1, 2, 3, 4}
s2 = {11, 5, 6, 7, 10}
print(s1.isdisjoint(s2))
print(s1.isdisjoint([1, 2, 3]))

#是否是子集
s = {1, 2}
print(s.issubset([11, 2, 3]))
print(s.issubset({1, 2, 3}))
print(s <= {1, 2, 3}) #True
print(s < {1, 2}) #False

#是否是超集
s = {1, 2, 3, 4, 5}
print(s.issuperset([11, 2, 3]))
print(s.issuperset({1, 2, 3}))
print(s >= {1, 2, 3}) #True
print(s > {1, 2}) #True
#error
#print(s > [1, 2])

#并集
s = {1, 2, 3}
print(s.union({3, 4, 5}))
print(s | {3, 4, 5})

#交集
s = {1, 2, 3}
print(s.intersection({3, 4, 5}))
print(s & {3, 4, 5})

#差集
s = {1, 2, 3}
print(s.difference({3, 4, 5})) #{1, 2}
print(s.difference({3, 4, 5}, {1, 6, 7, 8}))
print(s - {3, 4, 5}) #{1, 2}

#对称差集
s = {1, 2, 3}
print(s.symmetric_difference({3, 4, 5}))
print(s ^ {3, 4, 5}) #{1, 2, 4, 5}

#不可变集合
fz = frozenset("savet")
print(fz)

#修改（不能修改frozenset)，并集添加
s = {1, 2, 3}
s.update([5], "savet")
print(s)
#error
#frozenset("savet").update([2])

#交集添加
s = {1, 2, 3}
s.intersection_update([5], "savet")
print(s)

#差集添加
s = {1, 2, 3}
s.difference_update([5], "savet")
print(s)

#对称差集添加
s = {1, 2, 3}
s.symmetric_difference_update([5])
print(s)

#添加
s = {1, 2, 3}
s.add("123")
s.add(5)
print(s)

#删除
s = {1, 2, 3}
s.remove(1)
print(s)
s.discard(9) #不会抛出异常，如果删除的元素不存在
print(s)

#弹出
s = {1, 2, 3}
l = len(s)
for i in range(l):
    print(s.pop())
print(s)

#清空
s = {1, 2, 3}
s.clear()
print(s)

#哈希
print(hash(1))
#errop
#{[1,2]:[1, 2]}
#{[1, 2]}

#集合的嵌套
print({frozenset([1, 2, 3]), 4, 5})