"""Combatstate
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import questionary
from Utils import Pr, dice, Debug, Logger
from actionparser import Actionparser

if TYPE_CHECKING:
    from Entities import Entity


def combatstate(player: Entity, entities: list[Entity] = None) -> None:
    """
    Args:
        Player (obj:entity): the player obj.
        entities (list): list of entities besides the player obj.
    """
    if entities is None:
        entities = []
        Logger.log("No Entities are here to fight", 2)
        return
    if player is None:
        Logger.log("No Player is given.", 2)
        return

    wants_exit = False

    # Remove Player from Entitylist
    del entities[entities.index(player)]

    playername = player.name
    Logger.log(f"{playername} entered Combatstate with {entities}", 1)
    _enemylist = dict(zip(Debug.getNames(entities), entities))
    entities.append(player)
    Debug.objlist(entities)
    for e in entities:
        Logger.log(f"Rolling SPD for {e.name}", -1)
        e.spd = e.attributes.get("ini") + dice.roll("1w6+0")
        Logger.log(f"{e.name}'s SPD is {e.spd}", -1)

    entities.sort(key=lambda x: x.spd, reverse=True)
    Debug.objlist(entities)

    while not wants_exit:
        choice = questionary.select(
            "Choose Action:",
            choices=[
                "Attack",
                "zurück zum Spiel",
            ],
        ).unsafe_ask()

        match choice:
            case "Attack":
                Actionparser.show_wip()
                _enemylist.update({"Zurück": "Zurück"})
                choice2 = questionary.select(
                    "Wen möchtest du Angreifen?", choices=_enemylist.keys()
                ).unsafe_ask()
                if choice2 == ("Zurück"):
                    Logger.log("Player choose to back off", 1)
                    break

                Logger.log(f"{player.name} is about to Attack {choice2}", 1)
                _selectedEntity = _enemylist.get(choice2)
                _weapon = entities[0].slots[8]
                _weaponname = entities[0].slots[8].name
                _damage = _weapon.getDamage()
                Logger.log(
                    f"{player}({player.name}) is attacking with"
                    f"{_weapon}({_weaponname}) and inflicting"
                    f"{_damage} damage to {_selectedEntity}({choice2})"
                )
                _selectedEntity.actionstack.append(
                    ["take_damage", [_selectedEntity, _damage, player]]
                )
                Pr.n(
                    f"Du greifst {choice2} mit deinem {_weaponname} an und verursachst {_damage}"
                )

            case "zurück zum Spiel":
                wants_exit = True

        for e in entities:
            # pylint:disable=C0301
            e.act()
            # Work Actionstack to finish CombatRound
            Logger.log(f"Working Actionstack for {e.name}")
            Logger.log(f"Actionstack: {e.actionstack}")
            # Work through actionstack of Entity and process actions
            for i in range(0, len(e.actionstack)):
                Logger.log("#" * 50, -1)
                Logger.log(f"Length of Actionstack: {len(e.actionstack)}", -1)
                Logger.log(f"Current Actionstack: {e.actionstack}", -1)
                Logger.log(f"Current Index: {i}", -1)
                cur_action = e.actionstack.pop(0)
                _ret = Actionparser.callfunction(cur_action)
                Logger.log(f"Actionparser Returnvalue: {_ret}")
                if _ret is True:
                    entities.remove(e)
                    _enemylist.pop(e.name)
                Logger.log(f"Cur_Action: {cur_action}", -1)
                Logger.log(
                    f"Length of Actionstack after Action: {len(e.actionstack)}", -1
                )
                Logger.log(f"Current Actionstack after Action: {e.actionstack}", -1)
                Logger.log("#" * 50, -1)

        if wants_exit:
            Logger.log(f"{playername} leaving Combatstate")
            break
