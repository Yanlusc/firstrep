x = 0
y = 6

if x > y:                      # F
    print('x > y: yes')


if y > x:                      # T
    print('y > x : yes')


if x:                          # F
    print('x yes')


if y:                          # T
    print('y yes')


if x and y:                   # 2 et 7
    print('x and y: yes')

if y:
    if x:
        print('chained')


if x & y:                      # `AND Bitwise` 2->010  7->111
    print('x & y yes')
    # &, |, ~, ^, >>, << all bitwise opperation


if y or x:                     # un des deux est positif donc c'est un True
    print('y or x yes')

if y:
    print('y or x yes')

if x:
    print('y or x yes')


if 'ry' in 'bryan':            # T
    print('bryan yes')


if 'daaab' in ['dkow', 'lksjdfsdjfk', 'dappp', 'klsjdfkdjsf']:      # F
    print(' daaab yes')
