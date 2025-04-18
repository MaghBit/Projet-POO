from Enemy import *
from random import randrange

class MobHolder:

    def __init__(self):
        self.possibleMob = []

        self.possibleMob.append(Enemy("L'Araignée", 10, 3))
        self.possibleMob.append(Enemy("Le Zombie","15",1))
        self.possibleMob.append(Enemy("La Chauve-Souris",6,5))
        self.possibleMob.append(Enemy("Le Rat",3,1))
        self.possibleMob.append(Enemy("Le Phantome",18,4))
        self.possibleMob.append(Enemy("Le Scorpion",11,5))
        self.possibleMob.append(Enemy("Le Serpent",12,5))
        self.possibleMob.append(Enemy("Le Squelette",7,7))
        self.possibleMob.append(Enemy("Le Dragon",23,7))

    def getMobyById(self, id):
        return self.possibleMob[id]
    
    def getPossibleMobNumber(self):
        return len(self.possibleMob)
    
    def pickRandomMob(self):
        return self.possibleMob[randrange(0,self.getPossibleMobNumber()-1)]