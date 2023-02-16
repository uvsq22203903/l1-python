# -*-coding:Utf-8 -*
import tkinter as tk

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -

def fermer_fenetre():  # fonction callback qui appelle la fonction destroy()
    root.destroy()

# - - - - - - - - - - - - - - - - - - - - - - - - 
# Création de la fenêtre de l'interface graphique
# - - - - - - - - - - - - - - - - - - - - - - - -

root = tk.Tk()
root.title("J'apprends Tkinter")
root.geometry("400x300")
caneva = Canvas(root, width = 500, height = 500, bg ='red')
caneva.place(x = 100, y = 100)

# - - - - - - - - - - - - -
# Création d'un label texte
# - - - - - - - - - - - - -

texte = tk.Label (root, text = "J'adore Python")
texte.pack()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Création d'un bouton lancant la fonction fermer_fenetre
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

bouton = tk.Button(root, text="Quitter", command = lambda: fermer_fenetre())
bouton.pack()


root.mainloop # permet de toujours actualiser la fenêtre

# programme principal
print("finish")
