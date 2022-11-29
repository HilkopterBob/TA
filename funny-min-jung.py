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
global dbg
dbg = True
##################

###################
###ENV Variables###
items_file = "config/items.json"
lvl = 0
action = ""
###################





def gameloop(player, level=""):
        
        print("*"*10 + "player" + "*"*10 + "\n")
        print(vars(player))
        
        
        
        ####Work Actionstack for each Entity in Level
        for e in level.entitylist:
                for a in list(e.actionstack.queue):
                        pr.dbg(a)
                        ###Todo Action parser for actionstack (pass entity to which the action applies, pass the action, process action on entity, return successfull or error)
        ##############################################
        
        
        
        ##### ##### ##### #####

        #Effects:
        player.let_effects_take_effect(dbg)







if __name__ == "__main__":
        mPlayer = Entity("Blankoname", 100,100,0,[item("Item1","weapon"),item("item2","misc")])
        #mPlayer.set_name()
        vergiftung = Effect("Vergiftung","Nö","bad", -10, "hp")
        heilung = Effect("heilung","Nö","good", 5, "hp")
        heilung2 = Effect("heilung2","Nö","good", 5, "hp")
        heilung3 = Effect("heilung 3","Nö","good", 5, "hp")
        terror = Effect("Terror","Nö","evil", -100, "xp")
        #print(vars(vergiftung))
        mPlayer.add_effect(vergiftung)
        mPlayer.add_effect(heilung)
        mPlayer.add_effect(heilung2)
        mPlayer.add_effect(heilung3)
        mPlayer.add_effect(terror)
        # mPlayer.show_effects()
        #print(mPlayer.effects)
        #allItems = itemInit.load_all_items_from_json(items_file)
        #print(vars(itemInit.load_item_by_name_from_json(items_file, "Sword")))
        #print()
        #menu = Level(["Textadventure","Hauptmenü","spiel wird geladen"],["Spiel laden","Spiel starten","Spiel beenden"],"Hauptmenü",[],"zivilisiert","Mainmanu descr")
        #gameloop(mPlayer, menu)
        
        
        ####Add actions to Player Actionstack
        mPlayer.actionstack.put("Some Action from Actionstack")
        mPlayer.actionstack.put("Another Action from Actionstack")
        mPlayer.actionstack.put("And Another Action from Actionstack")
        
        ####Create a New Level with Player as only Entity in Level
        newLevel = Level([], [],"NewLevel", [], "Testtype", "NewLevel",[mPlayer])

        ####Run Gameloop with newLevel as Level
        gameloop(mPlayer, newLevel)

