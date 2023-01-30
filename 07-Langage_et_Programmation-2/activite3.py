class Time(object):
    "Definition d'un objet temps"
    def affiche_heure(self):
        print(f"{self.heure}:{self.minute}:{self.seconde}")


instant = Time()
instant.heure = 11
instant.minute = 34
instant.seconde = 25
