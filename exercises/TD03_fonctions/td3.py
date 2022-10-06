# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    sum = 0
    sum += temps[0]*24*60*60
    sum += temps[1]*60*60
    sum += temps[2]*60
    sum += temps[3]
    return sum

temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")
