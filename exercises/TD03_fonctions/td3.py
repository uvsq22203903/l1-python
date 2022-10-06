# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

temps = (3, 23, 1, 34)
print(type(temps))

# Renvoie la valeur sec de tps donné comme jour, heure, min, sec.

def tempsEnSeconde(temps):
    sum = 0
    sum += temps[0]*24*60*60
    sum += temps[1]*60*60
    sum += temps[2]*60
    sum += temps[3]
    return sum

print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le tps (j, h, min, sec) qui correspond au nbr de sec passé en arg"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "sec")

# fonction auxiliaire ici

def afficheplu(val, mot):
    if val != 0:
        print(val, mot, end="")
    if val > 1:
        print("s", end="")

def afficheTemps(temps):
    afficheplu(temps[0], "jour")
    afficheplu(temps[1], "heure")
    afficheplu(temps[2], "minute")
    afficheplu(temps[3], "seconde")

afficheTemps((1, 0, 14, 23))

# Déclarations de variables
# j : jour, h : heure, m : minute, s : seconde

j = int(input("Saisir un nombre de jour"))
h = int(input("Saisir un nombre d'heure (ne dépassant pas 24h"))
m = int(input("Saisir un nombre de minutes (<=60)"))
s = int(input("Saisir un nombre de secondes"))

def demandeTemps(j, h, m, s):
    if j >= 0:
        print(j, "jour(s)")
    elif h >= 0 and h <= 24:
        print(h, "heure(s)")
    elif m >= 0 and m <= 60:
        print(m, "minute(s)")
    elif s >= 0 and s <= 60:
        print(s, "seconde(s)")

print(j, "jour", h, "heure(s)", m, "minute(s)", s, "seconde(s)")

# afficheTemps(demandeTemps())

def sommeTemps(temps1, temps2):
    addition = secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))
    return addition

sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))

def proportionTemps(temps, proportion):
    calcul = secondeEnTemps(tempsEnSeconde(temps)+ proportion)
    return calcul

afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))
# appeler la fonction en échangeant l'ordre des arguments
