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





def gameloop(player, level=[]):
    
    #print("*"*10 + "player" + "*"*10 + "\n")
    #print(vars(player))
    
    level_index = 0             #Index that corresponds to level from level[]
    
    while True:

        current_level = level[level_index]

        for e in current_level.entitylist:
            for a in list(e.actionstack.queue):
                pr.dbg(a)
        ###Todo Action parser for actionstack (pass entity to which the action applies, pass the action, process action on entity, return successfull or error)
        ##############################################

        nirvana.change_entity_list("-", mPlayer)
        newnewLevel.change_entity_list("+", mPlayer)
        mPlayer.change_location("")
    
    
    ##### ##### ##### #####

    #Effects:
        player.let_effects_take_effect(dbg)







if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,[item("Item1","weapon"),item("item2","misc")])
    h = Entity()
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
    mPlayer.actionstack.put("let_effects_take_effect")
    
    ####Create a New Level with Player as only Entity in Level
    nirvana = Level(["Möchtest du ins NewNewLevel?"], ["Yes","No"],"nirvana", [], "Testtype", "nirvana",[mPlayer])                  #hier chillen entitys die existieren ohne in einem level eingesetzt zu werden
    nowhere = Level([], [],"nowhere", [], "Testtype", "nowhere",[])                         #Hommage für alte Textadventures
    newnewLevel = Level([], [],"NewNewLevel", [], "Testtype", "NewNewLevel",[])
    ####Run Gameloop with nirvana as Level
    gameloop(mPlayer, [nirvana, newnewLevel])
    
    