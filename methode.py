'''
POO: Methodes -> c'est une fonction de classe

'''


#constructeur avec valeur par défaut
class Vehicule:
    def __init__(self , marque_vehicule = "Ferrari", couleur_vehicule="bleu"):
        #Attributs (variable de classe)
        self.marque = marque_vehicule
        self.couleur = couleur_vehicule


    #ceci est une méthode
    def SeDeplacer(self):
        print(f"{self.marque} se deplace...")

#Programme

#nouvelle instance "maVoiture"
maVoiture = Vehicule("Honda", "orange")
maVoiture.SeDeplacer()


#nouvelle instance "VoitureDePapa"
VoitureDePapa = Vehicule()
VoitureDePapa.SeDeplacer()
