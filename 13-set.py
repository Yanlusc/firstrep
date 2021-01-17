""" A set:
- is a `not ordered` collection (you cant keep track of elements)
- unique elements (no duplicates -> no frequency of elements)
- extremely fast to do lookups, removals, additions.
You want to a set when all you care is to know if something is there or not.
When we talk about removing an element `1` from a list `[2, 3, 3, 1 , 7 , 43]`
the actually involves `shifting` the position of all the other element after
that element and keeping track of all remaing elements.
`Shifting` takes is a task that takes as much time as
the length of the element.
- Set execution happens in constant time (extremely fucking fast)
"""

# declare a set
x = set()               # This is the only way to create an empty
s = {2, 3, 45, 'David', 53, 3}   # This is known as a set literal
not_a_set = {}          # This does not create a set, it is an empty dictionary
print(type(not_a_set))

# Add an element
print('\nAdd an element\n')
print('Before addition', s)
s.add('Bonjour')
print('After addition', s)

# Remove an element
print('\nRemove an element\n')
print('Before remove', s)
s.remove('David')
print('After remove', s)


# Union
print('\nUnion\n')
s2 = {2, 'Yan', 298, 3, 53}
print(s, s2)
print(s.union(s2))             # This doesn't modify the initial set, it just displays a result
print(s, s2)

# Difference outer join left
print('\nDifference\n')
print(s, s2)
print(s.difference(s2), s2.difference(s))  # This doesn't modify the initial set, it just displays a result
print(s, s2)

# Intersection
print('\nIntersection\n')
print(s, s2)
print(s.intersection(s2))      # This doesn't modify the initial set, it just displays a result
print(s, s2)

# Fist way to Merge two sets
print('\nFist way to Merge two sets\n')
print('Before merge 1 way', s, s2)
s |= s2
print('After merge 1 way', s)

# Second way to Merge two sets
print('\nSecond way to Merge two sets\n')
s3 = {'987', 98789798, True}
print('Before merge 2 way', s2, s3)
s2.update(s3)
print('After merge 2 way', s2)

# Third way to Merge two sets
print('\nThird way to Merge two sets\n')  # What the fuck!
import operator
from functools import reduce
ss4 = {2, 3, 4, 5}
ss6 = {6, 7, 9, 8}
print(reduce(operator.or_, [ss4, ss6]))
print(ss4, ss6)
