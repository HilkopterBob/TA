"""Main Module for Textadventure
"""

# std imports:
from time import sleep

# project imports:
from pympler.asizeof import asizeof as getsize
from Entities import Entity
from Level import Level
from Effect import Effect
from Items import gitem
from Utils import Pr, Inp, Logger
from Utils.gamestates.inventorystate import inventorystate
from Utils.gamestates.combatstate import combatstate
from actionparser import Actionparser
from Assethandler import AssetHandler


def interact_with_level(player, level, level_list):
    """Current Game Interaction Function"""
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    Logger.log(f"Player: {player.name}, in Level: {level.name}")
    if level.name == "Menu":
        Pr.n("\n" * 5)
        Pr.headline(level.descr)
        Pr.n("\n" * 2)
    else:
        Logger.log("HUD")
        hud(player)
        # pr.n(level.descr)

        # Level Headers and Description
        level.printDesc()

    # Print Level Choices
    availableChoices = level.getAvailableChoices()
    for choice in availableChoices:
        print(f"{availableChoices.index(choice)+1}. {choice}")
    printed = True

    Logger.log(f"Current Choices: {level.choices}", -1)

    if printed:
        action = int(Inp.inp(mPlayer)) - 1  # pylint: disable=E0601
        if action == 33:
            Logger.log("Break!")
            return
    ##### ##### Reads triggers and action calls in level.text[dicts] ##### #####
    # Logger.log("*"*20
    # pr.n(level.text[action][0])
    # Logger.log("*"*20)
    ####Is doing nothing ?

    # Selecting index from available Actions
    Logger.log(f"Available Actions: {level.getAvailableChoices()}", -1)

    # Sehr falsch, Index Choice 2 wird text 1 zugeordnet
    availableChoicesDict = dict(zip(availableChoices, level.text))

    # Link Choices - result test

    if action < len(availableChoicesDict.keys()):
        actions = availableChoicesDict[availableChoices[action]]
        for i in actions:
            _currentAction = actions[actions.index(i)]
            if _currentAction != "":
                if isinstance(_currentAction, str):
                    Pr.n(_currentAction)
                else:
                    try:
                        try:
                            if "action" in _currentAction.keys():
                                if _currentAction.get("action") == "change_location":
                                    for _level in level_list:
                                        if (
                                            _level.name
                                            == list(_currentAction.values())[1]
                                        ):
                                            actiontoadd = [
                                                _currentAction.get("action"),
                                                [mPlayer, mPlayer.location, _level],
                                            ]
                                else:
                                    actiontoadd = [
                                        _currentAction.get("action"),
                                        [
                                            mPlayer,
                                            list(_currentAction.values())[1],
                                        ],
                                    ]
                            else:
                                Logger.log(f"No Action in Keys: {_currentAction}", 1)
                                # Do Trigger Stuff
                                # Letzter eintrag aus actions = immer Trigger.
                                # Supported nur einen Trigger!!!
                                touched_trigger = actions[-1]
                                level_triggers_list = level.triggers
                                Logger.log(level_triggers_list, 2)
                                for index, l_trigger in enumerate(level_triggers_list):
                                    if l_trigger.keys() == touched_trigger.keys():
                                        level_triggers_list[index] = touched_trigger
                            Logger.log(
                                f"Add {actiontoadd} to Actionstack for entity: {mPlayer}"
                            )
                            mPlayer.actionstack.append(actiontoadd)
                        except Exception as e:
                            Logger.log(f"ERR: {e}", 2)
                    except Exception:
                        Logger.log(f"CurrentAction: {_currentAction}", 2)
    else:
        Pr.n(
            f"Bitte gebe eine Zahl kleiner gleich {len(availableChoicesDict.keys())} ein!"
        )
        sleep(2)


def hud(player):
    """Player Hud

    Args:
        player (Entity): The Player to which the Hud should be displayed
    """

    if player.location.name not in ("Menu", "Options"):
        Pr.n("+" * 12 + " " + "+" * 12)
        Pr.n(f"Du befindest dich in: {player.location.name}")

        if player.hp > 25:
            Pr.g(f"HP: {player.hp}")
        else:
            Pr.b(f"HP: {player.hp}")
        Pr.n(f"Gold: {player.wealth}")
        Pr.n(f"Level: {player.level} XP: {player.xp}")


