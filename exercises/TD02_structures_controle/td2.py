# Exercice 1
"""
num1 = 15
num2 = 5
if num1 % num2 and num2 % num1:
    print("Factors!")
else:
    print("Not Factors!")

# Exercice 2

state = "Georgia"
if state == "New Jersey":
    print("School isn't cancelled")
elif state == "North Carolina":
    print("School is postponed")
elif state == "Georgia":
    print("School is cancelled !")
else:
    print("School's status is unknown")

# Exercice 3

zodiaque = {    0: "monkey",
                1: "rooster",
                2: "dog",
                3: "pig",
                4: "rat",
                5: "ox",
                6: "tiger",
                7: "rabbit",
                8: "dragon",
                9: "snake",
                10: "horse",
                11: "sheep"}
annee = int(input("Donnez une année pour découvrir le signe du zodiaque"))
x = annee % 12
print(x)
print(zodiaque[x])

# Exercice 4

temperature, celsius = -3,7, True
if celsius and temperature <= 0 or not celsius and temperature <= 32:
    print("Freezing !")
else:
    print("Not freezing !")

# Exercice 5

annee = int(input("saisir une année"))
if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print("Bisextile !")
else:
    print("Pas Bisextile")

# Exercice 6.1

for i in range(1, 11):
    print(i)
a = 10
b = 30
c = 4
print(range(a,b,c))

# Exercice 6.2

for i in range(2, 21, 2):
    print(i)

# Exercice 7.1

quantite = int[input("Combine de nombre allez-vous saisir ?")]
somme = 0
for i in range(quantite):
    nombre = int(input("Saisissez votre numéro"+str(1)))
    somme += nombre
print("La moyenne est :", somme/quantite)

# Exercice 7.2

somme = 0
quantite = 0
nombre_saisi = 0
while nombre_saisi != -1:
    nombre_saisi = int(input("saisissez nombre"))
    if nombre_saisi != -1:
        somme += nombre_saisi
        quantite += 1
print("La moyenne est", quantite, "nombre est :", somme/quantite)

# Exercice 8

nombre = int(input("Donnez un nombre"))
if nombre < 0:
    print("Mauvais nombre")
else:
    resultat = 1
    for i in range(1, nombre+1):
        resultat *= i
    print("factorielle", nombre, "est égale à", resultat)

# Exercice 9

jour_de_naissance = 0
reponse = int(input("votre jour de naissance est-il dans cette liste ? (0=non et 1=oui)1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31"))
if reponse == 1:
    jour_de_naissance +=1
reponse = int(input("votre jour de naissance est-il dans cette liste ? (0=non et 1=oui)2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31"))
if reponse == 1:
    jour_de_naissance +=2
reponse = int(input("votre jour de naissance est-il dans cette liste ? (0=non et 1=oui)4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31"))
if reponse == 1:
    jour_de_naissance +=4
reponse = int(input("votre jour de naissance est-il dans cette liste ? (0=non et 1=oui)8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31"))
if reponse == 1:
    jour_de_naissance +=8
reponse = int(input("votre jour de naissance est-il dans cette liste ? (0=non et 1=oui)16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"))
if reponse == 1:
    jour_de_naissance +=16
print("Votre jour de naissance est", jour_de_naissance)

# Exercice 10:

import random

num_loterie = random.randint(0, 99)
print(num_loterie)
num_utilisateur = int(input("Saisissez un nombre (2chiffres)"))
num_utilisateur_inverse = lambda num_utilisateur: int(str(num_utilisateur)[::-1])
if num_utilisateur == num_loterie:
    recompense = 10000
elif num_utilisateur_inverse == num_loterie:
    recompense = 3000
elif num_utilisateur[0] == num_loterie[0] or num_utilisateur[0] == num_loterie[1] or num_utilisateur[1] == num_loterie[0] or num_utilisateur[1] == num_loterie[1]:
    recompense = 1000

print("Votre récompense est de", recompense, "€.")"""

# Exercice 11:

entier = int(input("nombre entre 10 et 20 "))
somme = entier[0] + entier[1]
print(somme)

"""
# Exercice 18

n = int(input("entrez taille"))
for i in range(1, n+1):
    print(" ", "*")

# Exercice 19

n = int(input("donnez un entier"))
resultat, puissance = 0, 0
while resultat < 1000000:
    puissance += 1
"""
