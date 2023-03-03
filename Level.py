import Utils as pr
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
                            raise Exception(f"{pr.cyan(entity.name)} is already in entitielist of Level {pr.cyan(self.name)} and thus cannot be added.")
                    self.entitylist.append(entity)
                    return True
                except Exception as e:
                    if dbg == True: 
                        pr.dbg(e, 1)
                    else:
                        pr.stop_game_on_exception(e)
                    return False
            case "-":
                try:
                    self.entitylist = list (filter(lambda e: e.name != entity.name, self.entitylist))
                    return True
                except:
                    return False
            case _:
                return pr.dbg("got no right ctype. choose between + and -",1)



class LevelInit():
    def load_all_levels_from_json(json_file):
        """
            Return alls Levels from Json file
            
            :json_file (File): Json file to load Levels from

            =return= List of all Levels loaded from Json
        """
        curLevels = []
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)
        


        for lname in data.keys():
            if lname["child_levels"] in lname:
                for child_level in data.keys():
                    for lname in data.keys():
                        curLevels.append(Level.from_json(data[lname], lname))
            curLevels.append(Level.from_json(data[lname], lname))
        return curLevels

    def load_level_by_name_from_json(json_file, name):
        """
            Return a single Level Object from Json by given Name
            
            :json_file (File): Json File to load Item from

            =return= Level object
        """
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)
            

        for lname in data.keys():
            if lname == name:
                return Level.from_json(data[lname], lname)
        
        pr.dbg(f"Levelname: {pr.cyan(lname)} not found!",1)
        return False