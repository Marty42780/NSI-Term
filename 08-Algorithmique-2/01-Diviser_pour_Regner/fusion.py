from math import ceil

# Exercice 1

A = [23, 12, 4, 56, 35, 32, 42, 57, 3]

def diviser(liste: list) -> list:
    if len(liste) > 1:
        return (liste[:ceil(len(liste)/2)], liste[ceil(len(liste)/2):])
    else:
        return liste

def trier(liste: list) -> list:
   pass 

# Exercice 2

"""
def maxi(liste):
    maxi = liste[0]
    for i in liste[1:]:
        if i > maxi:
            maxi = i
    return maxi
"""

def maxi(liste):
    mid = len(liste)//2
    if len(liste)>1:
        return max(maxi(liste[:mid]), maxi(liste[mid:]))
    return liste[0]
    
