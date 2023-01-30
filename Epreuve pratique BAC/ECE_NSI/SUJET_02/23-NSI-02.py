# Epreuve Pratique BAC NSI
# SUJET 2

def indices_maxi(tab):
    max_value = 0
    max_values_indexes = []
    for number in tab:
        if number > max_value:
            max_value = number
    for index in range(len(tab)):
        if tab[index] == max_value:
            max_values_indexes.append(index)
    return (max_value, max_values_indexes)

def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

