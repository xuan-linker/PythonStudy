def hello():
    print("Hello world!")


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


# mutable and immutable object
# mutable : list,dict
# immutable : strings,tuples,numbers
def change_int(a):
    a = 10


def change_me(myList):
    myList.append([1, 2, 3, 4])
    print("function values:", myList)
    return


def print_me(str):
    print(str)
    return


def print_info(name, age):
    print("name:", name)
    print("age:", age)
    return


def print_info(name, age=20):
    print("name:", name)
    print("age:", age)
    return


def print_info_args(arg1, *vartuple):
    print("print:")
    print(arg1)
    print("---")
    print(vartuple)


# *value means tuple
def print_info_args2(arg1, *vartuple):
    print("print:")
    print(arg1)
    for var in vartuple:
        print(var)
    return


def print_info_args3(arg1, **vardict):
    print("print:")
    print(arg1)
    print(vardict)


hello()
print_welcome("Linker")
print("area:", area(10, 20))

b = 2
change_int(b)
print(b)

myList = [10, 20, 30]
change_me(myList)
print("out values:", myList)

# must input values
print_me("11")

print_me(str="123")

print_info(age=20, name="Linker")

print_info(age=30, name="hello")
# default value age = 20
print_info(name="ww")

print_info_args(10, 23, 44, 55)

print_info_args2(10, 23, 44, 55)

print_info_args3(1, a=2, b=3)

# lambda to build a function
sum = lambda arg1, arg2: arg1 + arg2

print("sum1:", sum(1, 2))
print("sum2:", sum(10, 2))


# / : a,b must use designated spot
# * : e,f must use arg=value
def print_f(a, b, /, c, *, e, f):
    print(a, b, c, e, f)


print_f(1, 2, 3, e=2, f=3)
