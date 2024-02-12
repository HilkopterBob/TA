"""
Levels Module which holds 2 Classes
    Level()
    Levelinit()
"""

import json
import random
from Utils import Pr, Logger
from config import entities_folder


class Level:
    """
    Class which defines Levels
    Contains Functions:
    from_json : Creates Levels from JSON
    """

    __slots__ = (
        "name",
        "descr",
        "text",
        "choices",
        "inv",
        "triggers",
        "ltype",
        "entitylist",
        "entityspawn",
    )

    def __init__(
        self,
        text=None,
        choices=None,
        name="Levelnameplatzhalter",
        inv=None,
        ltype="Testtype",
        descr="Standartdescription du Sohn einer Dirne",
        entitylist=None,
        entityspawn=None,
        triggers=None,
    ):
        if text is None:
            text = []
        if choices is None:
            choices = []
        if inv is None:
            inv = []
        if entitylist is None:
            entitylist = []
        if triggers is None:
            triggers = []
        if entityspawn is None:
            entityspawn = []

        self.name = name
        self.descr = descr
        self.text = text
        self.choices = choices
        self.inv = inv
        self.triggers = triggers
        self.ltype = ltype
        self.entitylist = entitylist
        self.entityspawn = entityspawn

        self.onLevelCreate()
        self.populate()

    @staticmethod
    def from_json(json_dct, lname):
        """Creates a Level from JSON

        Args:
            json_dct (JSON): Json Data to be parsed
            lname (String): Levelname

        Returns:
            Level: Level
        """
        return Level(
            json_dct["text"],
            json_dct["choices"],
            lname,
            json_dct["inv"],
            json_dct["ltype"],
            json_dct["descr"],
            json_dct["entitylist"],
            json_dct["entityspawn"],
            json_dct["triggers"],
        )

    def change_entity_list(self, ctype, entity):
        """
        Changes the list of entities for specific level

        :ctype: + for adding, - for subtracting entity from list

        :entity: the entity obj

        :dbg: debug, default = True

        =return= returns True if seccessfull, else false
        """
        match ctype:
            case "+":
                Logger.log(
                    f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                )
                Logger.log(f"Trying to add {entity.name} to {Level.levelname(self)}")
                try:
                    for e in self.entitylist:
                        if e.name == entity.name:
                            raise Exception(
                                f"{Pr.cyan(entity.name)} \
                                            is already in entitielist of Level \
                                            {Pr.cyan(self.name)} \
                                            and thus cannot be added."
                            )
                    self.entitylist.append(entity)
                    self.onEntityJoin(entity)
                    Logger.log(
                        f"{entity.name} got added to Level {Level.levelname(self)}"
                    )
                    Logger.log(
                        f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                    )
                    return True
                except Exception as e:
                    Logger.log(e, 4)
                    return False
            case "-":
                Logger.log(
                    f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                )
                Logger.log(
                    f"Trying to remove {entity.name} from {Level.levelname(self)}"
                )
                try:
                    self.entitylist = list(
                        filter(lambda e: e.name != entity.name, self.entitylist)
                    )
                    self.onEntityLeave(entity)
                    Logger.log(
                        f"{entity.name} got removed from Level {Level.levelname(self)}"
                    )
                    Logger.log(
                        f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                    )
                    return True
                except:
                    return False
            case _:
                return Logger.log("got no right ctype. choose between + and -", 1)

    def printDesc(self):
        """Prints Level Description to User"""
        for entry in self.descr:
            if len(entry) > 1:
                if isinstance(entry, str):
                    Pr.n(f"{str(entry)}")
                    continue
                if entry[1] in self.triggers:
                    Pr.n(f"{str(entry[0])}")
                continue

    def getAvailableChoices(self):
        """Returns the Choices currently available to the User

        Returns:
            list: Choices
        """
        achoices = []
        for choice in self.choices:
            if len(choice) == 1 and choice[0] != "":
                achoices.append(choice[0])
            elif len(choice) > 1:
                for cdict in self.triggers:
                    if choice[1] == cdict:
                        achoices.append(choice[0])

        return achoices

    def printChoices(self):
        """Prints the Available Choices to the User

        Returns:
            Boolean: True
        """
        i = 1
        for llist in self.choices:
            if len(llist) == 1 and llist[0] != "":
                Pr.n(f"{i}. {llist[0]}")
                i = i + 1
            elif len(llist) > 1:
                for ddict in self.triggers:
                    if llist[1] == ddict:
                        Pr.n(f"{i}. {llist[0]}")
                        i = i + 1
        return True

    def levelname(lobject):
        """Return the Name of an Levelobject

        Args:
            object (Level): Level from what you wan't the Objectname

        Returns:
            String: Levelname
        """
        try:
            return lobject.name
        except Exception as e:
            Logger.log(f"ERR: {e}", 2)
            return None

    def populate(self):
        """Populates the Level with Entities from Spawnlist

        Returns:
            Array: List of Entities
        """
        from Entities import EntityInit  # pylint: disable=C0415

        _entitiestospawn = self.entityspawn

        if _entitiestospawn is None or len(_entitiestospawn) < 1:
            Logger.log("No Entities to Spawn in this Level", 2)
            return 1

        _amount = random.randrange(1, len(_entitiestospawn))
        Logger.log(f"Entities to spawn: {_entitiestospawn}, Amount: {_amount}")

        _dict = list(_entitiestospawn.keys())
        _weights = list(_entitiestospawn.values())

        Logger.log(f"Trying to Spawn {_amount} Entities", 1)
        _entity = random.choices(_dict, weights=_weights, k=_amount)
        _entityreturn = []

        for i in _entity:
            Logger.log(f"Loading Entity {i} from Assets", 0)
            _entityreturn.append(
                EntityInit.load_entities_by_name_from_json(
                    f"{entities_folder}\\{i}.json", i
                )
            )

        for e in _entityreturn:
            Logger.log(f"Adding spawned Entity({e}|{e.name}) to Level({self.name})", 1)
            self.change_entity_list("+", e)
        return

    def onLevelCreate(self):
        """This is called whenever an Level is created"""
        Logger.log(f"Created Instance of Level: {self}({self.name})", 0)
        return

    def onEntityJoin(self, entity):
        """This is called whenever an Entity joins a Level

        Args:
            entity (entity): Entity which is joining the Level
        """
        Logger.log(
            f"Entity:{entity}({entity.name}) joined Level: {self}({self.name})", 1
        )
        if entity.isPlayer:
            if len(self.entitylist) > 1:
                # ToDo: Add Chance to put Player into Combat
                # ToDo: Change Chance based on Entity hostility
                Logger.log(f"Entitylist of Level: {self.entitylist}", -1)

                Pr.n(f"Du wirst von {self.entitylist[0].name} angegriffen!")

                entity.actionstack.insert(  # pylint: disable=E1101
                    0, ["change_gamestate", ["combat"]]
                )
        return

    def onEntityLeave(self, entity):
        """This is called whenever an Entity Leaves a Level

        Args:
            entity (entity): Entity which is leaving the Level
        """
        Logger.log(f"Entity:{entity}({entity.name}) left Level: {self}({self.name})", 2)
        return


