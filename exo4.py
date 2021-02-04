# s = f'{[i for i in [3, 234, 23, 987] if i%3==0]}

s = [3, 21, 23, 987]

d = filter(lambda i: i % 3 == 0, s)
print(list(d))
