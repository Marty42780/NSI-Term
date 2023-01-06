'''
Partie pour générer des arbre aléatoirement
'''
import random
alphabet = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def randomBool(): return random.randint(0,1)
def completeNoeud(nodes, alphabet):
    left = right = alphabet.pop(0)
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
    return {left+'-left': leftValue, right+'-right': rightValue}
class genarbre:
    def __init__(self, nodes):
        self.alphabet = alphabet
        self.himself = {'a':{}} # Initialisation
        nodes -= 1 # Pour le point A
        self.himself['a'] = completeNoeud(nodes, self.alphabet) # type: ignore # On rajoute les noeuds suivant sans dépasser nodes en hauteur
    
    def get_value(self, key):
        data = self.himself
        if key in data:
          return data[key]
        for k, v in data.items():
          if isinstance(v, dict):
            item = genarbre.get_value(self, key)
            if item is not None:
              return item
        return None
objet = genarbre(nodes=3)

'''
Partie pour générer des arbres à l'avance
'''
arbre = {'A':['B', 'F'], 'B':['C', 'D'], 'C':['E', ''], 'D':['', ''], 'E':['', ''], 'F':['G', 'H'], 'G':['I',''], 'H':['J', ''], 'I':['', ''], 'J':['', '']}

def hauteur(arbre, noeud='A'):
    if arbre[noeud][0] != '':
        hauteur(arbre, arbre[noeud][0])
    if arbre[noeud][1] != '':
        hauteur(arbre, arbre[noeud][0])
    else:
        return 0
    
hauteur(arbre)
