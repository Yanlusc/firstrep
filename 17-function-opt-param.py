
def func(x, y, z=None):
    print('Run', x, y, z)
    return x*y

a = func(3, 12)
b = func(3, 89, 'Genial')