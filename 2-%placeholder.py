# a = 'Jean Jacques a 45 ans et a 3 enfants'
# b = 'Marie a 32 ans et a 5 enfants'

# print(a, b, sep='\n')

def afficheFamille(personne, age, nb_enfants):
    return '%s a %d ans et a %s enfants' % (personne, age, nb_enfants)


print(afficheFamille('Jean Jacques', 45, 3))
print(afficheFamille('Marie', 32, 5))
