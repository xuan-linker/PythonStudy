# condition

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

age = int(input("please input your dog's age:"))
print("")
if age <= 0:
    print("are you kidding")
elif age == 1:
    print("the same as people's 14 years old")
elif age == 2:
    print("the same as people's 22 years old")
elif age > 2:
    humanAge = 22 + (age - 2) * 5
    print("the same as human' age :", humanAge)

num = int(input("please input a number"))
if num % 2 == 0:
    if num % 3 == 0:
        print("your number can divide by 3 and 2")
    else:
        print("your number can divided by 2 , but can't divided by 3")
else:
    if num % 3 == 0:
        print("your number can divided by 3 but can't divided 2")
    else:
        print("your number can't divided by 2 or 3")
