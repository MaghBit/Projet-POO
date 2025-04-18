import random

class LanceDe:
    def __init__(self):
        self.critique=15
        self.normal=10
        self.presque=5
        self.rate=0
        self.resultat = None

    def lanceDe(self):
        """
        Lance un dé à 20 faces et renvoie le résultat"""
        i=random.randint(0,21)
        if self.critique<=i:
            return "critique"
        elif self.normal<=i<self.critique:
            return  "normal"
        elif self.presque<=i<self.normal:
            return "presque"
        else:
            return "rate"
        
    def getvaleur(self):
        if self.lanceDe=="critique":
            return 15
        elif self.lanceDe=="normal":
            return  10
        elif self.lanceDe=="presque":
            return 5
        else:
            return 0