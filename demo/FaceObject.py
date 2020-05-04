class MyClass:
    i = 123

    def f(self):
        return "hello world"


x = MyClass()

print(x.i)
print(x.f())


class MyClass2:
    def __init__(self, data):
        print("init")
        self.data = 123


x = MyClass2(2)
print(x.data)
print(x.__class__)
