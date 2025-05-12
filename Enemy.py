#Ce fichier a pour but de d'avoir la classe de base pour tout les monstres
from Personnage import * 

class Enemy(Personnage):
    def __init__(self, name, pv, attackdmg):
        Personnage.__init__(self,name,pv,attackdmg)

    def printStat(self):
        print("Le monstre {}".format(Personnage.getStat(self)))
        
    def receiveNewEnemy(self, newEnnemy):
        self.__init__(newEnnemy.name, newEnnemy.pv, newEnnemy.attackdmg)
