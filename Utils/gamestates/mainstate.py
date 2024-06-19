"""main gamestate for interaction with levels
    and world aka. levelparser n shit
"""

# project imports:
from __future__ import annotations
from typing import TYPE_CHECKING
from Utils import Pr, Inp, Logger, hud

if TYPE_CHECKING:
    from Entities import Entity
    from Level import Level


def interact_with_level(player: Entity, level: Level, level_list: list[Level]) -> None:
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
        while True:
            action = int(Inp.inp(player)) - 1  # pylint: disable=E0601
            if action <= len(availableChoices) - 1:
                break
            print(
                f"Wrong Input! Input must be same or less than: {len(availableChoices)}"
            )
        if action == 33:
            Logger.log("Break!")  # this is bs
            """
            This breaks the Mainstate early in execution, 
            which is used with changing a new gamestate from
            commands recieved by the input parser.
            """
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
        # this Problem gets solved by input parser. this section
        # is kept alive for future development in minigames for
        # example, where to big inputs may change the environment.
        pass
