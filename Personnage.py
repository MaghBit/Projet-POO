class Personnage:
    def __init__(self,name,pv,attackdmg):
        self.name=name;
        self.pv=pv;
        self.attackdmg=attackdmg;
    
    def getDamage(self,damage):
        self.pv -= damage
        if self.pv <0:
            self.pv=0
            
    def attack(self,victim, boost=1):
        dmg = round(self.getattackdmg()*boost)
        print("{} attaque {} ({} points de degat(s))".format(self.getName(),victim.getName(),dmg))
        victim.getDamage(dmg)
        
        
    def modifyStat(self,name,value):
        if(name == "PV"):
            self.pv += value
            
        if(name == "AD"):
            self.pv += value
                
    def getName(self):
        return self.name

           
    def getPv(self):
        return self.pv
        
    def getattackdmg(self):
        return self.attackdmg
    
    def getStat(self):
       return ("{} possède actuellement {} points de vies, et attaque avec une force de {} points".format(self.getName(),self.getPv(),self.getattackdmg()))
    
    def isDead(self):
        if(self.pv<0 or self.pv==0):
            return True
        return False