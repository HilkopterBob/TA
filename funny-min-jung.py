"""Main Module for Textadventure
"""
from Entities import Entity, EntityInit, gitem
from Level import Level,LevelInit
from Effect import Effect, EffectInit
from Utils import pr, Debug, Inp
from actionparser import Actionparser
from config import levels_file,entity_file,effects_file,dbg



def interact_with_level(player, level, level_list):
    """Current Game Interaction Function
    """
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    pr.dbg(f"Player: {player.name}, in Level: {level.name}")
    if level.name == "Menu":
        pr.n("\n"*5)
        pr.headline(level.descr)
        pr.n("\n"*2)
    else:
        pr.dbg(f"HUD")
        hud(player)
        #pr.n(level.descr)


        #Level Headers and Description
        level.printDesc()

    #Print Level Choices
    availableChoices = level.getAvailableChoices()
    for choice in availableChoices:
        print(f"{availableChoices.index(choice)+1}. {choice}")
    printed = True 

    pr.dbg(level.choices)

    if printed:
        action = int(Inp.inp()) - 1

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### #####
    pr.dbg("*"*20)
    pr.n(level.text[action][0])
    pr.dbg("*"*20)
    ####Is doing nothing ? 

    #Selecting index from available Actions
    if dbg:
        pr.dbg(f"All Actions: {level.text[action]}")
        pr.dbg(f"Available Actions: {level.getAvailableChoices()}")
    availableChoicesDict = dict(zip(availableChoices, level.text))

    if action < len(availableChoicesDict.keys()):
        actions = availableChoicesDict[availableChoices[action]]
        for i in actions:
            if actions[actions.index(i)] != "":
                actiontoadd = [actions[actions.index(i)].get("action"),[mPlayer,list(actions[actions.index(i)].values())[1]]]
                pr.dbg(f'Add {actiontoadd} to Actionstack for entity: {mPlayer}')
                mPlayer.actionstack.append(actiontoadd)


'''
            match actions[actions.index(i)]:
                    case "remove_effect_by_name":
                        if dbg:
                            pr.dbg("Case 1 Triggered")
                        player.remove_effect_by_name(str(availableChoices[action][i][keys[1]]))
                    case "change_location":
                        if dbg:
                            pr.dbg("Case 2 Triggered")
                        for llevel in level_list:
                            if llevel.name == str(availableChoices[action][i][keys[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "add_effect":
                        if dbg:
                            pr.dbg("Case 3 Triggered")
                        effect = EffectInit.load_effect_by_name_from_json(effects_file,
                                                        str(availableChoices[action][i]["effect_name"]))
                        player.add_effect(effect)
                    case _:
                       pass
                       # pr.dbg(f"{availableChoices[action][i][key[0]]} is not defined ")
'''









'''
    if len(availableChoices[action]) > 1:
        pr.dbg("Entering Loop")    
        pr.dbg(f"{availableChoicesDict}")


        i = 1
        while i < len(availableChoices[action]):
            keys = list(availableChoicesDict.keys())
            values = list(availableChoicesDict.values())
            pr.dbg(f"{keys}")
            pr.dbg(f"{values}")
            if "action" not in str(values[1]):
                for ddict in level.triggers:
                    if ddict.keys() == availableChoices[action][1].values():
                        try:
                            #Enumerate als refactor nutzen
                            triggered_dict = list(filter(lambda dict: dict.keys()
                                                        != availableChoices[action][1][key[0]],
                                                        level.triggers))
                            triggered_dict_index = level.triggers.index(triggered_dict[0])
                            level.triggers[triggered_dict_index] = availableChoices[action][1]
                        except IndexError as e:
                            pr.dbg(e)
                        pr.dbg(availableChoices[action][1])
                        pr.dbg(level.triggers)
            elif "action" in str(values[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                try:
                    pr.dbg(keys)
                    pr.dbg(availableChoices[action][i][keys[0]])
                    pr.dbg(availableChoices[action][i][keys[1]])
                except Exception as e:
                    pr.dbg(Exception)
                match availableChoices[action][i][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(str(availableChoices[action][i][keys[1]]))
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(availableChoices[action][i][keys[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "add_effect":
                        effect = EffectInit.load_effect_by_name_from_json(effects_file,
                                                        str(availableChoices[action][i]["effect_name"]))
                        player.add_effect(effect)
                    case _:
                        pr.dbg(f"{availableChoices[action][i][key[0]]} is not defined ")
            i = i + 1
'''

def hud(player):
    """Player Hud

    Args:
        player (Entity): The Player to which the Hud should be displayed
    """
    if Level.levelname(player.location) not in ("Menu","Options"):
        pr.n("+"*12+" "+"+"*12)
        pr.n(f"Du befindest dich in: {Level.levelname(player.location)}")
        if player.hp > 25:
            pr.g(f"HP: {player.hp}")
        else:
            pr.b(f"HP: {player.hp}")
        pr.n(f"Gold: {player.wealth}")
        pr.n(F"Level: {player.level} XP: {player.xp}")

def gameloop(player, level_list=None):
    """
        The Main Game Loop
    """

    if level_list is None:
        level_list = []

    lap = 0
    pr.dbg(f"Roundcount: {lap}")
    while True:
        pr.dbg(f"-"*50)
        for level in level_list:
            pr.dbg(f"Comparing Levelname: {level.name} to Player location: {Level.levelname(player.location)}")
            if level.name == Level.levelname(player.location):
                pr.dbg(f"{level}, {player}")
                if not player in level.entitylist:
                    pr.dbg(f"{player.name} not in {level.name} - adding {player.name} to {level.name} entitylist",1)
                    level.change_entity_list("+",player)
                current_level = level
        pr.dbg(f"-"*50)
        #Loop through all Entities in CurrentLevel and Apply Actionstack
        pr.dbg(f"Entitylist: {current_level.entitylist}")
        for e in current_level.entitylist:
            pr.dbg(f"Working Actionstack for {e.name}")
            pr.dbg(f"Actionstack: {e.actionstack}")
            #Work through actionstack of Entity and process actions
            for i in range(0,len(e.actionstack)):
                pr.dbg(f"#"*50)
                pr.dbg(f"Length of Actionstack: {len(e.actionstack)}")
                pr.dbg(f"Current Actionstack: {e.actionstack}")
                pr.dbg(f"Current Index: {i}")
                cur_action = e.actionstack.pop(0)
                Actionparser.callfunction(cur_action)
                pr.dbg(f"Cur_Action: {cur_action}")
                pr.dbg(f"Length of Actionstack after Action: {len(e.actionstack)}")
                pr.dbg(f"Current Actionstack after Action: {e.actionstack}")
                pr.dbg(f"#"*50)
                
        

        player.check_level_up()
        interact_with_level(player, current_level, level_list)
        #changes the entity location, deletes entity from old level and adds to the new one


        #Increase Lap Counter by i
        lap = lap + 1

        #Wait for Player Input
        Debug.pause()


if __name__ == "__main__":
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

    #Add Players
    mPlayer = Entity("Player", 100,100,0,
                    [gitem("Item1","weapon"),gitem("item2","misc")], location=allLevels[0])
    hurensohn = Entity("Hurensohn", 100,100,0,
                    [gitem("Item1","weapon"),gitem("item2","misc")], location=allLevels[2])


    #put Kopfschmerz Effect in Actionstack
    mPlayer.actionstack.append(["add_effect",[mPlayer,"Kopfschmerz"]])
    mPlayer.actionstack.append(["take_effects",[mPlayer,True]])

    gameloop(mPlayer, allLevels)
