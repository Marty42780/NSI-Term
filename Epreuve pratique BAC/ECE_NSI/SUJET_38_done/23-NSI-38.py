# Epreuve Pratique BAC NSI
# SUJET 38

#------------EXERCICE 1---------------------------
#-------------------------------------------------

def correspond(mot, mot_a_trous):
    if len(mot) == len(mot_a_trous):
        for char in zip(mot, mot_a_trous):
            if char[0] == char[1] or char[1] == '*':
                pass
            else:
                return False
        return True
    else:
        return False

#------------EXERCICE 1---------------------------
#-------------------------------------------------

def est_cyclique(plan): 
    expediteur = 'A' 
    destinataire = plan[expediteur] 
    nb_destinaires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1
    return nb_destinaires == len(plan)
