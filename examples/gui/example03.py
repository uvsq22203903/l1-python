import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 500


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 300
x1 = CANVAS_WIDTH - 300
y1 = 100
y2 = 400
canvas.create_line(x0, y1, x1, y2)
canvas.create_oval(250,50,350,150)
canvas.create_oval(250, 200, 350, 300)
canvas.create_oval(250, 350, 350, 450)
    
# Fin de votre code

canvas.pack()
root.mainloop()
