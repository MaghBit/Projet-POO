from Personnage import *

class Player(Personnage):
    
    def __inti__(self, name, pv, attackdmg):
        Personnage.__init__(self,name,pv,attackdmg)

    def printStat(self):
        print("Le Joueur {}".format(Personnage.getStat(self)))