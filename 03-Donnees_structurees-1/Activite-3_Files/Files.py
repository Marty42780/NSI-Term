# ---------------------------------------------------------------------------- #
#                                     Files                                    #
# ---------------------------------------------------------------------------- #

def CREER_FILE_VIDE() -> list:
    return [None, 3, 0, None, None, None, None, None]

def ENFILER(F:list,x) -> bool:
    for i in range(3, len(F)):
        print(i, F[i])
        if F[i] == None:
            F[i] = x
            return True
    return False

def EST_PLEINE(F: list) -> bool:
    if F[-1] != None:
        return True
    else:
        return False

def DEPILER(P:list):
    for i in range(3, len(F)):
        print(i, F[i])
        if F[i] != None:
            F.pop(i)
            return True
    return False

F = CREER_FILE_VIDE()
for i in range(6):
    print(ENFILER(F, 2))

print(F)
print(len(F))
