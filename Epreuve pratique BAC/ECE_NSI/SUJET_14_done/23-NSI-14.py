# Epreuve Pratique BAC NSI
# SUJET 14

#------------EXERCICE 1---------------------------
#---------Recherche-------------------------------

def recherche(elt, tab):
    if elt in tab:
        for i in range(len(tab)):
            if elt == tab[i]:
                return i
            i += 1
    else:
        return -1


#------------EXERCICE 2---------------------------
#---------insertion-------------------------------

def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(l) - 2
    print(l, i)
    while a < l[i] and i >= 0: 
        print(l)
        l[i+1] = l[i] # Marche pas
        l[i] = a
        i = i-1 
    return l

