'''
POO: Methodes statiques -> méthode indépendante.
staticmethod    -> definir la methode statique

'''


#constructeur avec valeur par défaut
class Vehicule:

    stock = 10

    def __init__(self , marque_vehicule = "Ferrari", couleur_vehicule="bleu"):
        #Attributs (variable de classe)
        self.marque = marque_vehicule
        self.couleur = couleur_vehicule

   
    def Definition_Vehicule():
        print("Un véhicule est un moyen de transport...")

    Definition = staticmethod(Definition_Vehicule)    


#Programme

Vehicule.Definition()