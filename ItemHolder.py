#Ce fichier contient la classe ItemHolder qui gère les objets du jeu. Il permet de créer une liste d'objets possibles et de choisir un objet aléatoire avec des statistiques différentes.
from Item import *
from Amulet import *
from Potion import *

from random import randrange



class ItemHolder:
    def __init__(self):
        self.items = []

        #Création de la liste d'objets possibles avec leurs statistiques Item(nom, type, force)
        #Potion(nom, type, force)
        self.items.append(Potion("Potion de vie I",True,2))
        self.items.append(Potion("Potion de vie II",True,5))
        self.items.append(Potion("Potion d'acide léger I",False,1))
        self.items.append(Potion("Potion d'acide fort II",False,3))
        self.items.append(Potion("Potion de poison I",False,2))
        self.items.append(Potion("Potion de poison II",False,5))

        #Amulet(nom, type, point d'action, temps d'utilisation max)
        self.items.append(Amulet("Amulette de régénaration II ({} UT)","RestorePV",2,3))
         #{} qui se remplace par le nombre d'utilisations restantes grâce à la méthode format
        self.items.append(Amulet("Amulette de régénaration II ({} UT)","RestorePV", 3, 2))#2 UT
        self.items.append(Amulet("Amulette de feu I ({} UT)","RemovePV",3,2))#2 UT
        self.items.append(Amulet("Amulette de transformation du sac","ShuffleBackPack",1,1))    


    def getItemById(self, id):
        return self.items[id]

    #Méthode pour choisir un objet aléatoire dans la liste d'objets possibles
    def pickRandomItem(self):
        return self.items[randrange(0,len(self.items)-1)]
