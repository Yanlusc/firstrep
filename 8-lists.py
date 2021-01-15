""" Lists
- are `indexed` (the order in which we enter the elements maters)
- are `mutable` (I can modify any element in the list)"""

x = ['abc', 8.87, 32]
y = ['sdflksdafj', 3, 25]

print(len(x))

# Add an element
x.append('add')

# Extend by another list
x.extend(y)                    # x = x + y

# Acces an element
print(x[3])

# Remove an element
print('Before x.pop()', x)
x.pop()         # remove the last element in the list
x.pop(3)        # remove element at index 4
x.remove('abc')
# if `True` is in the list 3 times it only removes
# it once and 2 `True` are left

# Replace an element
print('Element to replace', x[2])
x[2] = 'not ok'


# Copy a list
y = x   # this does not do a true copy
print('Element to replace', y[1])
y[1] = 'Sophie'
x.pop()
# list just store for the reference to the memory addresses of the elements
print(x, y)


z = x[:]    # True copy(new addresses in the memory with same values)
print('Element to replace', z[1])
z[1] = 'Jerome'
x.pop()
print(x, z)

# Lookups
print('Jerome' in z)
