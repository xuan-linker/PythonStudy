student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)

if 'Rose' in student:
    print("in")
else:
    print("not in")

# calculate for set
a = set('abcdefg')
b = set('efghijk')

print(a)
# include a and not include b
print(a - b)
# include a and include b
print(a | b)
# at the same time in a and b
print(a & b)
# include a and include b but except at the same time in a and b
print(a ^ b)
