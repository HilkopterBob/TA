"""
Entities Module which holds 2 Classes
    Entity()
    Entityinit()
"""
import json
from Utils import Pr, Inp


class Entity():
    """
        Class which defines Entities
        Contains Functions:
        from_json : Creates Entities from JSON
    """
    def __init__(   self,
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
                    level=1
                    ):

        if inv is None:
            inv = []
        if geffects is None:
            geffects = []
        if beffects is None:
            beffects = []
        if eeffects is None:
            eeffects = []

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
        self.effects = [[self.geffects],[self.beffects],[self.eeffects]]
        self.actionstack = []

    @staticmethod
    def from_json(json_dct):
        """Creates an Entiy from given JSON

        Args:
            json_dct (json): The Json Code to be parsed

        Returns:
            Entity: Entity
        """
        return Entity(  json_dct['name'],
                        json_dct['hp'],
                        json_dct['wealth'],
                        json_dct['xp'],
                        json_dct['inv'],
                        json_dct['ptype'],
                        json_dct['geffects'],
                        json_dct['beffects'],
                        json_dct['eeffects'],
                        json_dct['location'],
                        json_dct['level']
                        )

    def set_name(self):
        """
            Sets the Name of an Entity Object
        """
        while True:
            self.name = Inp.inp("Wie soll der Held deiner Geschichte heißen?")
            Pr.n(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = Inp.inp("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
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
            return True
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
            self.inv = list (filter(lambda i: i.name != iname, self.inv))
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
            self.geffects = list (filter(lambda e: e.name != ename, self.geffects))
            self.beffects = list (filter(lambda e: e.name != ename, self.beffects))
            self.eeffects = list (filter(lambda e: e.name != ename, self.eeffects))
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
                Pr.dbg( f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                        )
            for e in self.geffects:
                self.change_stat(e)
                Pr.dbg( f"{Pr.cyan(e.name)}, \
                        {Pr.cyan(e.etype)} : affected OBJECT: \
                        {Pr.cyan(self.name)}. Value: \
                        {Pr.cyan(e.value)} influenced: \
                        {Pr.cyan(e.infl)}"
                        )
            for e in self.beffects:
                self.change_stat(e)
                Pr.dbg( f"{Pr.cyan(e.name)}, \
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
        self.location = new_level.name
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
                needed_xp = ((self.level + 1 )/0.4) ** 1.79
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp = self.xp - int(needed_xp)
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")


            if self.level >= 10 and self.level < 30:
                needed_xp = ((self.level + 1 )/0.37) ** 1.86
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp -= needed_xp
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")


            if self.level >= 30:
                needed_xp = ((self.level + 1 )/0.2) ** 2.175
                if self.xp > needed_xp:
                    self.level += 1
                    self.xp -= needed_xp
                    level_ups += 1

                if level_ups > 0:
                    Pr.n(f"Du bist {level_ups} Level aufgestiegen!")
                    Pr.n("Du bekommst: nichts.")


            break
        return True

class EntityInit():
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

        Pr.dbg(f"Itemname: {Pr.cyan(name)} not found!",1)
        return False


class gitem():
    """
        Class which defines Items
        Contains Functions:
        from_json : Creates Items from JSON
    """
    def __init__(   self,
                    name="placeholder",
                    itype="misc",
                    dmg=0,
                    condition=0,
                    effects = None,
                    useable=False,
                    equipable=False,
                    questitem=False
                    ):

        if effects is None:
            effects = []

        self.name = name
        self.itype = itype
        self.dmg = dmg
        self.condition = condition
        self.effects = effects
        self.usable = useable
        self.equipable = equipable
        self.questitem = questitem

    def get(self, thing: str, *args):
        """compatibility function for questify
        """
        return self.name

    @staticmethod
    def from_json(json_dct, iname):
        """Creates an Item from given JSON

        Args:
            json_dct (json): The Json Code to be parsed

        Returns:
            Item: Item
        """
        return gitem(iname,
                    json_dct['type'],
                    json_dct['dmg'],
                    json_dct['condition'],
                    json_dct['effects'],
                    json_dct['useable'],
                    json_dct['equipable'],
                    json_dct['questitem'])



class itemInit():
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
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for iname in data.keys():
            curItems.append(gitem.from_json(data[iname], iname))
        return curItems

    def load_item_by_name_from_json(json_file, name):
        """
            Return a single item Object from Json by given Name
            
            :json_file (File): Json File to load Item from

            =return= Item object
        """
        with open(json_file,encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for iname in data.keys():
            if iname == name:
                return gitem.from_json(data[iname], iname)

        Pr.dbg(f"Itemname: {Pr.cyan(name)} not found!",1)
        return False
