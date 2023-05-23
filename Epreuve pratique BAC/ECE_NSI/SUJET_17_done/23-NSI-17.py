# Epreuve Pratique BAC NSI
# SUJET 17

#------------EXERCICE 1---------------------------
#-------------------------------------------------

def moyenne(liste_notes):
    total_points, total_coefs = 0, 0
    for note in liste_notes:
        total_points += note[0] * note[1]
        total_coefs += note[1]
    return total_points / total_coefs
        

#------------EXERCICE 2---------------------------
#-------------------------------------------------

def pascal(n):
    triangle = [[1]]
    for k in range(1, n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle
