'''
POO: Le constructeur de classe
c'est une méthode qui porte un nom spécial __init__

self:   représente l'instance "voiture1" et "voiture2"
'''



class Vehicule:
    def __init__(self , marque_vehicule, couleur_vehicule):
        #Attributs (variable de classe)
        self.marque = marque_vehicule
        self.couleur = couleur_vehicule






#Programme

voiture1 = Vehicule("Renault", "rouge")   #instance objet
voiture2 = Vehicule("Toyota", "noire")   #instance objet




print(f"La voiture 1 est de couleur {voiture1.couleur} et c'est une {voiture1.marque}")

print(f"La voiture 2 est de couleur {voiture2.couleur} et c'est une {voiture2.marque}")

