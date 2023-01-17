import random


class Personnage:
    """Instruction de la classe"""

    def __init__(self, nombreDeVie):
        self.vie = nombreDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        self.vie -= random.randint(1, 3)


Bilbo = Personnage(20)
Gollum = Personnage(30)

Bilbo.donneEtat()
Gollum.perdVie()
Gollum.donneEtat()
Bilbo.perdVie()
Bilbo.donneEtat()
