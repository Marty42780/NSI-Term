from math import ceil

A = [23, 12, 4, 56, 35, 32, 42, 57, 3]

def diviser(liste: list) -> list:
    if len(liste) > 1:
        return (liste[:ceil(len(liste)/2)], liste[ceil(len(liste)/2):])
    else:
        return liste

def trier(liste: list) -> list:
   pass 
