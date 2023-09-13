"""Combatstate
"""
import questionary
from Utils import Pr, dice, Debug
from actionparser import Actionparser


def combatstate(player, entities=None):
    """
    Args:
        Player (obj:entity): the player obj.
        entities (list): list of entities besides the player obj.
    """
    if entities is None:
        entities = []
    if player is None:
        Pr.dbg("No Player is given.", 2)
        return

    wants_exit = False

    playername = player.name
    Pr.dbg(f"{playername} entered Combatstate with {entities}")
    _enemylist = dict(zip(Debug.getNames(entities), entities))
    entities.append(player)
    Debug.objlist(entities)
    for e in entities:
        Pr.dbg(f"Rolling SPD for {e.name}", -1)
        e.spd = e.attributes.get("ini") + dice.roll("1w6+0")
        Pr.dbg(f"{e.name}'s SPD is {e.spd}", -1)

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
                    Pr.dbg("Player choose to back off", 1)

                Pr.dbg(f"{player.name} is about to Attack {choice2}")
                _selectedEntity = _enemylist.get(choice2)
                _weapon = entities[0].slots[8]
                _weaponname = entities[0].slots[8].name
                _damage = _weapon.getDamage()
                Pr.dbg(
                    f"{player}({player.name}) is attacking with"
                    f"{_weapon}({_weaponname}) and inflicting"
                    f"{_damage} damage to {_selectedEntity}({choice2})"
                )
                _selectedEntity.actionstack.append(
                    ["take_damage", [_selectedEntity, _damage]]
                )
                Pr.n(
                    f"Du greifst {choice2} mit deinem {_weaponname} an und verursachst {_damage}"
                )

            case "zurück zum Spiel":
                wants_exit = True

        for e in entities:
            # Add Entity Intelligence or Base Attack here to add Damage to Player to Actionstack

            # Work Actionstack to finish CombatRound
            Pr.dbg(f"Working Actionstack for {e.name}")
            Pr.dbg(f"Actionstack: {e.actionstack}")
            # Work through actionstack of Entity and process actions
            for i in range(0, len(e.actionstack)):
                Pr.dbg("#" * 50, -1)
                Pr.dbg(f"Length of Actionstack: {len(e.actionstack)}", -1)
                Pr.dbg(f"Current Actionstack: {e.actionstack}", -1)
                Pr.dbg(f"Current Index: {i}", -1)
                cur_action = e.actionstack.pop(0)
                Actionparser.callfunction(cur_action)
                Pr.dbg(f"Cur_Action: {cur_action}", -1)
                Pr.dbg(f"Length of Actionstack after Action: {len(e.actionstack)}", -1)
                Pr.dbg(f"Current Actionstack after Action: {e.actionstack}", -1)
                Pr.dbg("#" * 50, -1)

        if wants_exit:
            Pr.dbg(f"{playername} leaving Combatstate")
            break
