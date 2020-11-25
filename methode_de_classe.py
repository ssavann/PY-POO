'''
POO: Methodes de classe -> agit sur la classe et non l'objet.
cls         -> class
classmethod -> definir la mthode de classe

'''


#constructeur avec valeur par défaut
class Vehicule:

    stock = 10

    def __init__(self , marque_vehicule = "Ferrari", couleur_vehicule="bleu"):
        #Attributs (variable de classe)
        self.marque = marque_vehicule
        self.couleur = couleur_vehicule

    def Decrementer_Stock(cls, nombre):
        cls.stock -= nombre

    DecrementerStock = classmethod(Decrementer_Stock)
   
#Programme

print("Nombre de voiture en stock :", Vehicule.stock)

Vehicule.DecrementerStock(2)
print("Nombre de voiture en stock :", Vehicule.stock)
