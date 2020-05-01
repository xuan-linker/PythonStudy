# Tuple (元组) the same as list but different with this can't change
testTuple = ('abc', 123, 4.56, 'Linker', 12.2)
testTuple2 = ("asd", 22)

print(testTuple)
print(testTuple[0])
print(testTuple[1:3])
print(testTuple[2:])
print(testTuple * 2)
print(testTuple + testTuple2)

# empty tup
tup1 = ()
print(tup1)
# just one member for tup need ,
tup2 = (1,)
print(tup2)


