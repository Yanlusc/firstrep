def func():
    print('Run')


def func_with_params(x, y):
    print(x, y)
    return x*y


def func_with_inner():
    print('Run')

    def inner_func():           # can only be called in `func_with_inner`
        print('Hello!')         # because it is local to `func_with_inner`
        return True
    return inner_func()


func_with_inner()
