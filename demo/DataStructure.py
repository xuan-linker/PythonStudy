a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

# a.index(333)
print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

# use list as stack
stack = [3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

# use list as queue
from _collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

# 列表推导式
vec = [2, 4, 6]
vec2 = [3 * x for x in vec]
print(vec)
print(vec2)

vec3 = [3 * x for x in vec if x > 3]
print(vec3)

vec4 = [str(round(355 / 113, i)) for i in range(1, 6)]
print(vec4)

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)

matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

del a[0]
print(a)

del a[2:3]
print(a)

del a[:]
print(a)

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3)
print(u)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
