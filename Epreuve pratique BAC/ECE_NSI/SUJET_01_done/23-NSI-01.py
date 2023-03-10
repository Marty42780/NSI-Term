# Epreuve Pratique BAC NSI
# SUJET 1

def verifie(liste):
    previous = liste.pop(0)
    for a in liste:
        if a < previous:
            return False
        previous = a
    return True

def depouille(urne):
    resultat = {} 
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

