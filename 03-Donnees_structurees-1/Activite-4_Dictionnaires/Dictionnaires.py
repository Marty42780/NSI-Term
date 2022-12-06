# ---------------------------------------------------------------------------- #
#                                 Dictionnaires                                #
# ---------------------------------------------------------------------------- #

dicoprix = {"jambon":3, "sauce_tomate":1.5, 'poivrons':2, 'oignons':1, "champignons":2, "mozarella":1.5, "creme_fraiche":1.5, "chevre":2, "tomates":2, "lardons":2.5, 'saumon':4, 'merguez':3}

def prixmoyen(dico: dict) -> float:
    return round(sum(dico.values())/len(dico), 2)

def prixPizza(list_ingredients: list, dicoprix: dict) -> float:
    prix = 0.0
    for i in list_ingredients:
        prix += dicoprix[i]
    return prix*1.5


monDicoPizzas ={"reine":["jambon", "mozarella", "sauce_tomate", "champignons"], 
"vesuvio": ['merguez', 'jambon', 'mozarella', 'poivrons', 'oignons' ], "cabri":["chevre", 
"lardons", "creme_fraiche","mozarella"], "napoli":["jambon", "tomates", "mozarella", 
"sauce_tomate", "champignons", "poivrons", "oignons"], "neptune":['saumon', 
'creme_fraiche','champignons']}

def possible(dicopizza: dict, val: int, dicoprix: dict) -> list: 
    pizzas_budgetables = []
    for i in dicopizza:
        if prixPizza(dicopizza[i], dicoprix) <= 12:
            pizzas_budgetables.append(i)
    return pizzas_budgetables

def affichePizza(dicopizzas: dict, dicoprix: dict) -> None:
    for pizza in dicopizzas:
        ingredients = ""
        for e in dicopizzas[pizza]:
            ingredients += e + " "
        print("pizza", pizza, ":", ingredients, prixPizza(dicopizzas[pizza], dicoprix))
    
def fusion(monDicoPizzas: dict, dicoprix: dict) -> dict:
    kingfusion = {}
    for pizza in monDicoPizzas:
        kingfusion[pizza] = monDicoPizzas[pizza], prixPizza(monDicoPizzas[pizza], dicoprix)
    return kingfusion

print(fusion(monDicoPizzas,dicoprix))