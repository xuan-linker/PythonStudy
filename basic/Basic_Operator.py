a = 21
b = 10
c = 0

c = a + b
print("1 - c result:", c)

c = a - b
print("2 - c result:", c)

c = a * b
print("3 - c result:", c)

c = a / b
print("4 - c result:", c)

c = a % b
print("5 - c result:", c)

a = 2
b = 3
c = a ** b
print("6 - c result:", c)

# 	取整除 - 向下取接近商的整数
a = 10
b = 5
c = a // b
print("7 - c result:", c)

print("----")
c = 10
a = 8
c //= a
print("8 - c result:", c)

print("---")
testList = [1, 2, 3, 4, 5]
count = len(testList)
if count > 3:
    print(f"Error , {count} is too many items")

# :=
if (count := len(testList)) > 3:
    print(f"Error,{count} is too many items")

# byte calculate

a = 0o0111100
b = 0o0001101

c = a & b
print("1 - c 的值：", c)

c = a | b
print("2 - c 的值：", c)

c = a ^ b
print("3 - c 的值：", c)

c = ~a
print("4 - c 的值：", c)

c = a << 2
print("5 - c 的值：", c)

c = a >> 2
print("6 - c 的值：", c)

# and or not

a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

a = 0

if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# is and ==
# is  用于判断两个变量 引用对象 是否为同一个，
# == 用于判断引用变量的 值 是否相等。
a = [1, 2, 3]
b = a

print(a is b)
print(a == b)

print("---")
b = a[:]

print(b is a)
print(b == a)

print("---")
# and 优先级更高
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
