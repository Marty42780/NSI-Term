liste_a_trier = [80, 14, 60, 17, 97, 19, 67, 81, 13, 52]

def diviser(liste: list) -> list:
    if len(liste) > 1:
        return (liste[:int(len(liste)/2)], liste[int(len(liste)/2):])
