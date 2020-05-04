while True:
    try:
        x = int(input("please input a number:"))
        break
    except ValueError:
        print("your input not number , please try again")

import sys

try:
    # raise Exception("error exception")
    f = open('myfile,txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("cloud not convert data to a integer")
except:
    print("Unexpected error", sys.exc_info()[0])
    raise
else:
    print("1")
finally:
    print('2')


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print("MyError value:", e.value)
