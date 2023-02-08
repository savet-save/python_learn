#字典part2
#修改
d = {"qwe":2, "rty":"q", 5:"abc"}
d["qwe"] = 3
print(d["qwe"])

d = {"qwe":2, "rty":"q", 5:"abc"}
d.update({"qwe":3, "rty":"w"})
print(d)

d.update(qwe=4, rty="e")
print(d)

#查找
d = {"qwe":2, "rty":"q", 5:"abc"}
print(d["qwe"])

d = {"qwe":2, "rty":"q", 5:"abc"}
print(d.get("weq"))

d = {"qwe":2, "rty":"q", 5:"abc"}
d.setdefault("weq")
print(d)

d = {"qwe":2, "rty":"q", 5:"abc"}
key = d.keys()
value = d.values()
item = d.items()
print(key)
print(value)
print(item)

d.pop("qwe")
print(key)
print(value)
print(item)

#拷贝
d1 = {"qwe":2, "rty":"q", 5:"abc"}
d2 = d1.copy()
print(d2)

#转换
d = {"qwe":2, "rty":"q", 5:"abc"}
print(list(d))
print(list(d.values()))

#迭代
d = {"qwe":2, "rty":"q", 5:"abc"}
for i in iter(d):
    print(i, end=" ")
print()

#嵌套
myClass = {"wqh" : {"arg":12, "svc":20}, "ygy":{"arg":11, "svc":8}}
print(myClass)

#字典推导式
d1 = {"qwe":2, "rty":"q", 5:"abc"}
d2 = {v:k for k,v in d1.items()}
print(d2)

d2 = {k:j for k,v in d1.items() for j,z in d1.items()}
print(d2)