# Epreuve Pratique BAC NSI
# SUJET 16

#------------EXERCICE 1---------------------------
#-------------------------------------------------

def recherche_indices_classement(elt: int, tab: list):
    result_inf, result_equal, result_sup = [], [], [] 
    for i in range(len(tab)):
        if tab[i] < elt:
            result_inf.append(i)
    for i in range(len(tab)):
        if tab[i] == elt:
            result_equal.append(i)
    for i in range(len(tab)):
        if tab[i] > elt:
            result_sup.append(i)
    return result_inf, result_equal, result_sup


#------------EXERCICE 2---------------------------
#-------------------------------------------------

resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [8, 4],
        'DS4':[15, 4]
    }
}

def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs[0], valeurs[1]
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return -1


