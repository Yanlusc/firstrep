x = []

print(28*'-')
print(dir(x))       # print all the functions available for the object x
print(28*'-')

for i in range(5):
    x.append(i)        # to add in a list we ALWAYS USE APPEND

y = [i for i in range(5)]
print('-'*28)
z = [i*10 for i in x if i % 2 == 0]
print(z)
print(28*'-')

print(28*'-')
print(x, y)
print(28*'-')

print(28*'-')
w = [i for i in range(1, 21) if i % 3 == 0]
print(w)
print(28*'-')
print(28*'-')
d = sum(i*2 for i in range(200) if i % 19)
print(d)
print(28*'-')

print(28*'-')


def mask_numbers(i):
    # return i if i % 2 == 0 else len(str(i))*'x'
    if i % 2 == 0:
        return i
    else:
        return len(str(i))*'x'


p = [mask_numbers(i) for i in range(1000) if i % 19 == 0]
print(p)
print(28*'-')


print(28*'-')
tuple_comprehension = tuple(i for i in range(5))          # sans le tuple créer un generator et pas un tuple{}
print(tuple_comprehension)
print(28*'-')

print(28*'-')
set_comprehension = {i for i in range(5)}
print(set_comprehension)
print(28*'-')


print(28*'-')
dict_comprehension = {'x'*i: i for i in range(5)}
dict_comprehension2 = {'x'+str(i): i for i in range(5)}
print(dict_comprehension)
print(dict_comprehension2)
print(28*'-')


print(28*'-')
# 10 pairs of key-value with the value set to 0
# keys as an unique alphabet letter
dico = {chr(i): 0 for i in range(ord('a'), ord('a')+10)}
print(dico)

print(28*'-')
