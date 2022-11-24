import random
# ######### 1. Débuts avec les listes ##########

liste = [3, 5, 10]  # Question 1

liste.append(12)  # Question 2
liste.append(17)
print(liste)

liste[2] = -7  # Question 3
print(liste)

for i in range(len(liste)):  # Question 4
    liste[i] = liste[i]*2

for i in range(len(liste)):  # Question 5
    liste[i] = liste[i] + 1

liste_aleatoire = []  # Question 6
for i in range(10):
    liste_aleatoire.append(random.randint(10, 99))
print("liste aléatoire:", liste_aleatoire)

liste_pair = []  # Question 7
liste_impair = []
for i in liste_aleatoire:
    if i % 2 == 0:
        liste_pair.append(i)
    else:
        liste_impair.append(i)
print("pair: ", liste_pair)
print("impair: ", liste_impair)

liste_aleatoire.sort()  # Question 8
print("liste aléatoire triée: ", liste_aleatoire)

del liste_aleatoire[0]  # Question 9
del liste_aleatoire[-1]  # on peut parcourir la liste à l'envers
print(liste_aleatoire)

paquet = [i for i in (1, 53)]  # Question 10

# Question 11
# Solution 1 - En créant un nouveau paquet
coupe = random.randint(0, 51)
paquet2 = []
for i in range(coupe, 52):
    paquet2.append(paquet[i])
for i in range(coupe):
    paquet2.append(paquet[i])
print(paquet2)
