P = [0, 1, 2, 3, None, None]

''' 4.3 Autres  exemples d’opérations sur les piles '''

def EMPILER(P:list,x):
    for i in range(len(P)):
        if P[i] == None:
            P[i] = x
            return P

def DEPILER(P:list):
    for i in range(len(P)-1,0, -1):
        if P[i] != None:
            dropped_value = P[i]
            P[i] = None
            return dropped_value
    
def CREER_PILE_VIDE() -> list:
    return [None]*5

def EST_VIDE(P:list) -> bool:
    if P == [None]*5:
        return True
    else:
        return False

def EST_PLEINE(P: list) -> bool:
    if P[-1] != None:
        return True
    else:
        return False


''' 4.5.3 Implémentattion en python '''
Nb_places = 5
Pile = CREER_PILE_VIDE()

Pile[0] = 1
print(Pile)
EMPILER(Pile, 2)
print(Pile)
EMPILER(Pile, 5)
print(Pile)
EMPILER(Pile, 9)
print(Pile)
DEPILER(Pile)
print(Pile)
EMPILER(Pile, 6)
print(Pile)