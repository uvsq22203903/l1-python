# -*-coding:Utf-8 -*
import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -
cpt = 0
def fermer_fenetre():  # fonction callback qui appelle la fonction destroy()
    root.destroy()
"""
def compteur(event):
    global cpt
    cpt += 1
    texte['text']="Nombre de clics = "+ str(cpt) # 

def couleur(event):
    if (event.widget == caneva_rouge):
        texte['text'] = "Couleur du canvas = Rouge"
    if (event.widget == canevas_noir):
        texte['text'] = "Couleur du canvas = Noir"
"""
# - - - - - - - - - - - - - - - - - - - - - - - - 
# Création de la fenêtre de l'interface graphique
# - - - - - - - - - - - - - - - - - - - - - - - -

root = tk.Tk()
root.title("J'apprends Tkinter")

# - - - - - - - - - - - - - - - - - -
# Création des canvas sur une grille
# - - - - - - - - - - - - - - - - - -
"""
caneva_rouge = tk.Canvas(root, width = 300, height = 300, bg ='red')
caneva_rouge.grid(row = 0, column = 1)
canevas_noir = tk.Canvas(root, width = 300, height = 300, bg ='black')
canevas_noir.grid(row = 1, column = 1)

# - - - - - - - - - - - - -
# Création d'un label texte
# - - - - - - - - - - - - -

texte = tk.Label (root, text = "Nombre de clics= " + str(cpt)) # concaténer deux chaines de caractères dans texte
texte.grid(row=0, column = 0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Création d'un bouton lancant la fonction fermer_fenetre
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

bouton = tk.Button(root, text="Quitter", command = fermer_fenetre)
bouton.grid(row=0, column=1)

caneva_rouge.bind("<Button-1>", compteur)
root.bind("<Double-1>", couleur)
"""


create=True

def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()
        create=False
        
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()

bouton = tk.Button(root, text = "Charger", command = lambda : charger(root))
bouton.place(x = 10, y = 10)

root.mainloop() # permet de toujours actualiser la fenêtre

