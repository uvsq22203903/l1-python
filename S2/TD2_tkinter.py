import tkinter as tk

root = tk.Tk()
root.title("J'apprends Tkinter")
texte = tk.Label (root, text = "J'adore Python")
bouton = tk.Button(root, text="Quitter", command=root.quit)

texte.pack()
bouton.pack()
root.mainloop


