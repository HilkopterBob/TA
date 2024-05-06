from .Utils import *
from pystyle import Write, Colors, Colorate
import json

class Level():

    def __init__(self, text=[], choices=[], name="Levelnameplatzhalter", inv=[], ltype="Testtype", descr="Standartdescription du Sohn einer Dirne", entitylist = [], triggers=[]):
        self.name = name
        self.descr = descr
        self.text = text                #
        self.choices = choices          #[["erste option"],["zweite option"],["dritte option",{trigger03:True}]]
        self.inv = inv
        self.triggers = triggers        #stores dicts in form: {searched_room?:True} → show new options
        self.ltype = ltype              #zivilisiert, Wald, Wild, feindlich, höllisch, idyllisch etc. → leveleffekte (zivilisiert: human race atk+, wald: elben atk+, wild: animal spawn rate+ etc.)
        self.entitylist = entitylist    #List of child entities in level

    @staticmethod   #Generate Level from Json
    def from_json(json_dct, lname):
        return Level(json_dct['text'], json_dct['choices'], lname, json_dct['inv'], json_dct['ltype'], json_dct['descr'], json_dct['entitylist'], json_dct['triggers'])


    def change_entity_list(self, ctype, entity, dbg=True):
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
                            raise Exception(f"{cyan(entity.name)} is already in entitielist of Level {cyan(self.name)} and thus cannot be added.")
                    self.entitylist.append(entity)
                    return True
                except Exception as e:
                    if dbg == True:
                        dbg(e, 1)
                    else:
                        stop_game_on_exception(e)
                    return False
            case "-":
                try:
                    self.entitylist = list (filter(lambda e: e.name != entity.name, self.entitylist))
                    return True
                except:
                    return False
            case _:
                return dbg("got no right ctype. choose between + and -",1)



class LevelInit():
    def load_all_levels_from_json(json_file, _curLevels = []):
        """
            Return alls Levels from Json file

            :json_file (File): Json file to load Levels from
            :_curLevels (List): Internally used for recursion

            =return= List of all Levels loaded from Json
        """
        #Populate curLevels for recursion
        curLevels = _curLevels

        #if json_file is not empty
        if json_file:
            #and if json file is actually a file
            if (type(json_file) != dict):
                #open the file
                with open(json_file, encoding="UTF-8") as json_data:
                    #and load its content
                    data = json.load(json_data)
            #if json file is already json data
            else:
                #read json data
                data = json_file

        #for each level in data
        for lname in data.keys():
            #Check needed to Exclude Schema
            if (lname[0] != "$"):
                #check if child levels exist
                if data[lname].get("child_levels"):
                    #populate childlevel array
                    childlevels = data[lname].get("child_levels")
                    #run this function recursively for all childlevels in given level
                    LevelInit.load_all_levels_from_json(childlevels, curLevels)
                #if there are no more Child levels create the Level and append it to curLevels list for Output
                curLevels.append(Level.from_json(data[lname], lname))
        #return Current Levels
        return curLevels



    def load_level_by_name_from_json(json_file, name):
        """
            Return a single Level Object from Json/File by given Name

            :json_file (File): Json File to load Level from

            =return= Level object
        """
        if json_file:
            if (type(json_file) != dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

            for lname in data.keys():
                if name == lname:
                    return Level.from_json(data[lname], lname)
            dbg(f"Levelname: {cyan(name)} not found!",1)
        return False
