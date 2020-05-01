n = 100

sum = 0
counter = 1

while counter <= n:
    sum = sum + counter
    counter += 1

print(sum)

##

# var = 1
# while var == 1:
#     num = int(input("please input a number:"))
#     print("your number :", num)
#
# print("Good bye!")

count = 0
while count < 5:
    print(count, "less than 5")
    count += 1
else:
    print(count, "great than or equal to 5")

flag = 1

while flag:
    print("welcome to xlccc")
    break

print("good bye")

##

for i in range(5):
    print(i, end=" ")
print("\n")

for i in range(5, 9):
    print(i, end=" ")
print("\n")

for i in range(0, 10, 3):
    print(i, end=" ")
print("\n")

for i in range(-10, -100, -30):
    print(i, end=" ")
print("\n")

##
a = ['Google', 'Baidu', 'Xlccc', 'Taobao', 'QQ']

for i in range(len(a)):
    print(i, a[i])
print("\n")

##
testList = list(range(5))
print(testList)

##
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("end")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("end")

##

for letter in 'xlccc':
    if letter == 'c':
        break
    print("now byte=", letter)

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print("now byte:", var)
print("good bye")

# prime number

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break
    else:
        print(n, "is prime number")

# pass do nothing

for letter in 'xlccc':
    if letter == 'c':
        pass
        print("run pass")
    else:
        print(letter + " ")
print("end")
