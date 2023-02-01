#branch
#a = int(input("input number:"))
a = -1
if a < 0:
    print("小于0")
elif (a == 0):
    print("等于0")
else:
    print("大于0")

# if else 表达式
print("1 < 2") if 1 < 2 else print("1 > 2")

(print("1 < 2") if 1 < 2 else
print("1 < 2") if 1 < 2 else
print("1 < 2") if 1 < 2 else 
print("1 > 2"))

print("1 < 2") if 1 < 2 else \
print("1 < 2") if 1 < 2 else \
print("1 < 2") if 1 < 2 else \
print("1 > 2")

#loop
i = 3
while i:
    print(i)
    i -= 1

i = -4
while i:
    i += 1
    if i == -1: continue
    print(i)

while 1:
    i += 1
    print(i)
    if i == 3: break
else:
    print("not exec here")

for char in "hello":
    print(char)

sum = 0
for i in range(0, 10):
    sum += i
print(sum)