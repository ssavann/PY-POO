import BoiteOutil

try:
    lon = input("Longeur du rectangle en cm ?")
    lar = input("Largeur du rectangle en cm ?")
    
    #Instancier l'objet rectangle
    rec = BoiteOutil.Rectangle(int(lon), int(lar))
    
    print(f"Le périmétre est {rec.Perimetre()} cm")
    print(f"L'aire du rectangle est {rec.Aire()} cm2")
    
    if rec.EstCarre():
        print("Ce n'est pas un rectangle.")
    else:
        print("C'est un rectangle.")
except:
    print("Une erreur s'est produite.")