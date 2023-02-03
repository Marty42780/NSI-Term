class Time(object):
    "Definition d'un objet temps"
    def __init__(self, hh=12, mm=0, ss=0):
        self.heure = hh
        self.minute = mm
        self.seconde = ss

    def affiche_heure(self):
        print(f"{self.heure}:{self.minute}:{self.seconde}")


instant = Time(8, 15, 49)


class Domino(object):
    "Definition d'un objet domino"
    def __init__(self, pointA=0, pointB=0):
        self.pointA=pointA
        self.pointB=pointB
    
    def affiche_points(self):
        print("Face A :", str(self.pointA))
        print("Face B :", str(self.pointB))

    def valeur(self):
        return self.pointA + self.pointB

domino1 = Domino(2,6)
domino2 = Domino(4,3)


class CompteBancaire():
    "Definition d'un objet compte bancaire"
    def __init__(self, nom="DURAND", solde=800):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme
        
    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print(f"Le solde du compte bancaire de M. {self.nom} est de {self.solde} euros.")

compte1 = CompteBancaire()
compte2 = CompteBancaire()


class Voiture():
    "Definition d'un objet voiture"
    def __init__(self, marque='Ford', couleur='rouge', pilote='personne', vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse

    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        if not self.pilote == 'personne':
            self.vitesse += taux*duree
    
    def affiche(self):
        print(f"La voiture de marque {self.marque} et de couleur {self.couleur} est pilotée par {self.pilote} a la vitesse de {self.vitesse} m/s.")

voiture1 = Voiture('Peugeot', 'bleue')
voiture2 = Voiture(couleur = 'verte')
voiture3 = Voiture('Mercedes')
voiture1.choix_conducteur('Roméo')
voiture2.choix_conducteur('Juliette')
voiture2.accelerer(1.8, 12)
voiture3.accelerer(1.9, 11)

class Satellite():
    def __init__(self, nom, masse=100, vitesse=0):
        self.nom = nom
        self.masse = masse
        self.vitesse = vitesse

    def impulsion(self, force, duree):
        self.vitesse += (force*duree)/self.masse

    def affiche_vitesse(self):
        print(f"La vitesse du satellite {self.nom} est de {round(self.vitesse, 1)} m/s.")

    def energie(self):
        return round((self.masse*(self.vitesse**2))/2, 1)

satellite1 = Satellite("Zoe", 250, 10)
satellite1.impulsion(500, 15)
satellite2 = Satellite("Hercule", 350, 20)
satellite2.impulsion(600, 20)

