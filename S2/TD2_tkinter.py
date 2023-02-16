import tkinter as tk
# Création de la fenêtre de l'interface graphique
root = tk.Tk()
root.title("J'apprends Tkinter")

 # fonction callback qui appelle la fonction destroy()
def fermer_fenetre():
    pass


texte = tk.Label (root, text = "J'adore Python")
bouton = tk.Button(root, text="Quitter", command=root.destroy)







texte.pack()
bouton.pack()
root.mainloop # permet de toujours actualiser la fenêtre
 # programme principal
print("finish")
