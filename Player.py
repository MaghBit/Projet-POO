#Ce fichier a pour but de d'avoir la classe de base pour tous les héros/joueurs
from Personnage import *

class Player(Personnage):
    
    def __inti__(self, name, pv, attackdmg):
        Personnage.__init__(self,name,pv,attackdmg)

    def printStat(self):
        print("Le Joueur {}".format(Personnage.getStat(self)))
