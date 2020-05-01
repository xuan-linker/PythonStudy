counter = 100
miles = 1000.0
name = "Liner"

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, "Liner"
print(a, b, c)

# Number
a, b, c, d = 10, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# if a's type equals int
print(isinstance(a, int))

print("-----")


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)

# isinstance() compare with son() as father's type
print(isinstance(B(), A))  # True

# type() don't compare with son() as father's type
print(type(B()) == A)  # False

# release object
del A
del B
# print(A)

# calculate

print(5 + 4)

print(2.2 - 1)

print(3 * 2)

print(2 / 5)
# division method get floor
print(2 // 5)
print(2 // 3)
print(2 // 10)

print(29 % 3)
# power
print(2 ** 5)

str = 'Runoob'

print(str)  # 输出字符串

print(str[0:-1])  # 输出第一个到倒数第二个的所有字符

print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST")  # 连接字符串

# List
testList = ['a', 'b', 'c', 'd', 'e']
print(testList)
print(testList[0])
print(testList[1:3])
print(testList[2:])
print(testList * 2)

# change list content
testList[0] = 1
print(testList)

testList[2:3] = ['w', 'ww']
print(testList)

testList[3:] = []
print(testList)


