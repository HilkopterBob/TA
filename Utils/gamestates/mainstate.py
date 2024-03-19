# std imports:
from time import sleep

# project imports:
from pympler.asizeof import asizeof as getsize
from Entities import Entity
from Level import Level
from Effect import Effect
from Items import gitem
from Utils import Pr, Inp, Logger, hud
from actionparser import Actionparser
from Assethandler import AssetHandler, load_game




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
        Logger.log("hud.hud")
        hud.hud(player)

        # Level Headers and Description
        level.printDesc()

    # Print Level Choices
    availableChoices = level.getAvailableChoices()
    for choice in availableChoices:
        print(f"{availableChoices.index(choice)+1}. {choice.choice[0]}")
    printed = True

    Logger.log(f"Current Choices: {[vars(choice) for choice in availableChoices]}", -1)

    if printed:
        action = int(Inp.inp(player)) - 1  # pylint: disable=E0601
        if action == 33:
            Logger.log("Break!")
            return

    Logger.log(f"Available Actions: {level.getAvailableChoices()}", -1)


    if action < len(availableChoices):
        actions = availableChoices[action].text
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
                                                [player, player.location, _level],
                                            ]
                                else:
                                    actiontoadd = [
                                        _currentAction.get("action"),
                                        [
                                            player,
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
                                f"Add {actiontoadd} to Actionstack for entity: {player}"
                            )
                            player.actionstack.append(actiontoadd)
                        except Exception as e:
                            Logger.log(f"ERR: {e}", 2)
                    except Exception:
                        Logger.log(f"CurrentAction: {_currentAction}", 2)
    else:
        Pr.n(
            f"Bitte gebe eine Zahl kleiner gleich {len(availableChoicesDict.keys())} ein!"
        )
        sleep(2)
