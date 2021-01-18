""" Dictionaries
- have 'Unique' keys
- they are very fast because they use something called a `Hash`. That is a reason
why they effective pour retrieve. You can assume dictionary execution time happens
in `constant time` although there is a chance that there something called
`hash collision`. -> Good luck understand `hash collision` concept
"""


def power(x, y):
    return x ** y


x = {'abc': 'pop', 'lol': [1, 2], 1: True, 'set': {
    1, 'j', 'o'}, 'tup': ('Bryan', 'Yannick'), 0: 'salkdf;jsadl;fk',
    'bol_cond': True or False, 'power_opp': power}


# Acces variable
# print(x['set'])
# print(x[False])     # =print(x[0])
# print(x[True])      # =print(x[1])
# print(x['bol_cond'])
# print(x)
# print(x['power_opp'])
# print(x['power_opp'](2, 3))

# # Replace
# x['abc'] = 'popculture'

# # Inner element modification
# x['lol'].append(888)
# x['lol'][1] = 'Yannick'
# print(x)
# x['lol'].pop(0)

# # Add
# x['vitesse'] = '399km/h'
# print(x)
# x['vitesse'] = '400km/h'

# # Delete
# print('Before deletion', x)
# del x['tup']
# print('After deletion', x)

# # Lookup
# print('Lookup')
# print('salkdf;jsadl;fk' in x)       # does not telle if the value is present
#                                     # it tells you if the key is present
# print('salkdf;jsadl;fk' in x.values())

# useful shit
values = x.values()
keys = x.keys()
print(x.items())

# loop over a dictionary
for key, value in x.items():
    print(key, value, sep='---->')

for i in x:
    print(i, x[i], sep='====>')
