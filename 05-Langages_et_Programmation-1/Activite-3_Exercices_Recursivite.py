""" Exerice 1 (Calcul des lignes du triangle de pascal) """

result = [0]
def lignesPascal(n):
    if n > 0:
        result.append(n)
        lignesPascal(n-1)
        return result
    else:
        return None

print(lignesPascal(4))