"""
Entities Module which holds 2 Classes
    Entity()
    Entityinit()
"""

import json
import random
from Utils import Logger, tcolors


class gitem:
    """
    Class which defines Items
    Contains Functions:
    from_json : Creates Items from JSON
    """

    __slots__ = (
        "name",
        "itype",
        "description",
        "ad",
        "ap",
        "hp",
        "ar",
        "mr",
        "rarity",
        "effects",
        "useable",
        "equipable",
        "slots",
        "questitem",
    )

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
        slots=None,
        questitem=False,
    ):
        if effects is None:
            effects = []
        if slots is None:
            slots = []

        self.name = name
        """Name of Item as String"""
        self.itype = itype
        """Type of Item as String"""
        self.description = description
        """Description of the Items as String"""
        self.ad = ad
        """The Physical Attack Damage of the Item as String"""
        self.ap = ap
        """The Magical Attack Power of the Item as String"""
        self.hp = hp
        """The Hitpoints of the Item as Integer"""
        self.ar = ar
        """The Physical Resistance to Damage of the Item as Integer"""
        self.mr = mr
        """The Magical Resistance to Damage of the Item as Integer"""
        self.rarity = rarity
        """The Rarity Level of the Item as String"""
        self.effects = effects
        """The Effects on the Items as Array of Objects"""
        self.useable = useable
        """If the Item is useable(consumable) as Boolean"""
        self.equipable = equipable
        """If the Item is equipable as Boolean"""
        self.slots = slots
        """The Slots where the Item can be Equipped as Array of Slots"""
        self.questitem = questitem
        """If the Item as a Questrelatet Item as Boolean"""

    def get(self, thing: str, *args):  # pylint: disable=W0613
        """compatibility function for questify"""
        return self.name

    def getDamage(self):
        """Return Damage Dict for Item in Format
        {
            "AD":ADDamage,
            "AP":APDamage
        }
        Ease of Access:
            AD = Item.getDamage().get('AD')
            AP = Item.getDamage().get('AP')
        """
        ADroll_result = 0
        ADnum_dice = int(self.ad.split("w")[0])
        ADBaseDamage = int(self.ad.split("+")[1])
        ADdice = int(self.ad.split("w")[1].split("+")[0])

        AProll_result = 0
        APnum_dice = int(self.ap.split("w")[0])
        APBaseDamage = int(self.ap.split("+")[1])
        APdice = int(self.ap.split("w")[1].split("+")[0])

        Logger.log(f"Rolling: {self.ad} for AD")
        for _ in range(ADnum_dice):
            ADroll = random.randint(1, ADdice)
            Logger.log(f"Rolled: {ADroll}", -1)
            ADroll_result += ADroll
        ADdmg = ADBaseDamage + ADroll_result
        Logger.log(f"Final Rollresult for AD: {ADdmg}")

        Logger.log(f"Rolling: {self.ap} for AP")
        for _ in range(APnum_dice):
            AProll = random.randint(1, APdice)
            Logger.log(f"Rolled: {AProll}", -1)
            AProll_result += AProll
        APdmg = APBaseDamage + AProll_result
        Logger.log(f"Final Rollresult for AP: {APdmg}")

        return {"AD": ADdmg, "AP": APdmg}

    def __str__(self):
        return f"{self.name}"

    # Commented out for readability in Logfile - need to find a workaround
    # def __repr__(self):
    #    return f"[{self.__class__.__module__}.{self.__class__.__name__}('{self.name}','{self.itype}','{self.description}',{self.ad},{self.ap},{self.hp},{self.ar},{self.mr},'{self.rarity}',[{self.effects}],{self.useable},{self.equipable},[{self.slots}],{self.questitem}) at <{hex(id(self))}>]"  # pylint:disable=C0301

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
            json_dct["slots"],
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

        Logger.log(f"Loading Items from: {json_file}")

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

        Logger.log(f"Itemname: {tcolors.cyan(name)} not found!", 1)
        return False
