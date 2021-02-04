import traceback


def fact(n):
    # verify n and raise error of not valid
    if not isinstance(n, int):
        raise TypeError("Wrong parameter type it must be an integer")
    if n < 0:
        raise ValueError("the value must be superior to 0 ")

    def inner_fact(n):
        if n <= 1:
            return 1
        else:
            return n * fact(n-1)

    return inner_fact(n)


try:
    print(fact(-5))
except ValueError:          # ValueError take only the argument of raise ValueError
    print("Merde! "*20)
    traceback.print_exc()   # Give the error message
except Exception:           # Except addresses all types of errors
    traceback.print_exc()
finally:
    print('Finally!')

print(fact(9))      # the finaly is always executed even if excep is not executed
