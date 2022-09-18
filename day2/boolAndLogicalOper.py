# bool
print(bool(2)) #True
print(bool("True")) #True
print(bool(" ")) #True
print(bool("")) #False
print(bool(0)) #False
a = None
print(bool(a)) #False
print(1 == True) #True
print(2 == True) #False
print(0 == False) #True

#Logical operations
print(True and False) #False
print(True or False) #True
print(not True) #False
# 以下结果由短路逻辑可以推导出
# 输出为最后一次运算的结果
print(2 and 0) #2
print("w" and 2) #w
print(0 and 2) #0
print(2 and 3) #3
print(2 or 0) #2
print("w" or 2) #w
print(0 or 2) #2
print(2 or 3) #2