class LevelInit:
    """
    Class which Initializes Levels
    Contains Functions:
    load_all_levels_from_json : Loads all available Levels from a Json File
    load_level_by_name_from_json : Loads an Level by it's Name from a Json File

    """

    def load_all_levels_from_json(json_file, _curLevels=None):
        """
        Return alls Levels from Json file

        :json_file (File): Json file to load Levels from
        :_curLevels (List): Internally used for recursion

        =return= List of all Levels loaded from Json
        """
        if _curLevels is None:
            _curLevels = []
        curLevels = _curLevels

        Logger.log(f"Loading Levels from: {json_file}")

        if json_file:
            if not isinstance(json_file, dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

        for lname in data.keys():
            if lname[0] != "$":
                if data[lname].get("child_levels"):
                    childlevels = data[lname].get("child_levels")
                    LevelInit.load_all_levels_from_json(childlevels, curLevels)
                curLevels.append(Level.from_json(data[lname], lname))
        return curLevels

    def load_level_by_name_from_json(json_file, name):
        """
        Return a single Level Object from Json/File by given Name

        :json_file (File): Json File to load Level from

        =return= Level object
        """
        if json_file:
            if not isinstance(json_file, dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

            for lname in data.keys():
                if name == lname:
                    return Level.from_json(data[lname], lname)
            Logger.log(f"Levelname: {Pr.cyan(name)} not found!", 1)
        return False
