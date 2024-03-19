"""
Actionparser Module which holds 1 Class
    Actionparser()
"""

import sys
from Effect import EffectInit
from config import config
from Level import Level
from Utils import Logger, Pr


class Actionparser:
    """
    Class which defines function for Actionparsing
    Contains Functions:
    callfunction : Calls an internal function by it's name
    add_effect : Adds an Effect to an Entity
    take_effects : Lets an Effect have its Effect on an Entity
    change_location : Switches Entity Location
    set_name : Sets the Name for an Entity
    change_health : Changes Health for an Entity
    add_item : Adds an Item to Entity Inventory
    remove_item_by_name : Removes an Item from an Entity Inventory by it's Name
    remove_item_by_index : Removes an Item from an Entity Inventory by it's Index
    show_effects : Displays all Effects on Entity
    remove_effect_by_name : Removes an Effect by it's Name from an Entity
    change_stat : Changes Stats of an Entity
    check_level_up : Checks for Player Level Up Conditions
    show_wip : shows wip banner
    """

    gamestate = "loading"

    def callfunction(attr=None):
        """Calls an internal function by it's String Name

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attr}", -1)

        if attr is None:
            attr = []

        _call = getattr(Actionparser, attr[0])
        return _call(attr[1])

    def close_game(attributes=None):
        """Calls the close_game function with arguments

        Args:
            attributes (None, optional):
        """
        Logger.log("Closing game")
        sys.exit()

    def add_effect(attributes=None):
        """Calls the add_effect Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _effectname = attributes[1]
            _effect = EffectInit.load_effect_by_name_from_json(
                config.effects_file, _effectname
            )
            _entity.add_effect(_effect)
            return 0
        except:
            return 1

    def take_effects(attributes=None):
        """Calls the take_effects Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            Logger.log(attributes)
            _entity = attributes[0]
            _entity.let_effects_take_effect([attributes[1]])
            return 0
        except:
            return 1

    def change_location(attributes=None):
        """Calls the change_location Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []
        try:
            _entity = attributes[0]
            _old_level = attributes[1]
            _new_level = attributes[2]
            Logger.log(
                f"Trying to Change {_entity} location "
                f"from {Level.levelname(_old_level)} to {Level.levelname(_new_level)}"
            )
            _entity.change_location(_old_level, _new_level)
            return 0
        except Exception as e:
            Logger.log(f"ERR: {e}", 1)
            return 1

    def set_name(attributes=None):
        """Calls the set_name Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _entity.set_name()
            return 0
        except:
            return 1

    def change_health(attributes=None):
        """Calls the change_health Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _value = attributes[1]
            _entity.change_health(_value)
            return 0
        except:
            return 1

    def add_item(attributes=None):
        """Calls the add_item Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _item = attributes[1]
            _entity.add_item(_item)
            return 0
        except:
            return 1

    def remove_item_by_name(attributes=None):
        """Calls the remove_item_by_name Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _iname = attributes[1]
            _entity.remove_item_by_name(_iname)
            return 0
        except:
            return 1

    def remove_item_by_index(attributes=None):
        """Calls the remove_item_by_index Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _index = attributes[1]
            _quest = attributes[2]
            _entity.remove_items_by_index(_index)
            return 0
        except:
            return 1

    def show_effects(attributes=None):
        """Calls the show_effects Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _entity.show_effects()
            return 0
        except:
            return 1

    def remove_effect_by_name(attributes=None):
        """Calls the remove_effect_by_name Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _ename = attributes[1]
            _entity.remove_effect_by_name(_ename)
            return 0
        except:
            return 1

    def change_stat(attributes=None):
        """Calls the change_stat Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _effect = attributes[1]
            _entity.change_stat(_effect)
            return 0
        except:
            return 1

    def take_damage(attributes=None):
        """Calls the take_damage Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error
            Dict: Damage in Format {"AD":DMG, "AP":DMG}
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _value = attributes[1]
            _inflicter = attributes[2]
            _dmg = _entity.take_damage(_value, _inflicter)
            return _dmg
        except:
            return 1

    def check_level_up(attributes=None):
        """Calls the check_level_up Function with arguments

        Args:
            attr (list, optional): Arguments passed. Defaults to [].

        Returns:
            Integer: 1 on Error, else 0
        """
        Logger.log(f"Call: {attributes}")

        if attributes is None:
            attributes = []

        try:
            _entity = attributes[0]
            _entity.check_level_up()
            return 0
        except:
            return 1

    def change_gamestate(attributes=None):
        """Changes the Current Game State"""

        if attributes is None:
            attributes = []

        try:
            newgamestate = attributes[0]
            Logger.log(f"Old Gamestate: {Actionparser.gamestate}")
            Actionparser.gamestate = newgamestate
            Logger.log(f"Changing Gamestate to {newgamestate}")
            Logger.log(f"New Gamestate: {Actionparser.gamestate}")
            return 0
        except:
            return 1

    def show_wip(*args):
        """shows wip message"""
        Pr.headline(
            "Work In Progress.\nCheck this feature in a later update.\n-the Devs ♥"
        )
