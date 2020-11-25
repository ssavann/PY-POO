'''
POO: Les classes
mot clé: class <nom de la classe>
camel case (casse de chameau)	-> chaque mot commence par une lettre capital (Majuscule)
class BatimentExterieur:

class Vehicule:
    #Attributs (variable de classe)
    couleur = "rouge"
    marque = "renault"
'''
from Classes.Vehicule import *


#Programme

voiture1 = Vehicule()   #instance objet
voiture2 = Vehicule()   #instance objet

voiture2.couleur = "jaune"
voiture2.marque = "Citroen"


print(f"La voiture 1 est de couleur {voiture1.couleur} et c'est une {voiture1.marque}")

print(f"La voiture 2 est de couleur {voiture2.couleur} et c'est une {voiture2.marque}")

