separator = 10*'-'
print(separator, 'Exo 1', separator)
x = [i for i in range(11)]
print(x)
print(separator*3)


print(separator, 'Exo 2', separator)
y = x[3:7]  # lorsqu'un slicing est effectué, celà copie tout les éléments
            # dans une nouvelle liste y
print(y)
print(separator*3)


print(separator, 'Exo 3', separator)
y[2] = 'Yannick'
print(x, y)
print(separator*3)


"Ajouter à y la liste z "
print(separator, 'Exo 4', separator)
z = [True, 'Hello', 9812, "No way!"]
y.append(z)
print(y)
print(separator*3)
print(separator, 'Exo 5', separator)
"ajouter 5000 à la liste y après 9812"
print(y[-1:])           # dont use slicing : to modify
print(y[-1:][0])        # dont use slicing : to modify
y[-1:][0].append(5000)  # dont use slicing : to modify
print(y[4])
y[4].append(5000)       # do this or with -1
y[-1].append(5000)      # or this

print(y)
print(separator*3)

"""adding list w in list """"
print(separator, 'Exo 6', separator)
w = [True, 'ABC', 8.443]
y[-1].append(w)
print(y)
print(separator*3)
