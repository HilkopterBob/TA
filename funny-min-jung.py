"""Main Module for Textadventure
"""
from Entities import Entity, gitem
from Level import Level
from Effect import Effect
from Utils import Pr, Debug, Inp
from actionparser import Actionparser
from Assethandler import AssetHandler



def interact_with_level(player, level, level_list):
    """Current Game Interaction Function"""
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    Pr.dbg(f"Player: {player.name}, in Level: {level.name}")
    if level.name == "Menu":

        Pr.n("\n"*5)
        Pr.headline(level.descr)
        Pr.n("\n"*2)
    else:
        Pr.dbg("HUD")
        hud(player)
        #pr.n(level.descr)


        #Level Headers and Description
        level.printDesc()

    #Print Level Choices
    availableChoices = level.getAvailableChoices()
    Pr.dbg(availableChoices, 1)
    for choice in availableChoices:
        print(f"{availableChoices.index(choice)+1}. {choice}")
    printed = True

    Pr.dbg(level.choices)

    if printed:
        action = int(Inp.inp()) - 1

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### #####
    #Pr.dbg("*"*20)
    #pr.n(level.text[action][0])
    #Pr.dbg("*"*20)
    ####Is doing nothing ?

    #Selecting index from available Actions
    Pr.dbg(availableChoices, 2)
    Pr.dbg(f"All Actions: {availableChoices[action]}")
    Pr.dbg(f"Available Actions: {level.getAvailableChoices()}")
    availableChoicesDict = dict(zip(availableChoices, level.text)) # Sehr falsch, Index Choice 2 wird text 1 zugeordnet
    Pr.dbg(availableChoicesDict, 2)
    #Link Choices - result test

    if action < len(availableChoicesDict.keys()):
        actions = availableChoicesDict[availableChoices[action]]
        for i in actions:
            _currentAction = actions[actions.index(i)]
            if _currentAction != "":
                if isinstance(_currentAction,str):
                    Pr.n(_currentAction)
                else:
                    try:
                        try:
                            if "action" in _currentAction.keys():
                                if _currentAction.get("action") == "change_location":
                                    for level in level_list:
                                        if level.name == list(_currentAction.values())[1]:
                                            actiontoadd = [_currentAction.get("action"),
                                                            [mPlayer,mPlayer.location,level]]
                                else:
                                    actiontoadd = [_currentAction.get("action"),
                                                    [mPlayer,list(_currentAction.values())[1]]]
                            else:
                                Pr.dbg(f"No Action in Keys: {_currentAction}", 1)
                                #Do Trigger Stuff
                                touched_trigger = actions[-1] # Letzter eintrag aus actions = immer Trigger. Supported nur einen Trigger!!!
                                level_triggers_list = level.triggers
                                Pr.dbg(level_triggers_list, 2)
                                for index, l_trigger in enumerate(level_triggers_list):
                                    if l_trigger.keys() == touched_trigger.keys():
                                        level_triggers_list[index] = touched_trigger
                            Pr.dbg(f'Add {actiontoadd} to Actionstack for entity: {mPlayer}')
                            mPlayer.actionstack.append(actiontoadd)
                        except Exception as e:
                            Pr.dbg(f"ERR: {e}", 2)
                    except:
                        Pr.dbg(f"CurrentAction: {_currentAction}", 2)

def hud(player):
    """Player Hud

    Args:
        player (Entity): The Player to which the Hud should be displayed
    """
    if Level.levelname(player.location) not in ("Menu","Options"):
        Pr.n("+"*12+" "+"+"*12)
        Pr.n(f"Du befindest dich in: {Level.levelname(player.location)}")
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
    current_level = Level
    if level_list is None:
        level_list = []

    lap = 0
    while True:

        Pr.dbg("-"*50)
        for level in level_list:
            Pr.dbg(f"Comparing Levelname: {level.name} "
                    f"to Player location: {Level.levelname(player.location)}")
            if str(level.name) == str(Level.levelname(player.location)):
                Pr.dbg(f"Player location ({Level.levelname(player.location)}) "
                        f"is equal to Level ({level.name}), ")
                if not player in level.entitylist:
                    Pr.dbg(f"{player.name} not in {level.name} "
                            f"- adding {player.name} to {level.name} entitylist",1)
                    level.change_entity_list("+",player)
                Pr.dbg(f"Setting CurrentLevel to Level: {Level.levelname(level)}")
                current_level = level
                Pr.dbg(f"CurrentLevel: {current_level}")
        Pr.dbg("-"*50)

        player.check_level_up()
        interact_with_level(player, current_level, level_list)
        # changes the entity location, deletes entity from old level and adds to the new one

        # Increase Lap Counter by i
        lap = lap + 1

        # Wait for Player Input
        Debug.pause()

        #Loop through all Entities in CurrentLevel and Apply Actionstack
        Pr.dbg(f"Entitylist: {current_level.entitylist}")
        for e in current_level.entitylist:
            Pr.dbg(f"Working Actionstack for {e.name}")
            Pr.dbg(f"Actionstack: {e.actionstack}")
            #Work through actionstack of Entity and process actions
            for i in range(0,len(e.actionstack)):
                Pr.dbg("#"*50)
                Pr.dbg(f"Length of Actionstack: {len(e.actionstack)}")
                Pr.dbg(f"Current Actionstack: {e.actionstack}")
                Pr.dbg(f"Current Index: {i}")
                cur_action = e.actionstack.pop(0)
                Actionparser.callfunction(cur_action)
                Pr.dbg(f"Cur_Action: {cur_action}")
                Pr.dbg(f"Length of Actionstack after Action: {len(e.actionstack)}")
                Pr.dbg(f"Current Actionstack after Action: {e.actionstack}")
                Pr.dbg("#"*50)


if __name__ == "__main__":
    # Checking Game File Integrity
    AssetHandler.CheckGameIntegrity()

    # Importing Level Assets
    AssetHandler.importLevels()
    allLevels = AssetHandler.allLevels

    # Importing Entity Assets
    AssetHandler.importEntities()
    allEntities = AssetHandler.allEntities

    # Creating seperate Player Entitiies
    mPlayer = Entity(
        "Player",
        100,
        100,
        0,
        [gitem("Item1", "weapon"), gitem("item2", "misc")],
        location=allLevels[1],
    )
    hurensohn = Entity(
        "Hurensohn",
        100,
        100,
        0,
        [gitem("Item1", "weapon"), gitem("item2", "misc")],
        location="Wiese",
    )

    # Creating seperate Effects
    kopfschmerz = Effect("Kopfschmerz", "Kopfschmerzen halt.", "bad", -1, "hp")
    heilung = Effect("heilung", "Nö", "good", 5, "hp")
    heilung2 = Effect("heilung2", "Nö", "good", 5, "hp")
    heilung3 = Effect("heilung 3", "Nö", "good", 5, "hp")
    terror = Effect("Terror", "Nö", "evil", -100, "xp")

    # put Kopfschmerz Effect in Actionstack
    mPlayer.actionstack.append(["add_effect", [mPlayer, "Kopfschmerz"]])
    mPlayer.actionstack.append(["take_effects", [mPlayer, True]])

    # List all Loaded Levels and Entities
    Debug.objlist(allLevels, "Levels")
    Debug.objlist(allEntities, "Entities")

    # Run Game
    gameloop(mPlayer, allLevels)
