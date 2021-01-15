""" What is the main difference between a `While` and `For...loop`
- `For loop` runs a predictable number of times
- `While loop` runs an undedined number of times
 """

for i in range(10):     # `range(10)` is equivalent `range(0, 10)`
    print(i)

for i in [21, 23, 5, 23, 239, 23, 'ygfcg', 23409, 97]:
    print(i)

x = [2, 5, 32, 98, 676]
for i in x:
    print(i)

"""
Imprimer une liste avec son index
"""

for i in range(len(x)):     # Avoid this
    print(i, x[i])

for i in range(len(x[3:])):     # Avoid this
    print(i+3, x[i+3])

for i, element in enumerate(x):     # Do this instead
    print(i, element)

for i, element in enumerate(x[3:], 3):      # Do this instead
    print(i, element)


y = (23, 42, 7093, 783, 23)

for i, element in enumerate(y[1:-2], 1):    # for i, element in enumerate(y[1:len(y)-2], 1):
    print(i, element)
