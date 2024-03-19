"""
Effects Module which holds 2 Classes
    Effect()
    EffectInit()
"""

import json
from Utils import Logger, tcolors


class Effect:
    """
    Class which defines Effects
    Contains Functions:
    from_json : Creates Effects from JSON
    """

    __slots__ = "name", "descr", "etype", "value", "infl"

    def __init__(
        self,
        name="Effectname",
        desrc="Effectdescription",
        etype="good",
        value=0,
        influenced="atk",
    ):
        self.name = name
        """The Name of the Effect as String"""
        self.descr = desrc
        """The Description of the Effect as String"""
        self.etype = etype
        """The Type of the Effect as String of ["good","bad","evil"]"""
        self.value = value
        """The amount of what the effect influences as Integer"""
        self.infl = influenced
        """The Attribute the effect influences as String"""

    @staticmethod
    def from_json(json_dct, ename):
        """Creates an Effect from given JSON

        Args:
            json_dct (json): The Json Code to be parsed
            ename (String): The Effect Name

        Returns:
            Effect: Effect
        """
        return Effect(
            ename,
            json_dct["descr"],
            json_dct["etype"],
            json_dct["value"],
            json_dct["infl"],
        )


class EffectInit:
    """
    Class which Initializes Effects
    Contains Functions:
    load_all_effects_from_json : Loads all available Effects from a Json File
    load_effect_by_name_from_json : Loads an Effect by it's Name from a Json File

    """

    def load_all_effects_from_json(json_file):
        """
        Return alls Effects from Json file

        :json_file (File): Json file to load Effects from

        =return= List of all Effects loaded from Json
        """
        effects_master_list = []
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for ename in data.keys():
            if ename[0] != "$":
                effects_master_list.append(Effect.from_json(data[ename], ename))
        return effects_master_list

    def load_effect_by_name_from_json(json_file, name):
        """
        Return a single Level Object from Json by given Name

        :json_file (File): Json File to load Item from
        :name (String): Name of Effect to be loaded

        =return= Level object
        """
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for ename in data.keys():
            if name == ename:
                return Effect.from_json(data[ename], ename)

        Logger.log(f"Effect: {tcolors.cyan(name)} not found!", 1)
        return False
