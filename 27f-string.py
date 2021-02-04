import uuid

tim = 59


def mult(param):
    return param*8

# f string only exist only since python version 3.
# basic f string
s = f'{[i for i in [3, 234, 23, 987] if i%3==0]} ' \
    f'Hello {tim} {22 + 5} {divmod(19, 4)}'
print(s)

# advanced f string
ma_liste = {'name': 'Yan', 'lastName': 'Luxi', 'id': uuid.uuid4()}
newline = '\n'
print (list(f"{key}: {value}" for key, value in ma_liste.items()))
sd = f'{newline.join(f"{key}: {value}" for key, value in ma_liste.items())}'
print(sd)
