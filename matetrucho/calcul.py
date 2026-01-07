class Calculateur:
    def __init__(self, nom="Utilisateur"):
        self.nom = nom

    def additionner(self, a, b):
        """Méthode 1 : Une addition simple"""
        return a + b

    def additionner2(self, a, b):
        """Méthode 1 : Une addition simple"""
        return a + 5*b
    
    def saluer(self):
        """Méthode 2 : Une interaction textuelle"""
        return f"Bonjour {self.nom}, le module matetrucho est prêt !"
