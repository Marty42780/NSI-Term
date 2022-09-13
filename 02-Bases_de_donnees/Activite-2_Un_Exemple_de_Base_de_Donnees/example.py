import sqlite3

def clients_ville_donnee():
    print("Liste des clients d'une ville donnée : ")
    nom_ville = input("Nom de la ville : ")
    CurseurNomVille = connexion.execute('SELECT * FROM CLIENT WHERE  VILLE =? ', (nom_ville,))
    for tupleVille in CurseurNomVille:
        print(tupleVille[1])

connexion = sqlite3.connect('exemple.bdd')
connexion.execute('PRAGMA foreign_keys = on')
clients_ville_donnee()
connexion.close()