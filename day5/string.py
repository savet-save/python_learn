#字符串
str1 = "I am Savet"

#大小写转换
print(str1.capitalize())
print(str1.casefold())
print(str1.title())
print(str1.swapcase())
print(str1.lower())
print(str1.upper())

#对齐
str1 = "Savet"
print(str1.center(20))
print(str1.ljust(20))
print(str1.rjust(20))
print(str1.zfill(20))
print('1')

#查找
str1 = "adbjdaqwe"
print(str1.count("a"))
print(str1.count("a", 0, 2))

print(str1.find("a"))
print(str1.rfind("a"))

#替换
str1 = """123
\t123
    233"""
print(str1.expandtabs(4))

str1 = "abcabc"
print(str1.replace("ab", "de"))

str1 = "abcabc"
print(str1.translate(str.maketrans("abcdefg", "1234567")))

#判断
str1 = "1234"
print(str1.startswith("1"))
print(str1.startswith("1", 1))
print(str1.startswith(("1", "2", "3"), 1))

num = "5678"
print(num.isdecimal())
print(num.isdigit())
print(num.isnumeric())
print("α".isalpha())

print("aa bb".isidentifier())

import keyword
print(keyword.iskeyword("while"))

str1 = "   123"
print(str1.lstrip())
str1 = "qwew.123.fwqr"
print(str1.strip("qwr"))

#拆分
str1 = "www.baidu.com"
print(str1.partition(".b"))

str1 = "www.baidu.com"
print(str1.split("."))

#拼接
str1 = ".".join(["www", "baidu", "com"])
print(str1)

#格式化字符串
year = 2023
str1 = "现在是 {} 年".format(year)
print(str1)

year, mon = (2023, 2)
str1 = "现在是 {1} 年 {0} 月".format(mon, year)
print(str1)

str1 = "现在是 {y} 年 {m} 月".format(m="2", y="2023")
print(str1)

print("1{{}}2".format())

#以货币形式显示
print("货币形式：{:,d}".format(1000000))
#科学计数法表示
print("科学计数法：{:E}".format(1200.12))
#以十六进制表示
print("100的十六进制：{:#x}".format(100))
#输出百分比形式
print("0.01的百分比表示：{:.0%}".format(0.01))

#f字符串
year = 2023
str1 = f"现在是 {year} 年"
print(str1)  #现在是 2023 年