#fichier qui s'occupe de l'affichage de l'interface
import time
import sys
from LancerDe import LanceDe

#Cette méthode permet de sauter des lignes pour nettoyer l'écran
def clearScreen():
    print("\n"*100)

def createSymbolMultiple(length,symbol):
    string = ""
    i = 0
    while (i<length):
        string += symbol
        i += 1
    return string   

#Cette méthode permet de créer une bannière pour afficher les stats du joueur et de l'ennemi
def createBattleStatSquare(fighter,size):
    
    #La banière avec le nom    
    drawed = "|{}|\n".format(fighter.getName())
    
    #Le haut
    drawed += "*"
    drawed += createSymbolMultiple(size,'-')
    drawed += "*\n"
    
    #Une ligne écart
    drawed += "|"
    drawed += createSymbolMultiple(size,' ')
    drawed += "|\n"
    
    #Ecrire les infos
    drawed += "|"
    tempInfo = "Pv : {}".format(fighter.getPv())
    drawed += tempInfo
    drawed += createSymbolMultiple(size-len(tempInfo)," ")
    drawed += "|\n"
    
    drawed += "|"
    tempInfo = "Ad : {}".format(fighter.getattackdmg())
    drawed += tempInfo
    drawed += createSymbolMultiple(size-len(tempInfo)," ")
    drawed += "|\n"
    
    #Une ligne écart
    drawed += "|"
    drawed += createSymbolMultiple(size,' ')
    drawed += "|\n"
    
    #Le bas
    drawed += "*"
    drawed += createSymbolMultiple(size,'-')
    drawed += "*\n"

    return drawed

#Cette méthode permet d'afficher les stats du joueur et de l'ennemi
def printBattleArena(player,enemy):
    clearScreen()
    
    print(createBattleStatSquare(player,14))
        
    print(createBattleStatSquare(enemy,14))


#Cette méthode permet d'afficher, à la fin de chaque round, une animation de transition
def nextRoundAnimation(roundId,player,enemy,newEnemy,obtainedItem=None):
    
     #Round Suivant
    clearScreen() 
    if(roundId > 1):
        printTextAnimation("Félicitation Aventurier {}, vous avez vaincu {} !!\nMais des ennemis plus forts encore vous attendent, peut-être...".format(player.getName(), enemy.getName().lower())) 
        if obtainedItem:
            printTextAnimation("\nVous obtenez un(e) {}".format(obtainedItem.getName().lower())) 
        sys.stdout.flush() 
        time.sleep(1) 
    
 
    printTextAnimation("\n\n----====Round {}====----\n".format(roundId))   
    sys.stdout.flush() 
    
    #Texte   
    introText = "{} vous barre la route !".format(newEnemy.getName())
    printTextAnimation(introText)
    sys.stdout.flush()
    time.sleep(3)

#Cette méthode est la méthode principale qui gère le choix de l'action du joueur. Elle affiche les actions possibles et demande à l'utilisateur de choisir une action.
def chooseBattleActions(possibleAction):
   
    print("Actions possibles : ")
    
    i = 0 
    while(i<len(possibleAction)):
        print(("[{}]{}".format(i,possibleAction[i]))) 
        i += 1

    print("\nQue Faire ?")     
    choosed = -1
    while(choosed<0 or choosed>len(possibleAction)-1):
        try:
           choosed = int(input())
        except ValueError:
            continue

        
    
    return possibleAction[choosed]   

#Cette méthode permet d'afficher un message pour demander à l'utilisateur d'appuyer sur Entrée pour continuer
def waitToResume():
    print("Appuyer sur Entrée pour continuer...")
    input()

#Cette méthode permet d'afficher un texte lettre par lettre avec un délai entre chaque lettre
def printTextAnimation(textToPrint,delay = 0.05):
    for letter in textToPrint:
        print(letter, end="")
        time.sleep(delay)

#Cette méthode permet de lancer un dé à 20 faces et d'afficher le résultat
def printdiceRollAnimation():
        """
        Lance un dé à 20 faces et renvoie le résultat"""
        clearScreen() 
        monde=LanceDe()
        resultat = monde.lanceDe()
        print("Lancer de Dé ")
        print("┌----------┐")
        print("|          |")
        print( resultat  )
        print("|          |")            
        print("└----------┘")
        return resultat

