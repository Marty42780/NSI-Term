import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def randomBool(): return random.randint(0,1)

def completeNoeud(nodes, alphabet):
    left = alphabet.pop(0)
    right = alphabet.pop(0)
    if nodes == 0:
        return None
    if randomBool() == 1:
        leftValue = completeNoeud(nodes-1, alphabet)
    else:
        leftValue = None
    if randomBool() == 0:
        rightValue = completeNoeud(nodes-1, alphabet)
    else:
        rightValue = None
    return {'left': leftValue, 'right': rightValue}
    
class arbre:
    def __init__(self, nodes):
        self.alphabet = alphabet
        self.himself = {'racine':{}} # Initialisation
        nodes -= 1 # Pour le point A
        self.himself['racine'] = completeNoeud(nodes, self.alphabet) # type: ignore # On rajoute les noeuds suivant sans dépasser nodes en hauteur
    
    def droit(self, noeud):
        return self.himself[noeud]
    
    
objet = arbre(nodes=2)
print(objet.himself)
print(objet.droit('racine'))
