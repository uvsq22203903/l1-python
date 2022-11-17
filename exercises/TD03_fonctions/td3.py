import time
# ######### Déclaration de Fonctions #########

# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes


def tempsEnSeconde(temps: tuple) -> int:
    sum = 0
    sum += temps[0]*24*60*60
    sum += temps[1]*60*60
    sum += temps[2]*60
    sum += temps[3]
    return sum


"""
def tempsEnSeconde(temps: tuple) -> int:
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
"""


# Renvoie la valeur sec de tps donné comme jour, heure, min, sec.


def secondeEnTemps(seconde: int) -> tuple:
    """Renvoie le tps (j, h, min, sec) qui
    correspond au nbr de sec passé en arg"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


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


def demandeTemps(j, h, m, s):
    if j >= 0:
        print(j, "jour(s)")
    elif h >= 0 and h <= 24:
        print(h, "heure(s)")
    elif m >= 0 and m <= 60:
        print(m, "minute(s)")
    elif s >= 0 and s <= 60:
        print(s, "seconde(s)")


def sommeTemps(temps1, temps2):
    addition = secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))
    return addition


def proportionTemps(temps, proportion):
    calcul = secondeEnTemps(tempsEnSeconde(temps) + proportion)
    return calcul


# fonction auxiliaire
# supposant que le temps 0 est le 1 janvier 1970 à 00:00:00


def tempsEnDate(temps):
    """fonction `tempsEnDate`qui donne la date sous
    la forme (année, mois, jour, heure, minute, seconde)"""
    annee = temps[2]
    mois = temps[1]
    jour = temps[0]
    heure = temps[3]
    minute = temps[4]
    seconde = temps[5]
    return (annee, mois, jour, heure, minute, seconde)


"""
def tempsEnDate(temps: tuple) -> tuple:
    annee = 1970 + temps[0] // 35
    numero_du_jour = 1 + temps[0] % 365
    return (annee, numero_du_jour, temps[1], temps[2], temps[3])
"""


def afficheDate(date=-1):
    """fonction `afficheDate`qui affiche la date"""
    print(date[0], " ", mois_de_l_annee[date[1]], date[2], " ",
          date[3], ":", date[4], ":", date[5])


"""
def afficheDate(date: tuple = ()) -> None:
    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Jour numéro", date[1], "de l'année", date[0], "à",
          str(date[2]) + ":" + str(date[3] + ":" + str(date[4]))
"""


def bissextile(jour):
    pass


# ####################### Programme Principal #############################

mois_de_l_annee = {1: "janvier",
                   2: "février",
                   3: "mars",
                   4: "avril",
                   5: "mai",
                   6: "juin",
                   7: "juillet",
                   8: "aoüt",
                   9: "septembre",
                   10: "octobre",
                   11: "novembre",
                   12: "décembre"}

temps = (3, 23, 1, 34)
print(type(temps))


print(tempsEnSeconde(temps))


temps = secondeEnTemps(100000)
print(temps[0], " jours ", temps[1], " heures ",
      temps[2], " minutes ", temps[3], " sec")


afficheTemps((1, 0, 14, 23))


# Déclarations de variables
# j : jour, h : heure, m : minute, s : seconde

j = int(input("Saisir un nombre de jour"))
h = int(input("Saisir un nombre d'heure (ne dépassant pas 24h"))
m = int(input("Saisir un nombre de minutes (<=60)"))
s = int(input("Saisir un nombre de secondes"))

print(j, "jour ", h, "heure(s) ", m, "minute(s) ", s, "seconde(s)")


sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))


afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))

# appeler la fonction en échangeant l'ordre des arguments


temps = secondeEnTemps(1000000000)
afficheTemps(temps)


a, b = 0, 1
for i in range(0, 5):
    a += 1
    if a % 3 != 0:
        continue
    b *= 2
print(a, b)

# afficher date sous forme de temps

date = tempsEnDate((1, 4, 1970, 0, 0, 0))

print(time.time())  # Afficher le temps écoulé (en sec) depuis 1970
