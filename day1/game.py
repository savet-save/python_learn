# 用 Python 设计第一个游戏
"""
temp = input("请猜数字:")
guess = int(temp)

if guess == 8:
    print("猜中了！")
else:
    print("猜错了，我想到是8")

print("游戏结束")
"""

# 改进版本
import random

counts = 3
while counts > 0:
    value = random.randint(1, 10)
    temp = input("请猜数字:")
    guess = int(temp)
    if guess == value:
        print("猜中了！")
        break
    else:
        if guess < value:
            print("小了")
        else:
            print("大了")
    counts -= 1

print("游戏结束，值为" + str(value))