n = int(input('entrer le nombre n'))


def rec(n):
    if n < 1:
        return 1
    result = n * rec(n-1)
    print(str(n) + "! = " + str(result))
    return result


print(rec(n))
