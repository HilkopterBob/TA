"""Hud creates the basic game output
    like gold, health, location
"""

from Utils import Pr


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
