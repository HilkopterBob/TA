"""Combatstate
"""
from Utils import Pr, dice, Debug


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

    playername = player.name
    Pr.dbg(f"{playername} entered Combatstate with {entities}")
    entities.append(player)
    Debug.objlist(entities)
    for e in entities:
        Pr.dbg(f"Rolling SPD for {e.name}", -1)
        e.spd = e.attributes.get("ini") + dice.roll("1w6+0")
        Pr.dbg(f"{e.name}'s SPD is {e.spd}", -1)

    entities.sort(key=lambda x: x.spd, reverse=True)
    Debug.objlist(entities)

    for e in entities:
        Pr.dbg(f"{e.name}'s Health is now: {e.hp}")

    ###Todo: Do Stuff after INI Calculation
    for i in range(1, len(entities)):
        entities[i].take_damage(  # pylint: disable=E1101
            entities[0].slots[8].getDamage()  # pylint: disable=E1101
        )
    for e in entities:
        Pr.dbg(f"{e.name}'s Health is now: {e.hp}")

    Pr.dbg(f"{playername} leaving Combatstate")