def gameloop(player, level_list=None):
    """
    The Main Game Loop
    """
    current_level = Level
    if level_list is None:
        level_list = []

    lap = 0

    # Entering Gameloop
    while True:
        for level in level_list:
            if str(level.name) == str(Level.levelname(player.location)):
                Logger.log(
                    f"Player location ({Level.levelname(player.location)}) "
                    f"is equal to Level ({level.name}), "
                )
                if not player in level.entitylist:
                    Logger.log(
                        f"{player.name} not in {level.name} "
                        f"- adding {player.name} to {level.name} entitylist",
                        1,
                    )
                    level.change_entity_list("+", player)
                Logger.log(f"Setting CurrentLevel to Level: {Level.levelname(level)}")
                current_level = level

        # Loop through all Entities in CurrentLevel and Apply Actionstack
        if Actionparser.gamestate == "game":
            for e in current_level.entitylist:
                for action in e.actionstack:
                    Logger.log(action)
                    Actionparser.callfunction(action)
                    e.actionstack.remove(action)

        match Actionparser.gamestate:
            case "loading":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                # loding steps
                Actionparser.gamestate = "game"
            case "game":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                interact_with_level(player, current_level, level_list)
                Actionparser.gamestate = Actionparser.gamestate
            case "inv":
                if Actionparser.gamestate == "game" or player.location.name == "Menu":
                    Logger.log('Gamestate "inv" not available from here!', 1)
                    Pr.yellow('Gamestate "inv" kann hier nicht geöffnet werden!')
                    Actionparser.gamestate = "game"
                else:
                    Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                    inventorystate(mPlayer)
                    Actionparser.gamestate = "game"
            case "combat":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                Logger.log(f"{mPlayer} Entering Combatstate")
                combatstate(
                    mPlayer, mPlayer.location.entitylist
                )  # pylint: disable=E0601
                Actionparser.gamestate = "game"
            case _:
                Pr.yellow(
                    f'Der Gamestate "{Actionparser.gamestate}" ist nicht bekannt.'
                )
                Logger.log(f"Gamestate {Actionparser.gamestate} unknown", 1)
                Actionparser.gamestate = "game"

        player.check_level_up()

        # changes the entity location, deletes entity from old level and adds to the new one

        # Increase Lap Counter by i
        lap = lap + 1

        # Loop through all Entities in CurrentLevel and Apply Actionstack
        Logger.log(f"Entitylist: {current_level.entitylist}", -1)
        for e in current_level.entitylist:
            Logger.log(f"Working Actionstack for {e.name}", 1)
            Logger.log(f"Actionstack: {e.actionstack}")
            # Work through actionstack of Entity and process actions
            for i in range(0, len(e.actionstack)):
                Logger.log("#" * 50, -1)
                Logger.log(f"Length of Actionstack: {len(e.actionstack)}", -1)
                Logger.log(f"Current Actionstack: {e.actionstack}", -1)
                Logger.log(f"Current Index: {i}", -1)
                cur_action = e.actionstack.pop(0)
                Actionparser.callfunction(cur_action)
                Logger.log(f"Cur_Action: {cur_action}", -1)
                Logger.log(
                    f"Length of Actionstack after Action: {len(e.actionstack)}", -1
                )
                Logger.log(f"Current Actionstack after Action: {e.actionstack}", -1)
                Logger.log("#" * 50, -1)


if __name__ == "__main__":
    # Checking Game File Integrity
    AssetHandler.CheckGameIntegrity()

    # Importing Level Assets
    AssetHandler.importLevels()
    allLevels = AssetHandler.allLevels

    # Importing Entity Assets
    AssetHandler.importEntities()
    allEntities = AssetHandler.allEntities

    # importing Item Assets
    AssetHandler.importItems()
    allItems = AssetHandler.allItems

    # Importing Effect Assets
    AssetHandler.importEffects()
    allEffect = AssetHandler.allEffects

    # Creating seperate Player Entitiies
    mPlayer = Entity(
        "Player",
        100,
        100,
        0,
        allItems,
        location=allLevels[1],
        attributes={"str": 8, "dex": 8, "int": 8, "ini": 80, "chr": 8},
        isPlayer=True,
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
    mPlayer.actionstack.insert(0, ["change_gamestate", ["game"]])

    # List all Loaded Levels and Entities
    # Debug.objlist(allLevels, "Levels")
    # Debug.objlist(allEntities, "Entities")
    # Debug.objlist(allItems, "Items")

    Logger.log(f"Speicherbedarf Levels: {getsize(Level())} B", 3)
    Logger.log(f"Speicherbedarf Items: {getsize(gitem())} B", 3)
    Logger.log(f"Speicherbedarf Entities: {getsize(Entity())} B", 3)
    Logger.log(f"Speicherbedarf Effects: {getsize(Effect())} B", 3)

    # Fill Player iventory with Placeholder Items
    while len(mPlayer.slots) < 11:
        mPlayer.slots.append("placeholder")
    # Run Game
    gameloop(mPlayer, allLevels)
