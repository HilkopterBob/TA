"""Util for Dice Rolling
"""

import random
from Utils import Logger


def roll(dice: str = None) -> int:
    """Rolls Dice when given as Dice String in Format like 1w6+5

    Args:
        dice (String): Dice String.

    Returns:
        int: Final roll Result
    """
    if dice is None:
        Logger.log("No Dice String given", 2)
        return 0

    Logger.log(f"Rolling: {dice}", 0)
    roll_result = 0
    num_dice = int(dice.split("w")[0])
    BaseDamage = int(dice.split("+")[1])
    dice = int(dice.split("w")[1].split("+")[0])

    for _ in range(num_dice):
        droll = random.randint(1, dice)
        Logger.log(f"Rolled: {droll}", -1)
        roll_result += droll
    dmg = BaseDamage + roll_result
    Logger.log(f"Final Rollresult: {dmg}", 1)
    return dmg
