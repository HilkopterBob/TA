"""Util for Dice Rolling
"""
import random
import json
from Utils.pr import Pr
from config import loottablepath


def roll_loot(loottable=None, amount=1):
    """Function to return an Array of Loot from Loottable

    Args:
        loottable (Dict, optional): The Loottable to be processed. Defaults to None.
        amount (int, optional): The Amount of items that should be returned. Defaults to 1.

    Returns:
        Array: List of Items selected from Loottable | Return 1 on Error
    """

    if amount < 1:
        Pr.dbg(f"Amount is {amount}", 3)
        return 1
    if loottable is None:
        Pr.dbg("No Loottable to get Items from", 3)
        return 1

    _lootdict = list(loottable.keys())
    _weights = list(loottable.values())

    Pr.dbg(f"Getting {amount} Items from Loottable: {loottable}", -1)

    return random.choices(_lootdict, weights=_weights, k=amount)


def getTable(name):
    """Returns Content of Loottable given by Name

    Args:
        name (String): Name of the Loottable that should be used

    Returns:
        Dict: Loottable | None if Error
    """
    if name is None:
        return None

    _json_file = loottablepath + "/" + name + ".json"

    Pr.dbg(f"Loading Loottable {_json_file}", -1)

    with open(_json_file, encoding="UTF-8") as json_data:
        data = json.load(json_data)
    return data
