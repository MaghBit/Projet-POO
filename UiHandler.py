import time
import sys
from LancerDe import LanceDe

def clearScreen():
    print("\n"*100)

def createSymbolMultiple(length,symbol):
    string = ""
    i = 0
    while (i<length):
        string += symbol
        i += 1
    return string   

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

def printBattleArena(player,enemy):
    clearScreen()
    
    print(createBattleStatSquare(player,14))
        
    print(createBattleStatSquare(enemy,14))



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

def waitToResume():
    print("Appuyer sur Entrée pour continuer...")
    input()


def printTextAnimation(textToPrint,delay = 0.05):
    for letter in textToPrint:
        print(letter, end="")
        time.sleep(delay)

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

def gameOverAnimation(enemy,currentRoundId):
    print(enemy.getName(), "vous blesse et termine la bataille en vous donnant le cancer....\nVous êtes mort après ",currentRoundId," bataille(s)...")