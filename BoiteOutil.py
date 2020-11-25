class Rectangle:
    
    #Constructeur de classe
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur
        
    #Méthodes
    def Perimetre(self):
        return (int(self.longeur) * 2) + (int(self.largeur) * 2)
    
    def Aire(self):
        return int(self.longeur) * int(self.largeur)
    
    def EstCarre(self):
        if self.longeur == self.largeur:
            return True
        return False
