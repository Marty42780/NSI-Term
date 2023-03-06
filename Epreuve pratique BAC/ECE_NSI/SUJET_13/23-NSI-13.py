# Epreuve Pratique BAC NSI
# SUJET 13

#------------EXERCICE 1---------------------------
#---------Recherche-------------------------------

def recherche(a, tab):
    result = 0
    for i in tab:
        if a == i:
            result += 1
    return result

#------------EXERCICE 2---------------------------
#---------Rendu_Monnaie-------------------------------

pieces = [1, 2, 5, 10, 20, 50, 100, 200]
def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre -= pieces[i]
        else:
            i -= 1
    return rendu


