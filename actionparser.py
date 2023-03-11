from Effect import Effect, EffectInit
from config import config
from Utils import pr

class Actionparser:
        

        def callfunction(attr = []):
            
            #attr = ["",["","",""]]
            #attr[0] == Name of Function to be Called
            #attr[1] == ["",["",""]]
                #attr[1][0] == The Entity to which the Action should be Applied
                #attr[1][1] == The Arguments for that
            _call = getattr(Actionparser,attr[0])
            return _call(attr[1])
        
        def add_effect(attributes = []):
            try:
                _entity = attributes[0]
                _effectname = attributes[1]
                _effect = EffectInit.load_effect_by_name_from_json(config.effects_file,_effectname)
                _entity.add_effect(_effect)
                return 0
            except:
                return 1
        
        def take_effects(attributes = []):
            try:
                pr.hello()
                pr.dbg(attributes)
                _entity = attributes[0]
                _entity.let_effects_take_effect([attributes[1]])
                return 0
            except:
                return 1
        
        def change_location(attributes = []):
            try:
                _entity = attributes[0]
                _old_level = attributes[1]
                _new_level = attributes[2]
                _entity.change_location(_old_level, _new_level)
                return 0
            except:
                return 1
        
        def set_name(attributes = []):
            try:
                _entity = attributes[0]
                _entity.set_name()
                return 0
            except:
                return 1
        
        def change_health(attributes = []):
            try:
                _entity = attributes[0]
                _value = attributes[1]
                _entity.change_health(_value)
                return 0
            except:
                return 1
        
        def add_item(attributes = []):
            try:
                _entity = attributes[0]
                _item = attributes[1]
                _entity.add_item(_item)
                return 0
            except:
                return 1
        
        def remove_item_by_name(attributes = []):
            try:
                _entity = attributes[0]
                _iname = attributes[1]
                _entity.remove_item_by_name(_iname)
                return 0
            except:
                return 1
        
        def remove_item_by_index(attributes = []):
            try:
                _entity = attributes[0]
                _index = attributes[1]
                _quest = attributes[2]
                _entity.remove_items_by_index(_index)
                return 0
            except:
                return 1
        
        def add_effect(attributes = []):
            try:
                _entity = attributes[0]
                _effect = attributes[1]
                _entity.add_effect(_effect)
                return 0
            except:
                return 1
        
        def show_effects(attributes = []):
            try:
                _entity = attributes[0]
                _entity.show_effects()
                return 0
            except:
                return 1

        def remove_effect_by_name(attributes = []):
            try:
                _entity = attributes[0]
                _ename = attributes[1]
                _entity.remove_effect_by_name(_ename)
                return 0
            except:
                return 1
        
        def change_stat(attributes = []):
            try:
                _entity = attributes[0]
                _effect = attributes[1]
                _entity.change_stat(_effect)
                return 0
            except:
                return 1
        
        def check_level_up(attributes = []):
            try:
                _entity = attributes[0]
                _entity.check_level_up()
                return 0
            except:
                return 1
        

        



            




#How to use:
# call: actionparser.callfunction("applyeffect",["Entityname","Effectname"]))
