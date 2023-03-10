# Epreuve Pratique BAC NSI
# SUJET 15

#------------EXERCICE 1---------------------------
#-------------------------------------------------

def mini(temp:list, annees:list) -> tuple:
    return min(temp), annees[temp.index(min(temp))]

#------------EXERCICE 2---------------------------
#-------------------------------------------------

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

