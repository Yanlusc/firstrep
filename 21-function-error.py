
def factorial(n):
    # error management
    if not isinstance(n, int):
        raise TypeError('Sorry, the number you past is not an Integer.')
    if not n >= 0:
        raise ValueError('Sorry, the number must be zero or positive.')

    def inner_factorial(n):             # wrapper for our bussiness logic
        if n <= 1:
            return 1
        return n*inner_factorial(n-1)
    return inner_factorial(n)


print(type(True))
print(isinstance(True, int))
print(factorial(True))
print(factorial(3))
print(factorial('fsd'))     # TypeError raised
print(factorial(8))
print(factorial(-3))        # ValueError raised
