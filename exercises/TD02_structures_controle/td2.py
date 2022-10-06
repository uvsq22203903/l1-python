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



# Exercice 6

for i in range(1, 11):
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
"""

# Exercice 8

nombre = int(input("Donnez un nombre"))
if nombre < 0:
    print("Mauvais nombre")
else:
    resultat = 1
    for i in range(1, nombre+1):
        resultat *= i
    print("factorielle", nombre, "est égale à", resultat)

# Exercice 18

n = int(input("entrez taille"))
for i in range(1, n+1):
    print(" ", "*")

# Exercice 19

n = int(input("donnez un entier"))
resultat, puissance = 0, 0
while resultat < 1000000:
    puissance += 1
