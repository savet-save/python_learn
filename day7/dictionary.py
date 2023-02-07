d = {"qwe":2, "rty":"q", 5:"abc"}
print(d[5])

c = dict(qwe=2, rty="q", abc=5)
print(c["rty"])

print(dict([("qwe", 2), ("rty", "q"), (5, "abc")]))

print(dict(d , trq="w"))

print(dict(zip(["qwe", "rty", 5], [2, "q", "abc"])))

print(dict.fromkeys("savet", 6))

#删除
d = {"qwe":2, "rty":"q", 5:"abc"}
print(d.pop("qwe"))

d = {"qwe":2, "rty":"q", 5:"abc"}
print(d.popitem())

d = {"qwe":2, "rty":"q", 5:"abc"}
del d["qwe"]
print(d)

print(dict.fromkeys("savet", 6).clear())