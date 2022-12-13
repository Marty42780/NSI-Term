import turtle as t

t.speed(speed=10.5)
t.setx(-170)
t.sety(150)
t.clear()

""" Exerice 1 (4.2) """

def triangle (longueur):
    t.forward(longueur)
    t.left(120)
    t.forward(longueur)
    t.left(120)
    t.forward(longueur)

triangle(100)

""" Exerice 2 (4.4) """


def koch(longueur, n):
    if n == 0:
        t.forward(longueur)
    else:
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)
        t.right(120)
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)

def flocon(taille, etape):
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)
    
# flocon(400, 2)

t.exitonclick()