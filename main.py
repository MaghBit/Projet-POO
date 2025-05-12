#Ce fichier est le point d'entrée du jeu qui gère la boucle principale du jeu donc le combat entre le joueur et l'ennemi en utilisant les classes définies dans les autres classes.
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

#Initialisation des personnages et du sac avec le joeur ayant des statistiques aléatoires
player = Player("Mathey",randint(12, 24),randint(1,10)) 
enemy = Enemy("Ghost In the Shell",0,0) 
backPack = BackPackHolder() 

#Sequence d'introduction
introSequence() 

#Initialisation de la bataille
initBattle(player,enemy,backPack) 

monde=LanceDe()
while(not player.isDead()):
    actionValidated = False 
    #Tour du joueur    
    while(not actionValidated):
        printBattleArena(player,enemy) 
        #choix de l'action avec la décision qui sera prise entre 0/1/2
        #0 = Attaquer, 1 = Ouvrir le sac, 2 = Fuir
        choice = chooseBattleActions(["Attaquer","Ouvrir le sac","Fuir"]) 
        resultat = None
        if choice == "Attaquer" or choice == "Fuir":
            #Lancer le dé pour savoir si l'attaque est un critique, normal, presque ou rate
            resultat = printdiceRollAnimation()
        #L'action choisie a été validée et on sort de la boucle pour continuer le combat
        actionValidated = fight(choice,player,enemy,backPack,resultat) 
        
    waitToResume() 
    
    #Verifier si l'enemi n'est pas mort
    if(enemy.isDead() == False):
        #Tour de l'enemi et création de l'arène de combat où l'ennemi attaque le joueur
        printBattleArena(player,enemy) 
        enemy.attack(player) 
        waitToResume() 
    else:
        currentRoundId += 1 
        nextRound(currentRoundId,player,backPack,enemy) 
        
        
gameOverAnimation(enemy,currentRoundId) 
