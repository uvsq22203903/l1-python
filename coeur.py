import turtle
pen = turtle.Turtle()

def courbe():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def coeur():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    courbe()
    pen.left(120)
    courbe()
    pen.forward(112)
    pen.end_fill()

def texte():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write("Je t'aime doudou <3", font = ("Verdana", 12, "bold"))

coeur()
texte()
pen.ht()