#永久储存
#file
fp = open("savet.txt", "w")
fp.write("abc")
fp.close()
fp = open("savet.txt", "r")
content = fp.read()
print(content)
fp.close()

#pathlib
from pathlib import Path
p = Path.cwd() #获取当前路径
print(p)
p = Path(p)
print(p.is_dir()) #判断是否是目录
print(p.is_file()) #判断是否是文件
print(p.exists())  #判断是否存在

ps = p.parents
for each in ps:
    print(each)

pt = p.parts
print(pt)

print(p.stat().st_size)

print(Path("./day13"))

print(Path("./day13").resolve())

#获取所有文件(不会递归展开)
p = Path(".")
for each in p.iterdir():
    print(each)

p = Path("savet1.txt")
if p.exists():
    p.unlink() #删除文件，删除目录是rmdir()
p = Path("./savet.txt")
f = p.open("w")
f.close()
p.rename("savet1.txt")

p = Path(".")
print(list(p.glob("*.txt"))) #查找
print(list(p.glob("*/*.py"))) #查找当前路径及子目录

#with
with open("savet.txt", "w") as f:
    f.write("savet")

#pickle
x, y, z = (1, 2, 3)
s = "savet"
l = [1, 2, 4]

import pickle
with open("savet.pkl", "wb") as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    pickle.dump(s, f)
    pickle.dump(l, f)

with open("savet.pkl", "rb") as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))