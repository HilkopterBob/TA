"""File just for some Snippets
"""
import random


def roll(value):
    """Rolls a Dice

    Args:
        value (String): Dicestring to roll e.g: 1w6+5 to Roll 1 D6 and add 5

    Returns:
        Boolean: Returns True - always
    """
    inp = value.split("w")
    inp2 = inp[1].split("+")
    rolls = int(inp[0])
    dice = int(inp2[0])
    base = int(inp2[1])
    randydice = rolls * random.randrange(1, dice)
    rolled = randydice + base
    print(f"{value} - Rolled {rolls}*w{dice} = {randydice} and added {base}: {rolled}")
    return True


if __name__ == "__main__":
    dicestring = (
        f"{random.randrange(1,5)}w{random.randrange(3,100)}+{random.randrange(0,10)}"
    )
    for x in range(20):
        roll(dicestring)
