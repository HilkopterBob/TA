"""
Entities Module which holds 2 Classes
    Entity()
    Entityinit()
"""
import json
from Utils import Pr


class gitem:
    """
    Class which defines Items
    Contains Functions:
    from_json : Creates Items from JSON
    """

    def __init__(
        self,
        name="placeholder",
        itype="misc",
        description="",
        ad=0,
        ap=0,
        hp=0,
        ar=0,
        mr=0,
        rarity="common",
        effects=None,
        useable=False,
        equipable=False,
        questitem=False,
    ):
        if effects is None:
            effects = []

        self.name = name
        self.itype = itype
        self.description = description
        self.ad = ad
        self.ap = ap
        self.hp = hp
        self.ar = ar
        self.mr = mr
        self.rarity = rarity
        self.effects = effects
        self.usable = useable
        self.equipable = equipable
        self.questitem = questitem

    def get(self, thing: str, *args):  # pylint: disable=W0613
        """compatibility function for questify"""
        return self.name

    @staticmethod
    def from_json(json_dct, iname):
        """Creates an Item from given JSON

        Args:
            json_dct (json): The Json Code to be parsed

        Returns:
            Item: Item
        """
        return gitem(
            iname,
            json_dct["type"],
            json_dct["description"],
            json_dct["ad"],
            json_dct["ap"],
            json_dct["hp"],
            json_dct["ar"],
            json_dct["mr"],
            json_dct["rarity"],
            json_dct["effects"],
            json_dct["useable"],
            json_dct["equipable"],
            json_dct["questitem"],
        )


class itemInit:
    """
    Class which Initializes Items
    Contains Functions:
    load_all_items_from_json : Loads all available Items from a Json File
    load_item_by_name_from_json : Loads an item by it's Name from a Json File

    """

    def load_all_items_from_json(json_file):
        """
        Return alls Items from Json file

        :json_file (File): Json file to load Items from

        =return= List of all Items loaded from Json
        """
        curItems = []

        Pr.dbg(f"Loading Items from: {json_file}")

        if not isinstance(json_file, dict):
            with open(json_file, encoding="UTF-8") as json_data:
                data = json.load(json_data)
        else:
            data = json_file

        for iname in data.keys():
            if iname[0] != "$":
                curItems.append(gitem.from_json(data[iname], iname))
        return curItems

    def load_item_by_name_from_json(json_file, name):
        """
        Return a single item Object from Json by given Name

        :json_file (File): Json File to load Item from

        =return= Item object
        """
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for iname in data.keys():
            if iname == name:
                return gitem.from_json(data[iname], iname)

        Pr.dbg(f"Itemname: {Pr.cyan(name)} not found!", 1)
        return False
