x = 'David'


def func_mod_local(name):
    x = name


def func_mod_global(name):
    global x    # the global value x='David' is accessed
    # and modify by x Yan contained inside the function func
    x = name


print('Before x mod:', x)
func_mod_local('Yan')
print('After x mod:', x)
