# Exercice 1

v = "35.0"
print(type(v))

# Exercice 2

nbr = input("Saisir un un nombre entier")
if nbr[0] < 0 and nbr[0] < 9:
    print("Ceci n'est pas un nombre")
if nbr / 5:
    print("le nombre est divisible par 5")
else:
    quotient = nbr // 5
    reste = nbr % 5
    print("Ce nombre n'est pas divisible par 5 : le quotient et le reste de la div euclidienne valent ", quotient, "et", reste, "respectivement.")

# Exercice 3

nombre = 8
factorielle = 1
while nombre != 0:
    a = nombre - 1
    factorielle *= a
factorielle *= nombre
print(factorielle)
