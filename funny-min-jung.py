#ToDo's:
#Spielerklasse
#Levelklasse
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from Entities import Entity, item, itemInit
from Level import Level
from Effect import Effect
import Utils as pr 
import json

##################
##Debug Variable##
dbg = True
##################

###################
###ENV Variables###
items_file = "config/items.json"
lvl = 0
action = ""
###################


def gameloop(player, level):

        print("*"*10 + "player" + "*"*10 + "\n")
        print(vars(player))
        print("*"*10 + "level" + "*"*10 + "\n")
        print(vars(level))
        print("*"*26 + "\n")

        ##### ##### ##### #####

        #Effects:





if __name__ == "__main__":
    mPlayer = Entity("Blankoname", 100,100,0,[item("Item1","weapon"),item("item2","misc")])
    #mPlayer.set_name()
    vergiftung = Effect("Vergiftung","Nö","bad", -2, "health")
    print(vars(vergiftung))
    mPlayer.add_effect(vergiftung)
    mPlayer.show_effects()
    allItems = itemInit.load_all_items_from_json(items_file)
    print(vars(itemInit.load_item_by_name_from_json(items_file, "Sword")))
    print()
    menu = Level(["Textadventure","Hauptmenü","spiel wird geladen"],["Spiel laden","Spiel starten","Spiel beenden"],"Hauptmenü",[],"zivilisiert","Mainmanu descr")

    

    gameloop(mPlayer, menu)

