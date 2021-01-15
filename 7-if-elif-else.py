"""

a = input("Entrez votre nom : ")

if a == 'Elon':
    print('As-tu inventé la Tesla ?')
elif a == 'Joe':
    print('Bye', a)
else:
    print('Go fuck yourself')
"""
"""
nom, prenom, age, salaire, pays(states -> dollar, suise--> franc, bel --> euro)
histoire 1: len(nom) > 4
histoire 2: lens(nom) < 4
dans les histoires il y a une question d'argent, cite une somme d'argent
- currencies adapte au pays
- le mec gagnent 388 euro
 """
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prenom : ")
age = int(input("Quel est votre age ? ").strip())
salaire = float(input(" Quel est votre salaire ? ").strip())
pays = input("Dans quel pays habitez-vous ?")


def money(pays):
    currenc = ''
    if pays == 'State':
        currenc = '$'
    elif pays == 'Suisse':
        currenc = 'franc'
    elif pays == 'Belgique':
        currenc = 'euro'
    return currenc


def sale_pays(nom, prenom, age, salaire, pays):
    if len(nom) > 4:
        return 'Histoire 1'
    elif len(nom) < 4:
        currenc = money(pays)
        return f'{nom} {prenom} gagne {salaire:.2f} {currenc}'


print(sale_pays(nom, prenom, age, salaire, pays))

print('maina' > 'Marie-Jeanne')