#Cette méthode permet d'afficher le message de début de jeu
def introSequence():
    clearScreen()
    printTextAnimation("""⠀                      ⢀⡴⠞⠛⠉⢙⡛⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⢰⠁⠀⠀⠉⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠜⢹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡶⠶⠮⠭⠵⢖⠒⠿⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡶⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣄⡀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠚⠿⡷⣄⣀⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠪⣻⣄⠀⠀⠀⣀⣀⠤⠴⠒⠚⢋⣭⣟⣯⣍⠉⠓⠒⠦⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡝⣧⠔⠋⠁⠀⣀⠤⠔⣶⣿⡿⠿⠿⠿⠍⠉⠒⠢⢤⣀⠈⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡦⠤⢤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣞⣧⠤⠒⠉⠀⠀⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢲⣴⣾⣷⢤⡀⠀⠀⠀⠀⠀⠀⠀
⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⢿⣿⣧⠙⢦⠀⠀⠀⠀⠀⠀
⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⣄⡀⠀⠐⢄⠀⠀⠀⢻⡇⠀⠀⠀⠀⡠⢊⣭⣬⣭⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡀⠀⠑⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠑⢄⣀⢿⠇⠀⠀⠀⡜⣼⠟⠁⠀⠀⠉⢿⡄⠀⠀⠀⠀⣠⠤⠤⠤⣀⡀⠈⠙⡄⠀⠈⢆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣝⢦⡀⠀⣠⡞⠢⢄⠀⡜⣼⠁⣠⣴⣶⢦⡀⠀⢻⠀⠀⢀⣎⡴⠟⠛⠛⠶⣝⢦⠀⠘⡄⠀⠈⢧⠀⠀
⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⢻⡾⠋⠀⣀⣀⠁⠁⡇⢰⢿⣄⣿⣎⢷⠀⢸⡇⠀⢸⡝⢀⣤⣄⡀⠀⠙⢷⡀⠀⢱⠀⠀⠈⡇⠀
⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠈⠙⣳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣧⠀⢀⣀⣀⡉⠱⣿⣼⣆⢿⠻⣯⡞⠀⢸⡇⠀⢸⣷⣏⢙⣿⡻⡆⠀⠀⢳⠀⠀⠀⠀⠀⢸⡀
⠀⢳⡀⠀⠀⠀⠀⠀⠉⠚⠁⠀⠀⠀⠀⠀⠉⠻⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠈⠁⠀⠀⠉⠢⠈⠛⢻⣿⠿⠛⠁⢀⣿⠇⠀⠈⣿⣿⢿⡟⣧⡷⠀⠀⢸⡄⠀⠀⠀⠀⠈⡇
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⢧⡀⠀⠀⠀⠢⠤⠔⡽⠁⠚⠉⠉⠉⢗⢷⣄⡠⣀⢻⣆⣀⣠⡿⠋⠀⠀⠀⠈⢿⡷⠿⠟⠁⠀⠀⣼⠀⠀⠀⠀⠀⠀⢱
⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠻⡄⠀⢀⣀⡤⠞⠁⠀⠀⠀⠀⠀⠘⢦⡈⠁⠀⠀⠸⡟⠉⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣤⡶⠟⠉⠙⠒⠀⠀⠀⠀⢘
⠀⠀⠀⠀⠈⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⡇⣿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣤⡀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠍⠠⠤⠒⠂⢄⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠈⠙⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⣽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣉⡿⠓⠲⠄⠀⠀⠀⠀⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣤⣄⣀⣠⣤⡤⠶⠛⣿⡀⠀⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣄⠀⠀⠉⠙⠒⠲⠤⠤⠤⣤⣤⡤⠖⠚⠁⠀⠀⠀⠀⠀⠀⠀⢰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣦⣄⡀⠀⠀⠀⢀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⡀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡱⡀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣔⢹⡉⢻⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣥⣠⣹⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣕⢄⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⠌⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⡦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠺⢕⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠤⢄⣀⣀⣀⣀⣀⣀⣠⠤⠴⠒⠊⠉    ⠀⠀⠀
    
                                 *------------------------*
                                 |  Chances You'll move   |
                                 *------------------------*                         
    
    """,0.01)
    print("")
    sys.stdout.flush()
    time.sleep(1)

#Cette méthode permet d'afficher le message de fin de jeu
def gameOverAnimation(enemy,currentRoundId):
    print(enemy.getName(), "vous blesse et termine la bataille en vous donnant le cancer....\nVous êtes mort après ",currentRoundId," bataille(s)...")
