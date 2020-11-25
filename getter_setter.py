'''
POO : les propriétés -> Modifier/controler les attributs (Encapsulation)

<getter>	Accesseur	--> Recuperer la valeur de l'attribut
<setter>	Mutateur	--> Définir la valeur de l'attribut
<property> 	(<getter>, <setter>)


'''

class Humain:
	#constructeur
	def __init__(self, nom, prenom):
		self._nom = nom 
		self.prenom = prenom 


	def get_nom(self):
		return self._nom 

	def set_nom(self, nouveauNom):
		
		self._nom = nouveauNom

	LeNom = property(get_nom, set_nom)


#programme
h1 = Humain("Tremblay", "David")
h1.LeNom = "Desjardins"


print("L'objet h1 se nomme", h1._nom, h1.prenom)