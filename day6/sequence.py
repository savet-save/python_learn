#+
print("123" + "567")
print((1, 2, 3) + (4, 5, 6))
print([1, 2, 3] + [4, 5, 6])

#*
print("123" * 3)
print((1, 2, 3) * 3)
print([1, 2, 3] * 3)

s = [1, 2, 3]
print(id(s))
s = s * 2
print(id(s))

t = (1, 2, 3)
print(id(t))
t = t * 2
print(id(t))

z = "14"
q = z + "24"
print(z is q)
print(z is not q)

print("s" in "savet")
print("c" not in "savet")

w = "aa"
del w
#print(w)

x = [1, 2, 3, 4, 5]
del x[1:2]
print(x)

y = [1, 2, 3, 4, 5]
del y[:]
print(y)

#get list
print(list("qwe"))
print(list(("q", "w", "e")))

#get tuple
print(tuple("qwe"))
print(tuple(["q", "w", "e"]))

#get string
print(str(["q", "w", "e"]))
print(str(("q", "w", "e")))

print(min([1, 2, 3, 4, 5]))
print(max("savet"))
print(min(1, 2, 3, 4, 5))
print(max(1, 2, 3, 4, 5))

print(sum((1, 2, 3)))

print(sorted([5, 2, 9, 1]))
print(sorted((5, 2, 9, 1)))

print(list(reversed([1, 2, 3, 4])))

print(all([1, 1, 0]))
print(any([1, 1, 0]))

print(list(enumerate(["qwe", "rty", "uio"])))

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3, 4], [4, 5, 6])))
import itertools
print(list(itertools.zip_longest([1, 2, 3, 4], [4, 5, 6])))

print(list(map(ord, "savet")))

print(list(filter(str.islower, "Savet")))

print(type(iter([1, 2, 3])))

print(next(iter([1, 2, 3])))
