# Fibonacci
a, b = 0, 1
while a < 10:
    print(b)
    a, b = b, a + b

a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a + b
