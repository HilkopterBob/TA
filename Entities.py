"""
Entities Module which holds 2 Classes
    Entity()
    Entityinit()
"""

import json
import random
from Level import Level
from Utils import Logger, Pr, Inp, loot, AI
from config import aitablepath


class Entity:  # pylint: disable=R0904
    """
    Class which defines Entities
    Contains Functions:
    from_json : Creates Entities from JSON
    """

    __slots__ = (
        "name",
        "hp",
        "wealth",
        "xp",
        "inv",
        "ptype",
        "geffects",
        "beffects",
        "eeffects",
        "effects",
        "location",
        "level",
        "allowdamage",
        "actionstack",
        "slots",
        "attributes",
        "spd",
        "loottable",
        "ai",
        "isPlayer",
        "Team",
        "maxHealth",
    )

    def __init__(
        self,
        name="Blanko",
        health=100,
        wealth=100,
        xp=0,
        inv=None,
        ptype=None,
        geffects=None,
        beffects=None,
        eeffects=None,
        location="Nirvana",
        level=1,
        allowdamage=True,
        slots=None,
        attributes=None,
        loottable=None,
        ai=None,
        spd=0,
        isPlayer=None,
        Team=0,
        maxHealth=None,
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
        if attributes is None:
            attributes = {}
        if ptype is None:
            ptype = []
        if loottable is None:
            loottable = {}
        if ai is None:
            ai = ""
        if isPlayer is None:
            isPlayer = False
        if maxHealth is None:
            maxHealth = 0

        self.location = location
        """Entity Location as Level Object"""
        self.name = name
        """Entity Name as String"""
        self.hp = health
        """Entity Health Points as Integer"""
        self.maxHealth = health
        """MaxHealth for Calculations"""
        self.wealth = wealth
        """Entity Wealth Points as Integer"""
        self.level = level
        """Entity Level as Integer"""
        self.xp = xp
        """Entity Experience Points as Integer"""
        self.inv = inv
        """Entity Inventory as Array"""
        self.ptype = ptype
        """Entity Type as String [Types= "good","bad","neutral"]"""
        self.geffects = geffects
        """List of positive Effects for Entity as Array of Objects"""
        self.beffects = beffects
        """List of negative Effects for Entity as Array of Objects"""
        self.eeffects = eeffects
        """List of evil Effects for Entity (Mainly Boss Effects) as Array of Objects"""
        self.effects = [[self.geffects], [self.beffects], [self.eeffects]]
        """Entities list of effects to be applied as Array of Arrays Containing [gEffects, bEffects, eEffects]"""  # pylint:disable=C0301
        self.actionstack = []
        """Current Queue of actions for entity as Array"""
        self.slots = slots
        """Entity Slots ["Head_slot", "Torso_slot", "Underwear", "Left_arm", "Right_arm","Left_leg", "Right_leg", "Gloves_slot","Meele Weapon", "Ranged Weapon","Quick_draw potion"]"""  # pylint:disable=C0301
        self.allowdamage = allowdamage
        """Entity allowDamage Flag as Boolean"""
        self.attributes = attributes
        """Attributes of Entity"""
        self.spd = spd
        """The Speed of the Entity in Combat, gets Calculated from INI"""
        self.loottable = loottable
        """The loottable attached to this Entity"""
        self.ai = self.get_ai(ai)
        """The used AI Parameters for this Entity"""
        self.isPlayer = isPlayer
        """Checks if Entity is Player or not"""
        self.Team = Team
        """Defines the Team this Entity is on"""

    def __str__(self):
        return f"{self.name}"

    # Commented out for readability in Logfile - need to find a workaround
    # def __repr__(self):
    #    return f"[{self.__class__.__module__}.{self.__class__.__name__}('{self.name}',{self.hp},{self.wealth},{self.xp},[{self.inv}],[{self.ptype}],[{self.geffects}],[{self.beffects}],[{self.eeffects}],'{self.location}',{self.level},{self.allowdamage},[{self.slots}],{self.attributes},{self.loottable},{self.ai},{self.spd},{self.isPlayer},{self.Team},{self.maxHealth}) at <{hex(id(self))}>]"  # pylint:disable=C0301

    @staticmethod
    def from_json(json_dct):
        """Creates an Entiy from given JSON

        Args:
            json_dct (json): The Json Code to be parsed

        Returns:
            Entity: Entity
        """
        _loottable = loot.getLootTable(json_dct["loottable"])
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
            json_dct["allowdamage"],
            json_dct["slots"],
            json_dct["attributes"],
            _loottable,
            json_dct["ai"],
            0,
            json_dct["isPlayer"],
            json_dct["Team"],
        )

    def get_ai(self, table):
        """Returns Content of Loottable given by Name

        Args:
            name (String): Name of the Loottable that should be used

        Returns:
            Dict: Loottable | None if Error
        """
        if table is None:
            return None
        if table == "":
            return None

        _json_file = aitablepath + "/" + table + ".json"

        Logger.log(f"Loading AI Params {_json_file}", -1)

        with open(_json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)
        return data

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
                if self.allowdamage:  #  pylint: disable=R1705
                    Logger.log(f"Entity {self.name} has 0 or less Health")
                    return True
                else:
                    self.hp = 1
                    Logger.log(
                        f"Entity {self.name} is not allowed to take \
                        Damage Allowdamage: {self.allowdamage}",
                        1,
                    )
                    return False
            return False
        except:
            return False

    def getTarget(self, entitylist):
        """Selects a Target Entity from List of Entities

        Args:
            entitylist (List): List of Entities
        Return:
            entity (entity): Selected Entity
        """
        _entitylist = []
        for i, e in enumerate(entitylist):
            Logger.log(f"Entity in list: ({i}){e}({e.name})")
            if e.Team != self.Team:
                _entitylist.append(e)
        _target = random.choice(_entitylist)
        return _target

    def act(self):
        """Function for Entity Intelligence"""
        if not self.location:
            Logger.log(
                f"Location for Entity {self}({self.name}) is not set Correctly: {self.location}",
                2,
            )
            return
        _entitylist = self.location.entitylist
        Logger.log(f"Entitylist: {_entitylist}")
        Logger.log(f"Entity {self}({self.name}) is acting here!")
        match (AI.calcbehaviour(self)):
            case 0:
                Logger.log("Entity would Flee")
            case 1:
                Logger.log("Entity would Attack")
                _selectedEntity = self.getTarget(_entitylist)
                Logger.log(
                    f"Targetted Entity: {_selectedEntity}({_selectedEntity.name})"
                )
                Logger.log(
                    f"Entity {self}({self.name}) attacks {_selectedEntity}({_selectedEntity.name})"
                )
                _damage = {
                    "AD": 1,
                    "AP": 0,
                }  # Set Default Damage #ToDo: Move to somewhere else
                if (
                    len(self.slots) != 0
                ):  # Prevent Crash if no Slots are used #ToDo: Fix
                    if self.slots[8] is None:
                        _weapon = None
                        _weaponname = "Hand"
                    else:
                        _weapon = self.slots[8]
                        _weaponname = _weapon.name
                        _damage = _weapon.getDamage()
                _selectedEntity.actionstack.append(
                    ["take_damage", [_selectedEntity, _damage, self]]
                )
            case 2:
                Logger.log("Entity would Buff")
            case 9:
                Logger.log("Entity is Player")
            case _:
                Logger.log("Unhandled or Error")

        # If health is low and aggression is low too -> flee
        # If health is low and aggression is high -> Attack with all of its power
        # If health is low and aggression is medium -> try to heal

        # if there are more than 1 enemys attack the one with lowest hp

    def take_damage(self, value=None, inflicter=None):
        """Adds Damage to the Entity and Calculates health loss based on Armor and Resistance

        Args:
            value (dict): Damage that is Inflicted. Defaults to {"AD":0,"AP":0}.

        =return= Returns Damage taken as Dict of AD and AP;
                If Entity dies from Damage this function returns TRUE
        """
        if value is None:
            value = {"AD": 0, "AP": 0}
        if inflicter is None:
            inflicter = None

        resistance = {}
        ar = 0
        mr = 0

        if self.isPlayer:
            Pr.n(f"Du wirst von {inflicter.name} angegriffen.")

        Logger.log(f"{self.name} is about to take {value} damage from {inflicter}", 1)

        # TODO: Fix order in which damage is inflicted / actionstack is worked

        for i in range(0, 8):
            try:
                if self.slots[i].itype != "armor":  # pylint: disable=E1101
                    Logger.log(f"There is no Armor Item in Slot {i}", 0)
                else:
                    ar += self.slots[i].ar  # pylint: disable=E1101
                    mr += self.slots[i].mr  # pylint: disable=E1101
                    resistance = {"AR": ar, "MR": mr}
            except Exception:
                Logger.log(f"There is no Valid Item in Slot {i}", 0)

        if not resistance:
            resistance = {"AR": 0, "MR": 0}

        attacklist = list(value.values())
        resistancelist = list(resistance.values())
        Logger.log(f"{self.name} has {resistance} defence")
        _attacklist = []
        for c, v in enumerate(attacklist):
            if v != 0:
                _attack = v * (v / (v + resistancelist[c]))
            else:
                _attack = v
            _attacklist.append(round(_attack, 1))
        damage = dict(zip(value.keys(), _attacklist))
        Logger.log(f"{self.name} taking {damage} damage")

        if self.isPlayer:
            Pr.n(f"Du bekommst {damage} schaden.")

        for i in _attacklist:
            _ret = self.change_health(i * -1)
            if _ret:
                Logger.log(f"{self.name} is destroyed!")
                # TODO: remove Entity from Entitylist so it doesn't get counted in action parsing
                self.actionstack = []
                try:
                    _loot = loot.roll_loot(self.loottable, 1)
                    Logger.log(f"Entity Lootroll for 1 Item: {_loot}")
                    Pr.n(
                        f"{self.name} wurde besiegt! Und hat {_loot[0].name} fallen gelassen."
                    )
                    if inflicter:
                        if inflicter.add_item(_loot[0]):
                            Logger.log(f"Item {_loot[0]} has been successfully added")
                        # TODO: Add XP to Inflicter
                except Exception as e:
                    Logger.log(e, 2)
            return _ret
        return damage

    def add_item(self, item):
        """
        Adds Item to Inventory

        :iname: Name of Item
        :itype: Type of Item

        =return= Returns True if successfull otherwise returns false
        """
        Logger.log(f"Trying to Add {item} to {self.name}'s Inventory")
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

    def change_stat(self, effect, value):
        """
        changes stat (effect.infl) by value

        :effect(string): effect name

        :value(int/double): effect value

        =return= true if sucessfull, else false
        """

        match effect:
            case "hp":
                try:
                    self.hp += value
                    return True
                except:
                    return False
            case "xp":
                try:
                    self.xp += value
                    return True
                except:
                    return False
            case _:
                Logger.log("change_stat: WILDCARD AUSGELÖST! debuginfo:", 2)
                Logger.log(vars(self))
                Logger.log(vars(effect))
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
                Logger.log(
                    f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                )
            for e in self.geffects:
                self.change_stat(e)
                Logger.log(
                    f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                )
            for e in self.beffects:
                self.change_stat(e)
                Logger.log(
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
        errstate = False
        if not isinstance(old_level, Level) or not isinstance(new_level, Level):
            Logger.log("Level not Level Object!", 2)
            Logger.log(
                f"OldLevel: {old_level} | {type(old_level)},"
                f" New_Level: {new_level} | {type(new_level)}",
                2,
            )
            errstate = True
        Logger.log(f"Changing Level for {self} from {old_level} to {new_level}")
        self.location = new_level
        new_level.change_entity_list("+", self)
        if not errstate:
            old_level.change_entity_list("-", self)

    def check_level_up(self):
        """
        checks if entity has enough xp to level up,
        will level up the entity UNTIL there are not enough xp

        =return= returns nothing, yet
        """
        level_ups = 0
        old_level = self.level
        Logger.log(f"Previous Level: {old_level}")
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

    def equip_item(self, item_name, slot=""):
        """enables equiping of eqipment"""
        for item in self.inv:
            if item.name == item_name:
                cur_item = item
        if slot == "":
            slot = cur_item.slots[0]

        Logger.log(f"Equipping {item_name} in {slot}", -1)
        match slot:
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
                Logger.log("Item has no equipment slot assigned", 1)

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

        Logger.log(f"Loading Entities from: {json_file}")

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

        for ename in data.keys():
            if ename == name:
                return Entity.from_json(data[ename])

        Logger.log(f"Itemname: {Pr.cyan(name)} not found!", 1)
        return False
