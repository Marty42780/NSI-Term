# ---------------------------------------------------------------------------- #
#                                    Listes                                    #
# ---------------------------------------------------------------------------- #

def INSERER(L, x, i): 
    if L[0] == (L.__len__()-1) or (i-i > L[0]):
        print("’La liste est déjà pleine ou alors le rang n’est pas correct !")
        return False
    else:
        for k in range(L[0]+1, i, -1):
            L[k] = L[k-1]
        L[i] = x
    L[0] = L[0]+1
    return True

def SUPPRIMER(L, i):
    if (L[0] != 0) and (i <= L[0]):
        for k in range(i, L[0]+1):
            L[k] = L[k+1]
        L[0] = L[0]-1
        return True
    else:
        print("La liste est déjà vide ou alors le rang n’est pas correct !")
        return False

Nb_Element = 5
Liste=[None]*(Nb_Element+1)
print(Liste)
Liste[0] = 0
print(Liste)
INSERER(Liste, 'N', 1)
print(Liste)
INSERER(Liste, 'I', 2)
print(Liste)
INSERER(Liste, 'I', 3)
print(Liste)
SUPPRIMER(Liste, 2)
print(Liste)
INSERER(Liste,'S',2)
print(Liste)
INSERER(Liste, 2020, 4)
print(Liste)
INSERER(Liste, 2021, 5)
print(Liste)
