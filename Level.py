"""
Levels Module which holds 2 Classes
    Level()
    Levelinit()
"""
import json
from Utils import Pr


class Level:
    """
    Class which defines Levels
    Contains Functions:
    from_json : Creates Levels from JSON
    """

    def __init__(
        self,
        text=None,
        choices=None,
        name="Levelnameplatzhalter",
        inv=None,
        ltype="Testtype",
        descr="Standartdescription du Sohn einer Dirne",
        entitylist=None,
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

        self.name = name
        self.descr = descr
        self.text = text
        self.choices = choices
        self.inv = inv
        self.triggers = triggers
        self.ltype = ltype
        self.entitylist = entitylist

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
                Pr.dbg(
                    f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                )
                Pr.dbg(f"Trying to add {entity.name} to {Level.levelname(self)}")
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
                    Pr.dbg(f"{entity.name} got added to Level {Level.levelname(self)}")
                    Pr.dbg(
                        f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                    )
                    return True
                except Exception as e:
                    Pr.dbg(e, 1)
                    return False
            case "-":
                Pr.dbg(
                    f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                )
                Pr.dbg(f"Trying to remove {entity.name} from {Level.levelname(self)}")
                try:
                    self.entitylist = list(
                        filter(lambda e: e.name != entity.name, self.entitylist)
                    )
                    Pr.dbg(
                        f"{entity.name} got removed from Level {Level.levelname(self)}"
                    )
                    Pr.dbg(
                        f"Entitylist of Level {Level.levelname(self)}: {self.entitylist}"
                    )
                    return True
                except:
                    return False
            case _:
                return Pr.dbg("got no right ctype. choose between + and -", 1)

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
            Pr.dbg(f"ERR: {e}", 2)
            return None


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

        Pr.dbg(f"Loading Levels from: {json_file}")

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
            Pr.dbg(f"Levelname: {Pr.cyan(name)} not found!", 1)
        return False
