x = 8
y = 3
z = 9

result1 = x == y        # False
result2 = y > 0         # True
result3 = z < x + 2     # False

result4 = result1 or result2 or result3
# if there is a true between the or it displays true
print(result4)

print('not False', not False)
print('not False', not False)
print('not (True or False)', not (True or False))
print('not (True and False)', not (True and False))
print('not (False and True or False)', not (False and True or False))

result5 = not (False and True or False and not False)
print('not (False and True or False and not False)', result5)

# Which comes first?
# not -> and  -> or             Ordre des priorités lors des opérations
