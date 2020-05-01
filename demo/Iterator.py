testList = [1, 2, 3, 4]
it = iter(testList)
print(next(it))
print(next(it))

for x in it:
    print(x, end=" ")
print("----")

it = iter(testList)
for x in it:
    print(x, end=" ")
print("----")
##

import sys

list = [1, 2, 3, 4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
print("----")


##
