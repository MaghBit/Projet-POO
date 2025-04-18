
from UiHandler import * 

from MobHolder import * 
from CombatActionHandler import * 

from BackPackHolder import * 
from Item import * 
from Potion import * 
from ItemHolder import * 

from Personnage import * 
from Enemy import * 
from Player import * 

from LancerDe import LanceDe
from random import randint


currentRoundId = 1

player = Player("Mathey",randint(12, 24),randint(1,10)) 
enemy = Enemy("Ghost In the Shell",0,0) 
backPack = BackPackHolder() 

#Sequence d'introduction
introSequence() 

#Initialisation
initBattle(player,enemy,backPack) 

monde=LanceDe()
while(not player.isDead()):
    actionValidated = False 
    #Tour du joueur    
    while(not actionValidated):
        printBattleArena(player,enemy) 

        choise = chooseBattleActions(["Attaquer","Ouvrir le sac","Fuir"]) 
        resultat = None
        if choise == "Attaquer" or choise == "Fuir":
            resultat = printdiceRollAnimation()
        actionValidated = fight(choise,player,enemy,backPack,resultat) 
        
    waitToResume() 
    
    #Verifier si l'enemi n'est pas mort
    if(enemy.isDead() == False):
        #Tour de l'enemi
        printBattleArena(player,enemy) 
        enemy.attack(player) 
        waitToResume() 
    else:
        currentRoundId += 1 
        nextRound(currentRoundId,player,backPack,enemy) 
        
        
gameOverAnimation(enemy,currentRoundId) 