import sys

print("command args :")
for i in sys.argv:
    print(i)

print("\n\nPython path:", sys.path, "\n")

if __name__ == '__main__':
    print("main run")
else:
    print("from other module")

dir(sys)
print(dir(sys))

print(dir())
