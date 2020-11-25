'''
POO : les propriétés -> Modifier/controler les attributs (Encapsulation)


'''

class Humain:
	#constructeur
	def __init__(self, nom, prenom):
		self.nom = nom 
		self.prenom = prenom 



#programme
h1 = Humain("Tremblay", "David")

h1.nom = "Lemieux"

print("L'objet h1 se nomme", h1.nom, h1.prenom)