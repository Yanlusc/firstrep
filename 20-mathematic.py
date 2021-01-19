def operation(type_op):
    def sommation(x, y):        # sum
        return x+y

    def substract(x, y):        # sub
        return x-y

    def multiplication(x, y):   # mult
        return x*y

    def division(x, y):         # div
        return x/y

    def wtf(x, y):
        s = sommation(x, y)
        ss = substract(x, y)
        mult = multiplication(x, y)
        d = division(x, y)
        return s, ss, mult, d

    if type_op == 'sum':
        return sommation
    if type_op == 'sub':
        return substract
    if type_op == 'mult':
        return multiplication
    if type_op == 'div':
        return division
    if type_op == 'op':
        return wtf


print(operation('sum')(2, 4))
print(operation('sub')(2, 4))
print(operation('mult')(2, 4))
print(operation('div')(2, 4))
print(operation('op')(2, 4))
