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


def interact_with_level(player, level):
    printed = False
    i = 1
    pr.n(level.descr)
    for llist in level.choices:
        if len(llist) == 1:
            pr.n(f"{i}. {llist[0]}")
            printed = True
            i = i + 1
        elif len(llist) > 1:
            for ddict in level.triggers:
                if llist[1] == ddict:
                    pr.n(f"{i}. {llist[0]}")
                    printed = True
                    i = i + 1
    if printed == True:
        action = pr.inp()
        #try:
        pr.n(level.text[int(action) - 1][0])
    
        if len(level.text[int(action) - 1]) > 1:
            key = list(level.text[int(action) - 1][1].keys())
            #print(key)
            for ddict in level.triggers:
                if ddict.keys() == level.text[int(action) - 1][1].keys():
                    #level.triggers.keys == level.text[int(action) - 1][1]
                    #level.triggers = list (filter(lambda d: d[key[0]] != level.text[int(action) - 1][1], level.triggers))
                    try:
                        triggered_dict = list(filter(lambda dict: dict[key[0]] != level.text[int(action) - 1][1][key[0]], level.triggers))
                        triggered_dict_index = level.triggers.index(triggered_dict[0])
                        level.triggers[triggered_dict_index] = level.text[int(action) - 1][1]
                    except IndexError as e:
                        if dbg:
                            pr.dbg(e)
                    print(level.text[int(action) - 1][1])
                    print(level.triggers)
                    #FUNKTIONIERT!!! refactor incoming...
        # except:
        #     pr.b("Deine Eingabe war falsch.")



def hud(player):
    pr.n(f"Du befindest dich in: {player.location}")
    pr.n(f"Gold: {player.wealth}")
    pr.n(F"Level: {player.level} XP: {player.xp}")


def gameloop(player, level_list=[]):
        
    lap = 0                                             #rundenanzahl
    while True:
        for level in level_list:
            if level.name == player.location:
                current_level = level

        
        for e in current_level.entitylist:
            for a in list(e.actionstack.queue):
                pr.dbg(a)
        ###Todo Action parser for actionstack (pass entity to which the action applies, pass the action, process action on entity, return successfull or error)
        ##############################################

        hud(player)                                         #basic hud
        player.let_effects_take_effect(dbg)                 #effects 
        player.check_level_up()                             #check for levelups and level up if enough xp
        interact_with_level(player, current_level)
        if player.location != "Wiese":
            player.change_location(level_list[0],level_list[2]) #changes the entity location, deletes entity from old level and adds to the new one
        


        lap = lap + 1
        pr.pause()







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
    #mPlayer.add_effect(terror)
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
    nirvana = Level(["Du siehst einen Weg.",], ["Atmen", "Den Wen entlanggehen"],"Nirvana", [], "Testtype", "nirvana",[mPlayer])                  #hier chillen entitys die existieren ohne in einem level eingesetzt zu werden
    nowhere = Level([""], [],"nowhere", [], "Testtype", "nowhere",[])                         #Hommage für alte Textadventures
    newnewLevel = Level(["Du siehst einen Weg, der ins Nirvana führt."], ["Nachdenken","Ins Nirvana gehen"],"NewNewLevel", [], "Testtype", "NewNewLevel",[])
    wiese = Level([["die erste option zeigt diesen text"],[ "die zweite option zeigt diesen text",{"trigger03":True}],["dritte option"]],[["erste option"],["zweite option"],["dritte option",{"trigger03":True}]],"Wiese",descr="Das ist die Beschreibung einer Wiese.", triggers=[{"trigger03":False}])
    ####Run Gameloop with nirvana as Level
    gameloop(mPlayer, [nirvana, newnewLevel,wiese])
    
    