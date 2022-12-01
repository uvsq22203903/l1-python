import random

class TicTacToe:
    def __init__(self):
        self.plateau = []
    
    def creation_plateau(self):
        for i in range(3):
            rangee = []
            for j in range(3):
                rangee.append('-')
            self.plateau.append(rangee)
    
    def get_random_premier_joueur(self):
        return random.randint(0, 1)

    def joueur(self, rangee, col, joueur):
        self.plateau[rangee][col] = joueur

    def vainqueur(self, joueur):
        victoire = None
        n =len(self.plateau)

        # verif rangée
        for i in range(n):
            victoire = True
            for j in range(n):
                if self.plateau[i][j]!=joueur:
                    victoire = False
                    break
            if victoire:
                return victoire

        # vérif colonne
        for i in range(n):
            victoire = True
            for j in range(n):
                if self.board[j][i]!= joueur:
                    victoire = False
                    break
            if victoire:
                return victoire

        # verif diagonale
        victoire = True
        for i in range(n):
            if self.plateau[i][j]!= joueur:
                victoire = False
                break
            if victoire:
                return victoire
        
        victoire = True
        for i in range(n):
            if self.plateaau[i[n-1-i]]!= joueur:
                victoire = False
                break
        if victoire:
            return victoire, False
            
        for rangee in self.plateau:
            for item in rangee:
                if item == '-':
                    return False
        return True

    def plateau_plein(self):
        for rangee in self.plateau:
            for item in rangee:
                if item == '-':
                    return False
        return True

    def changement_joueur(self, joueur):
        return 'X' if joueur == 'O' else 'O'

    def plateau(self):
        for rangee in self.plateau:
            for item in rangee:
                print(item, end=" ")
    
    def debut(self):
        self.create_plateau()
        joueur = 'X' if self.get_random_premier_joueur()==1 else 'O'
        while True:
            print(f"Player {joueur} turn")
        self.show_plateaau()

