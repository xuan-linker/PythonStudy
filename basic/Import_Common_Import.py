# import and from...import
import sys

print('command line parameter:')
for i in sys.argv:
    print(i)

print(" -- ")
print("\n python path:", sys.path)

print(" -- ")

from sys import argv, path

print('path:', path)
