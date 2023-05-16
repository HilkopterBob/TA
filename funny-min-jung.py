"""Main Module for Textadventure
"""
from Entities import Entity, EntityInit, gitem
from Level import LevelInit
from Effect import Effect, EffectInit
from Utils import Pr, Debug, Inp
from actionparser import Actionparser
from config import levels_file,entity_file,effects_file




def interact_with_level(player, level, level_list):
    """Current Game Interaction Function
    """
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    if level.name == "Menu":
        Pr.n("\n"*5)
        Pr.headline(level.descr)
        Pr.n("\n"*2)
    else:
        hud(player)
        #Pr.n(level.descr)
        for entry in level.descr:
            if len(entry) > 1:
                if isinstance(entry,str):
                    Pr.n(f"{str(entry)}")
                    continue
                if entry[1] in level.triggers:
                    Pr.n(f"{str(entry[0])}")
                continue

    for llist in level.choices:
        if len(llist) == 1 and llist[0] != "":
            Pr.n(f"{i}. {llist[0]}")
            printed = True
            i = i + 1
        elif len(llist) > 1:
            for ddict in level.triggers:
                if llist[1] == ddict:
                    Pr.n(f"{i}. {llist[0]}")
                    printed = True
                    i = i + 1
    if printed:
        action = int(Inp.inp()) - 1

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### #####

    Pr.n(level.text[action][0])
    if len(level.text[action]) > 1:
        i = 1
        while i < len(level.text[action]):
            key = list(level.text[action][i].keys())




            if "action" not in str(key[0]):
                for ddict in level.triggers:
                    if ddict.keys() == level.text[action][1].keys():
                        try:
                            #Enumerate als refactor nutzen
                            triggered_dict = list(filter(lambda dict: dict.keys()
                                                        != level.text[action][1][key[0]],
                                                        level.triggers))
                            triggered_dict_index = level.triggers.index(triggered_dict[0])
                            level.triggers[triggered_dict_index] = level.text[action][1]
                        except IndexError as e:
                            Pr.dbg(e)
                        Pr.dbg(level.text[action][1])
                        Pr.dbg(level.triggers)
            elif "action" in str(key[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                try:
                    Pr.dbg(key)
                    Pr.dbg(level.text[action][i][key[0]])
                    Pr.dbg(level.text[action][i][key[1]])
                except Exception as e:
                    Pr.dbg(Exception)
                match level.text[action][i][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(str(level.text[action][i][key[1]]))
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(level.text[action][i][key[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "add_effect":
                        effect = EffectInit.load_effect_by_name_from_json(effects_file,
                                                        str(level.text[action][i]["effect_name"]))
                        player.add_effect(effect)
                    case _:
                        Pr.dbg(f"{level.text[action][i][key[0]]} is not defined ")
            i = i + 1


def hud(player):
    """Player Hud

    Args:
        player (Entity): The Player to which the Hud should be displayed
    """
    if player.location not in ("Menu","Options"):
        Pr.n("+"*12+" "+"+"*12)
        Pr.n(f"Du befindest dich in: {player.location}")
        if player.hp > 25:
            Pr.g(f"HP: {player.hp}")
        else:
            Pr.b(f"HP: {player.hp}")
        Pr.n(f"Gold: {player.wealth}")
        Pr.n(F"Level: {player.level} XP: {player.xp}")

def gameloop(player, level_list=None):
    """
        The Main Game Loop
    """
    if level_list is None:
        level_list = []

    lap = 0
    while True:
        for level in level_list:
            if level.name == player.location:
                current_level = level

        #Loop through all Entities in CurrentLevel and Apply Actionstack
        for e in current_level.entitylist:
            #Work through actionstack of Entity and Process actions
            for action in e.actionstack:
                Pr.dbg(action)
                Actionparser.callfunction(action)
                e.actionstack.remove(action)

        player.check_level_up()
        interact_with_level(player, current_level, level_list)
        #changes the entity location, deletes entity from old level and adds to the new one


        #Increase Lap Counter by i
        lap = lap + 1

        #Wait for Player Input
        Debug.pause()


if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,
                    [gitem("Item1","weapon"),gitem("item2","misc")], location="Menu")
    hurensohn = Entity("Hurensohn", 100,100,0,
                    [gitem("Item1","weapon"),gitem("item2","misc")], location="Wiese")
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
