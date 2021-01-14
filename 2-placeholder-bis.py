def afficheFamille(personne, age, nb_enfants):
    var1 = '{0} a {1} ans et a {2} enfants'
    return var1.format(personne.lower(), age, nb_enfants)


print(afficheFamille('Jean Jacques', 45, 3))
print(afficheFamille('Marie', 32, 5))


def showPrice(art, price):
    print(" L'article {0} coute {1:49.2f} €".format(art, price))
# [flags][width][.precision]type


showPrice('ps5', 1000)


def showPrice2(art, price):
    a = "L'article {article} coute {prix:.2f} €"
    print(a.format(article=art.lower(), prix=price))


showPrice2('ORDINATEUR', 3000)
