Burger = ["Pain", "Cheese", "Steak", "Salade", "Tomate", "Onions", ["Ketchup", "Burger", "Creme"], "Pain"]

def CREER_FILE_VIDE() -> list:
    return [None]*5

def EST_VIDE(F:list) -> bool:
    if F == [None]*5:
        return True
    else:
        return False

def EMFILER(F:list,x) -> list:
    for i in range(len(F)):
        if F[i] == None:
            F[i] = x
            return F

def EST_PLEINE(F: list) -> bool:
    if F[-1] != None:
        return True
    else:
        return False

def DEPILER(P:list):
    P.append(None)
    return P.pop(0)

print(DEPILER(Burger))
print(Burger)