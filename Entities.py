"""
Entities Module which holds 2 Classes
    Entity()
    Entityinit()
"""
import json
from Level import Level
from Utils import Pr, Inp


class Entity:
    """
    Class which defines Entities
    Contains Functions:
    from_json : Creates Entities from JSON
    """

    def __init__(
        self,
        name="Blanko",
        health=100,
        wealth=100,
        xp=0,
        inv=None,
        ptype="",
        geffects=None,
        beffects=None,
        eeffects=None,
        location="Nirvana",
        level=1,
        slots=None,
        allowdamage=True,
    ):
        if inv is None:
            inv = []
        if geffects is None:
            geffects = []
        if beffects is None:
            beffects = []
        if eeffects is None:
            eeffects = []
        if slots is None:
            slots = []

        self.location = location
        self.name = name
        self.hp = health
        self.wealth = wealth
        self.level = level
        self.xp = xp
        self.inv = inv
        self.ptype = ptype
        self.geffects = geffects
        self.beffects = beffects
        self.eeffects = eeffects
        self.effects = [[self.geffects], [self.beffects], [self.eeffects]]
        self.actionstack = []
        self.slots = (
            slots  # ["Head_slot", "Torso_slot", "Underwear", "Left_arm", "Right_arm",
        )
        # "Left_leg", "Right_leg", "Gloves_slot",
        # "Meele Weapon", "Ranged Weapon",
        # "Quick_draw potion"]
        self.allowdamage = allowdamage

    @staticmethod
    def from_json(json_dct):
        """Creates an Entiy from given JSON

        Args:
            json_dct (json): The Json Code to be parsed

        Returns:
            Entity: Entity
        """
        return Entity(
            json_dct["name"],
            json_dct["hp"],
            json_dct["wealth"],
            json_dct["xp"],
            json_dct["inv"],
            json_dct["ptype"],
            json_dct["geffects"],
            json_dct["beffects"],
            json_dct["eeffects"],
            json_dct["location"],
            json_dct["level"],
        )

    def set_name(self):
        """
        Sets the Name of an Entity Object
        """
        while True:
            self.name = Inp.inp("Wie soll der Held deiner Geschichte heißen?")
            Pr.n(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = Inp.inp(
                "[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)"
            )
            if action == "y":
                break

    def change_health(self, value=0):
        """
        Changes the Player Health

        :value: Amount to Change

        =return= Returns True if successfull otherwise returns false
        """
        try:
            self.hp += value
            if self.hp <= 0:
                if self.allowdamage: #  pylint: disable=R1705
                    Pr.dbg("Entity {self} has 0 or less Health")
                    return True
                else:
                    self.hp = 1
                    Pr.dbg(
                        f"Entity {self.name} is not allowed to take \
                        Damage Allowdamage: {self.allowdamage}",
                        1,
                    )
                    return False
            return False
        except:
            return False

    def add_item(self, item):
        """
        Adds Item to Inventory

        :iname: Name of Item
        :itype: Type of Item

        =return= Returns True if successfull otherwise returns false
        """
        try:
            self.inv.append(item)
            return True
        except:
            return False

    def remove_item_by_name(self, iname=""):
        """
        Removes Item by given Itemname, if no Name is given no Item will be removed.

        :iname: Name of Item which should be removed

        =return= Returns True if successfull otherwise returns false
        """
        try:
            self.inv = list(filter(lambda i: i.name != iname, self.inv))
            return True
        except:
            return False

    def remove_item_by_index(self, index=-1, quest=False):
        """
        Removes Item by given Index,
        if no Index is given the last Item in Inventory will be removed.

        :index: Index of Item which should be removed

        =return= Returns True if successfull otherwise returns false
        """

        try:
            if not self.inv[index].questitem:
                self.inv.pop(index)
            elif quest:
                self.inv.pop(index)
            return True
        except:
            return False

    def add_effect(self, effect):
        """
        appends effect to coresponding list

        :effect: OBJECT!

        =return= Returns True if successfull otherwise returns false
        """
        match effect.etype:
            case "good":
                try:
                    self.geffects.append(effect)
                    return True
                except:
                    return False
            case "bad":
                try:
                    self.beffects.append(effect)
                    return True
                except:
                    return False
            case "evil":
                try:
                    self.eeffects.append(effect)
                    return True
                except:
                    return False

    def show_effects(self, names=False):
        """
        prints element.name of effects[]

        :names: shows only the effect.name if True, false shows var(effect)

        only for debug!
        """
        try:
            if names:
                try:
                    for e in self.effects[0][0]:
                        print(e.name)
                    for e in self.effects[1][0]:
                        print(e.name)
                    for e in self.effects[2][0]:
                        print(e.name)
                    return True
                except e:
                    print(e)
                    return False
            else:
                try:
                    for e in self.effects:
                        print(vars(e))
                    return True
                except:
                    return False
        except:
            return False

    def remove_effect_by_name(self, ename=""):
        """
        removes effect from entity by given name
        :ename: effect.name as string

        =return= returns true if successfull, else false
        """
        try:
            self.geffects = list(filter(lambda e: e.name != ename, self.geffects))
            self.beffects = list(filter(lambda e: e.name != ename, self.beffects))
            self.eeffects = list(filter(lambda e: e.name != ename, self.eeffects))
            return True
        except:
            return False

    def remove_effect_by_index(self, index=-1):
        """
        removes effect by given index

        :index: index of effect that should be removed

        =return= true if successfull else false
        """
        try:
            self.effects.pop(index)
            return True
        except:
            return False

    def change_stat(self, effect):
        """
        changes stat (effect.infl) by effect.value

        :effect(obj): effect object

        =return= true if sucessfull, else false
        """
        match effect.infl:
            case "hp":
                try:
                    self.hp += effect.value
                    return True
                except:
                    return False
            case "xp":
                try:
                    self.xp += effect.value
                    return True
                except:
                    return False
            case _:
                print("change_stat: WILDCARD AUSGELÖST! debuginfo:")
                print(vars(self))
                print(vars(effect))
                return False

    def take_effects(self):
        """
        used in gameloop to let effects take effect onto entety

        :: no vars except self-obj

        =return= true if succesfull else False
        """
        try:
            for e in self.eeffects:
                self.change_stat(e)
                Pr.dbg(
                    f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                )
            for e in self.geffects:
                self.change_stat(e)
                Pr.dbg(
                    f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                )
            for e in self.beffects:
                self.change_stat(e)
                Pr.dbg(
                    f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                )
            return True
        except:
            return False

    def change_location(self, old_level, new_level):
        """
        changes entty location by edditing onwn location,
        deletes itself from old and adds to new entity.list

        :old_level: old level object, old_level.entity_list will get eddited

        :new_level: new level object, new_level.entity_list will get eddited

        =return= returns nothing, yet
        """
        if not isinstance(old_level, Level) or not isinstance(new_level, Level):
            Pr.dbg("Level not Level Object!", 1)
            Pr.dbg(
                f"OldLevel: {old_level} | {type(old_level)},"
                f" New_Level: {new_level} | {type(new_level)}"
            )
        Pr.dbg(f"Changing Level for {self} from {old_level} to {new_level}")
        self.location = new_level
        new_level.change_entity_list("+", self)
        old_level.change_entity_list("-", self)

    def check_level_up(self):
        """
        checks if entity has enough xp to level up,
        will level up the entity UNTIL there are not enough xp

        =return= returns nothing, yet
        """
        level_ups = 0
        old_level = self.level
        Pr.dbg(f"Previous Level: {old_level}")
        while True:
            if self.level < 10:
                needed_xp = ((self.level + 1) / 0.4) ** 1.79
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp = self.xp - int(needed_xp)
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")

            if self.level >= 10 and self.level < 30:
                needed_xp = ((self.level + 1) / 0.37) ** 1.86
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp -= needed_xp
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")

            if self.level >= 30:
                needed_xp = ((self.level + 1) / 0.2) ** 2.175
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp -= needed_xp
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")

            break
        return True

    def consume_item(self, item_name):
        """enables consumption of consumables."""
        for item in self.inv:
            if item.name == item_name:
                consumable = item

        if consumable.effects and consumable.itype != "Food":
            if len(consumable.effects) != 0:
                for effect in consumable.effects:
                    self.add_effect(effect)
            else:
                self.change_health(consumable.dbg)
            self.remove_item_by_name(consumable.name)

        if consumable.itype == "Food":
            self.change_health(consumable.dmg)

    def equip_item(self, item_name):
        """enables equiping of eqipment"""
        for item in self.inv:
            if item.name == item_name:
                cur_item = item
        match cur_item.slots[0]:
            case "head":
                if self.slots[0]:
                    if self.slots[0] != "placeholder":
                        self.inv.append(self.slots[0])
                self.slots[0] = cur_item
                self.inv.remove(cur_item)
            case "torso":
                if self.slots[1]:
                    if self.slots[1] != "placeholder":
                        self.inv.append(self.slots[1])
                self.slots[1] = cur_item
                self.inv.remove(cur_item)
            case "underwear":
                if self.slots[2]:
                    if self.slots[2] != "placeholder":
                        self.inv.append(self.slots[2])
                self.slots[2] = cur_item
                self.inv.remove(cur_item)
            case "left_arm":
                if self.slots[3]:
                    if self.slots[3] != "placeholder":
                        self.inv.append(self.slots[3])
                self.slots[3] = cur_item
                self.inv.remove(cur_item)
            case "right_arm":
                if self.slots[4]:
                    if self.slots[4] != "placeholder":
                        self.inv.append(self.slots[4])
                self.slots[4] = cur_item
                self.inv.remove(cur_item)
            case "left_leg":
                if self.slots[5]:
                    if self.slots[5] != "placeholder":
                        self.inv.append(self.slots[5])
                self.slots[5] = cur_item
                self.inv.remove(cur_item)
            case "right_leg":
                if self.slots[6]:
                    if self.slots[6] != "placeholder":
                        self.inv.append(self.slots[6])
                self.slots[6] = cur_item
                self.inv.remove(cur_item)
            case "gloves":
                if self.slots[7]:
                    if self.slots[7] != "placeholder":
                        self.inv.append(self.slots[7])
                self.slots[7] = cur_item
                self.inv.remove(cur_item)
            case "melee":
                if self.slots[8]:
                    if self.slots[8] != "placeholder":
                        self.inv.append(self.slots[8])
                self.slots[8] = cur_item
                self.inv.remove(cur_item)
            case "ranged":
                if self.slots[9]:
                    if self.slots[9] != "placeholder":
                        self.inv.append(self.slots[9])
                self.slots[9] = cur_item
                self.inv.remove(cur_item)
            case "quick_draw_potion":
                if self.slots[10]:
                    if self.slots[10] != "placeholder":
                        self.inv.append(self.slots[10])
                self.slots[10] = cur_item
                self.inv.remove(cur_item)
            case _:
                Pr.dbg("Item has no equipment slot assigned", 1)

    def unequip_item(self, item_name):
        """enable unequiping equiped items

        Args:
            item_name (str): name of unequiping item
        """
        for index, item in enumerate(self.slots):
            if isinstance(item, str):
                continue
            if item.name == item_name:
                self.inv.append(item)
                self.slots[index] = "placeholder"


class EntityInit:
    """
    Class which Initializes Entities
    Contains Functions:
    load_entities_from_json : Loads all available Entities from a Json File
    load_entities_by_name_from_json : Loads an Entities by it's Name from a Json File

    """

    def load_entities_fromjson(json_file):
        """
        Return alls Entities from Json file

        :json_file (File): Json file to load Entities from

        =return= List of all Entities loaded from Json
        """

        Pr.dbg(f"Loading Entities from: {json_file}")

        curEntities = []
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for ename in data.keys():
            if ename[0] != "$":
                curEntities.append(Entity.from_json(data[ename]))
        return curEntities

    def load_entities_by_name_from_json(json_file, name):
        """
        Return a single Entitiy Object from Json by given Name

        :json_file (File): Json File to load Entity from

        =return= Entity object
        """
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)
            Pr.dbg(data)

        for ename in data.keys():
            if ename == name:
                return Entity.from_json(data[ename])

        Pr.dbg(f"Itemname: {Pr.cyan(name)} not found!", 1)
        return False
