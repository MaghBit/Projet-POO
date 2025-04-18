#Ce fichier a pour but de prendre en charge le sac du joueur
from Item import *
from ItemHolder import *
from Amulet import *

class BackPackHolder:
    def __init__(self):
        self.items=[]

    def getItemList(self):
        list = ""
        for i in self.items:
            list += i.getName
            list += "\n"
        return list
    
    def choosedItem(self):
        print("Objet dans le sac : ")
        i=0
        while(i<len(self.items)):
            print(i, self.items[i].getName())
            i+=1
        print("\n[99]Retour")

        choosed = -1
        while((choosed<0 or choosed>len(self.items)-1) and choosed != 99):
            try:
                print("\nLequel prendre?")
                choosed = int(input())
            except Exception as e:
                choosed = -1
        
        if(choosed == 99):
            return 'Back'
        
        choosedItem = self.items[choosed]
        

        if(choosedItem.__class__.__name__ == "Amulet"):
            choosedItem.ItemUsed()
            if choosedItem.isUsedMax():
                self.removeItem(choosed)
        else:
            self.removeItem(choosed)
        return choosedItem
        
    def storeItem(self, itemtostore):
        self.items.append(itemtostore)
        
    def removeItem(self,id):
        self.items.pop(id)
        
    def getItemById(self,id):
        return self.items[id]
        
    def getItemCount(self):
        return len(self.items)