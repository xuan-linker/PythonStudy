# Dictionary like Java's map
dict = {}
dict['one'] = "1 - Linker"
dict[2] = "2 - xlccc"
testDict = {'name': 'linker', 'web': 'xlccc', 'macro': 'micro'}

print(dict['one'])
print(dict[2])
print(testDict)
print(testDict.keys())
print(testDict.values())

testDict = ([('Xlccc', 1), ('Google', 2), ('Taobao', 3)])
print(testDict)

testDict = {x: x ** 2 for x in (2, 4, 6)}
print(testDict)

testDict = ([('Xlccc', 1), ('Google', 2), ('Taobao', 3)])

testDict2 = dict.fromkeys(testDict)
print(testDict2)

testDict2 = testDict.copy()
print(testDict2)

testDict = ([('Xlccc', 1), ('Google', 2), ('Taobao', 3)])

# print(testDict.get('Xlccc'))


print("---")
dict.setdefault("hello", "world")
testDict = dict
print(testDict)

testDict.clear()
print(testDict)
