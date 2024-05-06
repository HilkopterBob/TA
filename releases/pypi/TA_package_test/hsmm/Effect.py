from .Utils import *
import json



class Effect():

    def __init__(self, name="Effektnameplatzhalter", desrc="Effektbeschreibungsplatzhalter", etype="good", value=0, influenced="atk"):
        self.name = name
        self.descr = desrc
        self.etype = etype                  #:Effekttyp, good|bad|evil → siehe Gameloop
        self.value = value
        self.infl = influenced              #:Influenced Vale, welcher Wert beeinflusst wird (hp, xp, atk, def, speed etc)

    @staticmethod   #Generate Level from Json
    def from_json(json_dct, ename):
        return Effect(ename, json_dct["descr"], json_dct["etype"], json_dct["value"], json_dct["infl"])



class EffectInit():
    def load_all_effects_from_json(json_file):
        """
            Return alls Effects from Json file

            :json_file (File): Json file to load Effects from

            =return= List of all Effects loaded from Json
        """
        effects_master_list = []
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)

        for ename in data.keys():
            effects_master_list.append(Effect.from_json(data[ename], ename))
        return effects_master_list

    def load_effect_by_name_from_json(json_file, name):
        """
            Return a single Level Object from Json by given Name

            :json_file (File): Json File to load Item from
            :name (String): Name of Effect to be loaded

            =return= Level object
        """
        with open(json_file, encoding="UTF-8") as json_data:
            data = json.load(json_data)


        for ename in data.keys():
            if name == ename:
                return Effect.from_json(data[ename], ename)

        dbg(f"Effect: {cyan(name)} not found!", 1)
        return False
