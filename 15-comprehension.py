x = []

print(28*'-')
print(dir(x))       # print all the functions available for the object x
print(28*'-')

for i in range(5):
    x.append(i)        # to add in a list we ALWAYS USE APPEND

y = [i for i in range(5)]
print('-'*28)
z = [i*10 for i in x if i % 2 == 0]

print(28*'-')
print(x, y)
print(28*'-')
