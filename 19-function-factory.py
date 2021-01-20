def to_the_power(number):
    print('to_the_power')

    def nth_power(power):
        print('inner_func')
        return number ** power
    return nth_power


# I asked for the factory to make me a function
# `nth_power` with number=2
raise_two = to_the_power(2)
# Then I past another number to my fuction to set `power`value
print(raise_two(1))
# print(raise_two(2))
# print(raise_two(3))
# print(raise_two(4))

print('-'*29)

# I asked for the factory to make me a function
# `nth_power` with number=4
raise_four = to_the_power(4)
print(raise_four(1))
print(raise_four(2))
print(raise_four(3))

print('-'*29)

print(to_the_power(2)(6))
