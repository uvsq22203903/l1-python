import random

# Déclarations des variables

morpion = [[0,0,0],
           [0,0,0],
           [0,0,0]]

victoire = False
notfull = True

# Déclaration des fonctions

def initialisation():
    who_start = random.randint(0,1)
    global joueur
    if who_start==0:
        print(joueur1, "commence.")
        joueur=1
    else:
        print(joueur2, "commence.")
    global victoire
    victoire=False
    global notfull
    notfull=True
    global fini
    fini=False


def jouer_signe(tour, morpion, position):

    return morpion


def verif():
    pass


def verif_full():
    global joueur
    global notfull
    global victoire
    global fini
    vainqueur = 0
    if victoire==False and notfull==True:
        ligne = 0
        colonne = 0
        try:
            while morpion[colonne][ligne]!=0:
                ligne+=1
                if ligne==3:
                    colonne+=1
                    ligne=0
        except IndexError:
            notfull=False
        


def affichage_final(victoire, vainqueur):
    if victoire == True:
        if vainqueur == 1:
            print("Le joueur 1 a gagné.")
        else:
            print("Le joueur 2 a gagné")
    else:
        print("Match nul")


def changement_joueur(joueur):
    # on passe au joueur suivant
    if joueur==1:
        joueur=2
    else:
        joueur=1
    return joueur


"""Programme Principal"""

joueur1= input("Quel est votre username ", )
joueur2 = input("Quel est votre username", )
initialisation()
