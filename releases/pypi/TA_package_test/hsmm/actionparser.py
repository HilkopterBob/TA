from .Effect import Effect, EffectInit
import os
from .Utils import *

PATH = os.path.dirname(os.path.realpath(__file__))
global items_file
global levels_file
global effects_file
global entity_file
items_file = str(PATH+r"/conf/items.json")
levels_file = str(PATH+r"/conf/levels.json")
effects_file = str(PATH+r"/conf/effects.json")
entity_file = str(PATH+r"/conf/entities.json")



class Actionparser:


        def callfunction(attr = []):

            #attr = ["",["","",""]]
            #attr[0] == Name of Function to be Called
            #attr[1] == ["",["",""]]
                #attr[1][0] == The Entity to which the Action should be Applied
                #attr[1][1] == The Arguments for that
            _call = getattr(Actionparser,attr[0])
            return _call(attr[1])

        def applyeffect(attributes = []):
            _entity = attributes[0]
            _effectname = attributes[1]
            _effect = EffectInit.load_effect_by_name_from_json(effects_file,_effectname)
            dbg(f"{cyan(f'{_effect.name}')} applied to {cyan(f'{_entity.name}')}")
            return 0

        def takeeffects(attributes = []):
            dbg(attributes)
            _entity = attributes[0]
            _entity.let_effects_take_effect([attributes[1]])
            return 0



#How to use:
# call: actionparser.callfunction("applyeffect",["Entityname","Effectname"]))
