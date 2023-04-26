"""
Levels Module which holds 2 Classes
    Level()
    Levelinit()
"""
import json
from Utils import pr


class Level():
    """
        Class which defines Levels
        Contains Functions:
        from_json : Creates Levels from JSON
    """
    def __init__(   self,
                    text=None,
                    choices=None,
                    name="Levelnameplatzhalter",
                    inv=None,
                    ltype="Testtype",
                    descr="Standartdescription du Sohn einer Dirne",
                    entitylist = None,
                    triggers=None
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
        return Level(json_dct['text'],
                    json_dct['choices'],
                    lname, json_dct['inv'],
                    json_dct['ltype'],
                    json_dct['descr'],
                    json_dct['entitylist'],
                    json_dct['triggers'])


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
                try:
                    for e in self.entitylist:
                        if e.name == entity.name:
                            raise Exception(f"{pr.cyan(entity.name)} \
                                            is already in entitielist of Level \
                                            {pr.cyan(self.name)} \
                                            and thus cannot be added.")
                    self.entitylist.append(entity)
                    return True
                except Exception as e:
                    pr.dbg(e, 1)
                    return False
            case "-":
                try:
                    self.entitylist = list (filter(lambda e: e.name != entity.name,
                                            self.entitylist))
                    return True
                except:
                    return False
            case _:
                return pr.dbg("got no right ctype. choose between + and -",1)

    def printDesc(self):
        for entry in self.descr:
            if len(entry) > 1:
                if isinstance(entry,str):
                    pr.n(f"{str(entry)}")
                    continue
                if entry[1] in self.triggers:
                    pr.n(f"{str(entry[0])}")
                continue
    
    def getAvailableChoices(self):
        achoices = []
        for choice in self.choices:
            if len(choice) == 1 and choice[0] !="":
                achoices.append(choice[0])
            elif len(choice) > 1:
                for cdict in self.triggers:
                    if choice[1] == cdict:
                        achoices.append(choice[0])
        return achoices
                        
    def printChoices(self):
        i = 1
        for llist in self.choices:
            if len(llist) == 1 and llist[0] != "":
                pr.n(f"{i}. {llist[0]}")
                i = i + 1
            elif len(llist) > 1:
                for ddict in self.triggers:
                    if llist[1] == ddict:
                        pr.n(f"{i}. {llist[0]}")
                        i = i + 1
        return True


class LevelInit():
    """
        Class which Initializes Levels
        Contains Functions:
        load_all_levels_from_json : Loads all available Levels from a Json File
        load_level_by_name_from_json : Loads an Level by it's Name from a Json File

    """
    def load_all_levels_from_json(json_file, _curLevels = None):
        """
            Return alls Levels from Json file
            
            :json_file (File): Json file to load Levels from
            :_curLevels (List): Internally used for recursion

            =return= List of all Levels loaded from Json
        """
        if _curLevels is None:
            _curLevels = []
        curLevels = _curLevels

        if json_file:
            if not isinstance(json_file,dict):
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
            if not isinstance(json_file,dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

            for lname in data.keys():
                if name == lname:
                    return Level.from_json(data[lname], lname)
            pr.dbg(f"Levelname: {pr.cyan(name)} not found!",1)
        return False
