# -*- coding: utf-8 -*-
import random


class Personnage:
    """Instruction de la classe"""

    def __init__(self, nombreDeVie):
        self.vie = nombreDeVie

    def donneEtat(self):
        return self.vie

    def perdVie(self):
        self.vie -= random.randint(1, 3)


def game():
    Bilbo = Personnage(20)
    Gollum = Personnage(30)
    while Bilbo.donneEtat() > 0 and Gollum.donneEtat() > 0:
        Bilbo.perdVie()
        Gollum.perdVie()
    if Bilbo.donneEtat() <= 0 and Gollum.donneEtat() > 0:
        message = f"Gollum est vainqueur, il lui reste encore {Gollum.donneEtat()} points alors que Bilbo est mort."
    elif Gollum.donneEtat() <= 0 and Bilbo.donneEtat() > 0:
        message = f"Bilbo est vainqueur, il lui reste encore {Bilbo.donneEtat()} points alors que Gollum est mort."
    else:
        message = f"Les deux combattants sont morts en m�me temps."
    return message
