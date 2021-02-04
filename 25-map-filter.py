x = [12, 21, 43, 53, 897, 987, 87, 89, 90809812982]


def f(param):
    return param*2


mp = map(lambda i: i*2, x)
mp2 = map(f, x)


mp3 = map(lambda i: i % 2 == 0, x)
ft = filter(lambda i: i % 2 == 0, x)

print(list(mp))
print(list(mp2))
print(list(mp3))
print(list(ft))
