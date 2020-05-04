import math
import sys

s = "Hello,Linker"
str(s)

print(repr(s))
print(str(s))
# str()： 函数返回一个用户易读的表达形式
# repr()： 产生一个解释器易读的表达形式
# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

path = "/Users/linkp/linker/python/StudyRunoob/foo.txt"
f = open(path, "w")
f.write("hello world txt\n")
f.close()

f = open(path, "r")
str = f.read()
print(str)
f.close()

f = open(path, "r")
str = f.readline()
print(str)
f.close()

f = open(path, "w")
num = f.write("aaaaaaaaa 阿斯顿\n")
print(num)
f.close()

f = open(path, "w")
value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
f.close()
