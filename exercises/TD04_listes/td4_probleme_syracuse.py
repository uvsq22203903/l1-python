def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste.append(n)
    return liste


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1, n_max + 1):
        syracuse(i)
    return True


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n)) - 1


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = [tempsVol(i) for i in range(1, n_max + 1)]
    return liste


def altMax(n: int) -> int:
    """Retourne l'altitude maximale de l'entier n"""
    return max(syracuse(n))


def altMaxListe(n_max):
    return [altMAx(i) for i in range(1 n_max +1)]


# ####### Programme Principal #######

print(syracuse(3))
print(testeConjecture(10000))
print("Le temps de vol de", 3, "est", tempsVol(3))
print(tempsVolListe(100))
liste_temps = tempsVolListe(10000)
temps_max = max(liste_temps)
print("L'entier", liste_temps.index(temps_max)+1, "a le plus grand temps de vol égal à", temps_max)
list_alt = altMaxListe(10000)
altitude_max = max(list_alt)
print("L'entier", list_alt.index(altitude_max)+1, "a la plus grande altitude maximale égale à", altitude_max)
