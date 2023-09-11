"""Combatstate
"""
from Utils import Pr, dice


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
    for e in entities:
        e.spd = e.attributes.get("ini") + dice.roll("1w6+0")
        Pr.dbg(f"{e.spd}", 2)
    Pr.dbg(f"{playername} leaving Combatstate")
