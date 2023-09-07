"""Combatstate
"""
from Utils import Pr


def combatstate(player):
    """
    Args:
        Player (obj:entity): the player obj.
    """
    playername = player.name
    Pr.dbg(f"{playername} entered Combatstate")
    Pr.dbg(f"{playername} leaving Combatstate")
