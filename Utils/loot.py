"""Util for Dice Rolling
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import random
import json
from Utils import Logger
from config import loottablepath, items_folder
from Items import itemInit

if TYPE_CHECKING:
    from Effect import Effect
    from Items import gitem


def roll_loot(loottable: dict[str:int] = None, amount: int = 1) -> list[gitem] | int:
    """Function to return an Array of Loot from Loottable

    Args:
        loottable (Dict, optional): The Loottable to be processed. Defaults to None.
        amount (int, optional): The Amount of items that should be returned. Defaults to 1.

    Returns:
        Array: List of Items selected from Loottable | Return 1 on Error
    """

    if amount < 1:
        Logger.log(f"Amount is {amount}", 3)
        return 1
    if loottable is None:
        Logger.log("No Loottable to get Items from", 3)
        return 1

    _lootdict = list(loottable.keys())
    _weights = list(loottable.values())

    Logger.log(f"Getting {amount} Items from Loottable: {loottable}", -1)
    _loot = random.choices(_lootdict, weights=_weights, k=amount)
    _lootret = []
    for item in _loot:
        Logger.log(f"Loading item {item} from Assets", 0)
        _lootret.append(
            itemInit.load_item_by_name_from_json(f"{items_folder}\\{item}.json", item)
        )
    return _lootret


def getLootTable(name: str) -> dict[str:int]:
    """Returns Content of Loottable given by Name

    Args:
        name (String): Name of the Loottable that should be used

    Returns:
        Dict: Loottable | None if Error
    """
    if name is None:
        return None

    _json_file = loottablepath + "/" + name + ".json"

    Logger.log(f"Loading Loottable {_json_file}", -1)

    with open(_json_file, encoding="UTF-8") as json_data:
        data = json.load(json_data)
    return data


def importAi(name: str) -> dict[str:int]:
    """Returns Content of Loottable given by Name

    Args:
        name (String): Name of the Loottable that should be used

    Returns:
        Dict: Loottable | None if Error
    """
    if name is None:
        return None

    _json_file = loottablepath + "/" + name + ".json"

    Logger.log(f"Loading AI Params {_json_file}", -1)

    with open(_json_file, encoding="UTF-8") as json_data:
        data = json.load(json_data)
    return data
