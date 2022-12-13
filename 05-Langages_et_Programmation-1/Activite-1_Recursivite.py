
""" Exercice 1 """

def fctA ():
    print("Début fonction fctA")
    i = 0
    while i < 5:
        print(f"fctA {i}")
        i += 1
    print("Fin fonction fctA")
    
def fctB(): 
    print("Début fonction fctB")
    i = 0
    while i < 5:
        if i == 3:
            fctA()
            print("Retour à la fonction fctB")
        i += 1
    print("Fin fonction fctB")
    
# fctB()

""" Exercice 2 """

def fctC():
    print("Hello World!")
    fctC()

# fctC()

""" Exercice 3 """

def fctD(n):
    if n > 0:
        fctD(n-1)
    print(n)

# fctD(3)

""" Exercice 4 """

def fctE(n):
    if n > 0:
        return n*fctE(n-1)
    else:
        return 1
    
print(fctE(3))

