"""
if else
"""
if True:
    print("True")
else:
    print("false")
'换行符'
total = "item_one + \
        item_two + \
        item_three"
print(total)

total = ['item_one', 'item_two', "item_three",
         'item_four']
print(total)
"""
基本类型
"""
a = 1
print(a)

a = True
print(a)

a = 1.32
print(a)

a = 1 + 2j
print(a)

# 字符串相同
a = "hello"
b = 'hello'
if a == b:
    print("a==b")
else:
    print("a!=b")

# 字符串String
world = '字符串'
sentence = "This is sentence."
paragraph = """This is 
paragraph.
do you know?"""
print(world)
print(sentence)
print(paragraph)

# print string

str = "Hello World!"

print(str)
print(str[0: -1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + 'Linker')
print("---------")
print('hello\nworld!')
print(r'hello\nworld')

# input("\n\n按下enter键后退出")

# import sys;x = "helloworld";sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print("--------")
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()
