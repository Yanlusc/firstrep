x = [2, 532, 23, 97, 96, 9890]

i = 0
s = ''
while True:
    print('run')
    i += 2      # this is the equivalent of `i = i + 2`
    i -= 1
    i *= 2      # this is the equivalent of `i = i * 2`
    i /= 2
    s += 'd'
    print(s)
    if i == 3:
        break

j = 0
while True:
    print('run first while loop')
    j += 1
    while True:     # the `break` only stop the loop that is was called in
        print('run second while loop')
        j *= 2
        if j > 4:
            print('time to quit')
            break

