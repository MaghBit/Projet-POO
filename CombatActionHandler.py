#Ce fichier gère les actions du joueur lors du combat. Il permet d'attaquer, fuir et ouvrir le sac/utiliser un objet. Il gère également tous ce qui est lié à inventaire du personnage.
from BackPackHolder import *

from Item import *
from Amulet import *
from Potion import *

from Enemy import *
from MobHolder import *

from UiHandler import *
from LancerDe import *
##### Action : attaquer
def fight(action,player: Personnage,enemy: Personnage,backPack: BackPackHolder, de = None):
    if(action == "Attaquer"):
        #Lancer le dé pour s'avoir si le joueur touche
        if de=="rate":
            print("Vous ratez votre attaque !")
        else:
            boost = 1
            if de=="critique":
                print("Vous infligez un coup ciritique !")
                boost = 1.5
            elif de=="normal":
                print("Vous mettez un coup avec succés !")
            elif de=="presque":
                print("Vous trébuchez sur vos pas")
                boost = 0.8
            player.attack(enemy, boost)
            
    ##### Action : fuir
    elif action == "Fuir":
        if de=="critique":
            enemy.getDamage(999)
            print(" Vous fuyez avec succès comme un trouillard \n Personne ne le saura !")
        else:

            print("Vous ne pouvez pas fuir !")


    ##### Action : Ouvrir le sac
    elif(action == "Ouvrir le sac"):
        
        clearScreen()

        print("Vous ouvrez  le sac")
        choosedItem=backPack.choosedItem()
        if(choosedItem.__class__.__name__=="str"):
            return False       
        
        ############Si l'item est une potion
        if(choosedItem.__class__.__name__ == 'Potion'):
            print("Vous utilisez la {}.".format(choosedItem.getName().lower()), end='')
            dmg = choosedItem.getActionPoints()

            de = printdiceRollAnimation()

            #La potion n'a pas d'effet
            if de=="rate":
                print("Mais cela a échoué !")
            
            else:
                #si l'effet de la potion est bénéfique
                boost = 1
                if choosedItem.getIsBenefic():
                    print("Vous gagnez {} points de vies !".format(dmg))
                    
                    if de == "critique":
                        boost = 1.5
                        print("Ca vous a donné plus de PV que davantage !")

                    elif de == "presque":
                        boost = 0.8
                        print("Mais la potion avait un goût amer !")
                    player.pv += round(dmg*boost)
                    
                else:
                    #si l'effet de la potion est néfaste
                    print("Vous lancez la potion sur {}.".format(enemy.getName().lower()))

                    if de == "critique":
                        boost = 1.5
                        print("Coup critique !")

                    elif de == "presque":
                        boost = 0.8
                        print("Mais cela n'a pas fait grand chose !")
                    player.pv += round(dmg*boost)

                    print("{} pert {} points de vies !".format(enemy.getName().lower(),choosedItem.getActionPoints()))
                    enemy.pv -= choosedItem.getActionPoints()   
                    
        

        ############Si l'item est une Amulette
        elif(choosedItem.__class__.__name__ == "Amulet"):
            print("Vous utilisez ",choosedItem.getName()," qui brille dans le noir. ")

            #Si l'effet régénère des points de vie
            if(choosedItem.getEffect() == "RestorePV"):
                print("Vous recuperez ",choosedItem.getActionPoints() ,"point(s) de vie !")
                player.pv += choosedItem.getActionPoints()
            #Si l'effet fait des dégats
            elif(choosedItem.getEffect() == "RemovePV"):
                print("Elle dégage une vague d'énérgie qui blesse ",enemy.getName()," ! ",enemy.getName(), "pert" ,choosedItem.getActionPoints(), "points de vies")
                enemy.pv -= choosedItem.getActionPoints()

            #Si l'effet est le mélange du sac
            elif(choosedItem.getEffect() == "ShuffleBackPack"):
                print("Vous sentez votre sac bouger..... Tout vos objects ont été changés !")

                toGenerate = backPack.getItemsCount()
                print(toGenerate)
                i = 0
                while (i < toGenerate):
                    backPack.removeItem(0)
                    i += 1
                i = 0
                while (i < toGenerate):
                    backPack.storeItem(ItemHolder().pickRandomItem())
                    i += 1

    
    return True
    

#Cette fonction initialise la bataille en créant un nouvel ennemi et en ajoutant deux objets aléatoires au sac du joueur.
def initBattle(player,enemy,backPack):
    #Creer le nouvel ennemis
    newEnemy = MobHolder().pickRandomMob()  
    enemy.receiveNewEnemy(newEnemy);    

    #Mettre en place le sac, et y ajouter deux items aléatoires
    backPack.storeItem(ItemHolder().pickRandomItem())
    backPack.storeItem(ItemHolder().pickRandomItem())
    
    #Lancer l'animation du round
    nextRoundAnimation(1,player,backPack,enemy,newEnemy)

#Cette fonction gère la fin du round et le passage au round suivant. Elle permet de créer un nouvel ennemi et d'ajouter un objet aléatoire au sac du joueur.
def nextRound(currentRoundId,player,backPack,enemy):
    obtainedItem = None
    if random.random()*100 > 50:
        obtainedItem = ItemHolder().pickRandomItem()
        backPack.storeItem(obtainedItem)   
    
    newEnemy = MobHolder().pickRandomMob()
    
    nextRoundAnimation(currentRoundId,player,enemy,newEnemy,obtainedItem);        
        
    enemy.receiveNewEnemy(newEnemy)
