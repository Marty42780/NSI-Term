from math import sqrt

class Point(object):
    "Définition d'un point Mathématique"

    def affiche_point(p):
        print("Coordonnées :", str(p.x), ";", str(p.y))

    def distance(p1, p2):
        return sqrt(((p1.x-p2.x)**2+(p1.y-p2.y)**2))

p5, p6 = (Point() for i in range(2))
p5.x, p5.y, p6.x, p6.y = 12.3, 5.7, 6.2, 9.1
affiche_point(p6)

class Rectangle(object):
    "Définition d'un rectangle"

def trouveCentre(box):
    p = Point()
    p.x = box.coin.x + box.largeur/2.0
    p.y = box.coin.y + box.longueur/2.0
    return p

boite = Rectangle()
boite.largeur = 50.0
boite.longueur = 35.0

boite.coin = Point()
boite.coin.x = 12.0
boite.coin.y = 27.0

print(trouveCentre(boite))
centre = trouveCentre(boite)
print(centre)

