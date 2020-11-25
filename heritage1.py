'''
POO : Héritage (Classe mere ----> enfant)

Classe enfant: est une sorte de classe mère ---> spécialisation
issubclass(<Enfant>, <Mère>  ---> vrai ou faux)


'''

#classe mère
class Vehicule:
	
	def __init__(self, marque_vehicule, couleur_vehicule):
		#Attributs (Variable de classe)
		self.marque = marque_vehicule
		self.couleur = couleur_vehicule

	def SeDeplacer(self):
		print(f"{self.marque} Le véhicule se déplace")


#classe enfant
class Avion(Vehicule):

	def __init__(self, marque_Avion, couleur_Avion, nb_reacteur):
		Vehicule.__init__(self, marque_Avion, couleur_Avion)
		self.nb_reacteur = nb_reacteur


	def Voler(self):
		print(f"{self.marque} vole dans les air...")




#programme


v1 = Vehicule("Harley Davidson", "noir")

a1 = Avion("Airbus", "rouge", 2)

print(a1.marque)
print(a1.couleur)
a1.SeDeplacer()

a1.Voler()