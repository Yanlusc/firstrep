bryan_com = 'print moi une petite phrase, tu me prints ça'
mis_a_jour = 'pause café'
var_bol1 = True
numb1 = 100000
# le underscore permet de séparer les chiffres depuis Python 3 .
numb2 = 20_0000
numb2_bis = '{:_}'.format(numb1)
numb3 = numb1 + numb2


print(var_bol1)
print(bryan_com)
print(numb3)
print(mis_a_jour)
print(numb2_bis)


print(str(numb1) + ' ' + str(numb2) + ' ' + str(numb3))
print('numero suivant ' + str(numb1), numb2, numb3, sep='\nnumero suivant ')
# \n permet de faire un saut de ligne
print('{:_x}'.format(0xFFFFFFFF))
