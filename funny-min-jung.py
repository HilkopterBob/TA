from Entities import Entity, EntityInit, item, itemInit
from Level import Level, LevelInit
from Effect import Effect, EffectInit
from Utils import pr, Debug, Inp
import json
import hunter 
from actionparser import Actionparser
from config import *




def interact_with_level(player, level, level_list):
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    if level.name == "Menu":
        pr.n("\n"*5)
        pr.headline(level.descr)
        pr.n("\n"*2)
    else:
        hud(player)
        #pr.n(level.descr)
        for entry in level.descr:
            if len(entry) > 1:
                if type(entry) == str:
                    pr.n(f"{str(entry)}")
                    continue
                else:
                    if entry[1] in level.triggers:
                        pr.n(f"{str(entry[0])}")
                    continue

    for llist in level.choices:
        if len(llist) == 1 and llist[0] != "":
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
        action = int(Inp.inp()) - 1

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### ##### 

    pr.n(level.text[action][0])
    if len(level.text[action]) > 1:
        i = 1
        while i < len(level.text[action]):
            key = list(level.text[action][i].keys())




            if "action" not in str(key[0]):
                for ddict in level.triggers:
                    if ddict.keys() == level.text[action][1].keys():
                        try:
                            #Enumerate als refactor nutzen
                            triggered_dict = list(filter(lambda dict: dict.keys() != level.text[action][1][key[0]], level.triggers))
                            triggered_dict_index = level.triggers.index(triggered_dict[0])
                            level.triggers[triggered_dict_index] = level.text[action][1]
                        except IndexError as e:
                                pr.dbg(e)
                        pr.dbg(level.text[action][1])
                        pr.dbg(level.triggers)
            elif "action" in str(key[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                try:
                    pr.dbg(key)
                    pr.dbg(level.text[action][i][key[0]])
                    pr.dbg(level.text[action][i][key[1]])
                except Exception as e:
                    pr.dbg(Exception)
                match level.text[action][i][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(str(level.text[action][i][key[1]]))
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(level.text[action][i][key[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "add_effect":
                        effect = EffectInit.load_effect_by_name_from_json(effects_file, str(level.text[action][i]["effect_name"]))
                        player.add_effect(effect)
                    case _:
                        pr.dbg(f"{level.text[action][i][key[0]]} is not defined ")
            i = i + 1


def hud(player):
    if player.location != "Menu" and player.location != "Options":
        pr.n("+"*12+f" "+"+"*12)
        pr.n(f"Du befindest dich in: {player.location}")
        if player.hp > 25:
            pr.g(f"HP: {player.hp}")
        else:
            pr.b(f"HP: {player.hp}")
        pr.n(f"Gold: {player.wealth}")
        pr.n(F"Level: {player.level} XP: {player.xp}")

def gameloop(player, level_list=[]):
        
    lap = 0                                             #rundenanzahl
    #start of loop
    while True:
        #Loop through all Levels and check if Player is inside level   ---  TODO: FIX because unperformant
        for level in level_list:
            if level.name == player.location:
                current_level = level
        
        #Loop through all Entities in CurrentLevel and Apply Actionstack
        for e in current_level.entitylist:
            """
            Todo Action parser for actionstack (pass entity to which the action applies, 
            pass the action, process action on entity, return successfull or error)
            """
            #Work through actionstack of Entity and process actions
            for action in e.actionstack:
                pr.dbg(action)
                Actionparser.callfunction(action)
                e.actionstack.remove(action)
                
        player.check_level_up()                             #check for levelups and level up if enough xp
        interact_with_level(player, current_level, level_list)
        #changes the entity location, deletes entity from old level and adds to the new one
        

        #Increase Lap Counter by i
        lap = lap + 1

        #Wait for Player Input
        Debug.pause()


if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,[item("Item1","weapon"),item("item2","misc")], location="Menu")
    hurensohn = Entity("Hurensohn", 100,100,0,[item("Item1","weapon"),item("item2","misc")], location="Wiese")
    #mPlayer.set_name()
    kopfschmerz = Effect("Kopfschmerz","Kopfschmerzen halt.","bad", -1, "hp")
    heilung = Effect("heilung","Nö","good", 5, "hp")
    heilung2 = Effect("heilung2","Nö","good", 5, "hp")
    heilung3 = Effect("heilung 3","Nö","good", 5, "hp")
    terror = Effect("Terror","Nö","evil", -100, "xp")

    #Load all existing Levels
    print(levels_file)
    allLevels = LevelInit.load_all_levels_from_json(levels_file)
    Debug.objlist(allLevels, "Levels")

    #Load all existing Entities
    allEntities = EntityInit.load_entities_fromjson(entity_file)
    Debug.objlist(allEntities,"Entities")
    
    ###########################################
    #######___HOW TO USE ACTIONSTACK___########
    ###########################################
    ####Add actions to Player Actionstack
    # mPlayer.actionstack.put("Some Action from Actionstack")
    # mPlayer.actionstack.put("Another Action from Actionstack")
    # mPlayer.actionstack.put("And Another Action from Actionstack")
    # mPlayer.actionstack.put("let_effects_take_effect")

    #put Kopfschmerz Effect in Actionstack
    mPlayer.actionstack.append(["add_effect",[mPlayer,"Kopfschmerz"]])
    mPlayer.actionstack.append(["take_effects",[mPlayer,True]])

    gameloop(mPlayer, allLevels)
    
    

