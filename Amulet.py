from Item import *

class Amulet(Item):
    def __init__(self,name,effect,actionPoints,maxUseTime):
        Item.__init__(self, name)
        self.effect=effect
        self.actionPoints=actionPoints
        self.remainingUse=maxUseTime
        self.maxUseTime=maxUseTime

    def getName(self):
        if(self.maxUseTime == 1):
            return Item.UseItem(self)
        return Item.getName(self).format(self.remainingUse) 
        #Cette méthode ajoute des détails sur l'état de l'amulette(Amulette magique (3 utilisations restantes) par exemple)
        
    def getEffect(self):
        return self.effect
    
    def getActionPoints(self):
        return self.actionPoints
    
    def getRemainingUse(self): 
        return self.remainingUse
    
    def ItemUsed(self):
        self.remainingUse -= 1

    def isUsedMax(self):
        return  self.remainingUse <= 0
    
    def getUseTime(self):
        return self.maxUseTime