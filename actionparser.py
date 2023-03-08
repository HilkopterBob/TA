from Effect import Effect, EffectInit
from config import config
import Utils as pr

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
            _entity = attributes[0]
            _effectname = attributes[1]
            _effect = EffectInit.load_effect_by_name_from_json(config.effects_file,_effectname)
            _entity.add_effect(_effect)
            pr.dbg(f"{pr.cyan(f'{_effect.name}')} applied to {pr.cyan(f'{_entity.name}')}")
            return 0
        
        def take_effects(attributes = []):
            pr.dbg(attributes)
            _entity = attributes[0]
            _entity.let_effects_take_effect([attributes[1]])
            return 0
        
        def change_location(attributes = []):
            _entity = attributes[0]
            _old_level = attributes[1]
            _new_level = attributes[2]
            _entity.change_location(_old_level, _new_level)
            return 0
        
        def set_name(attributes = []):
            _entity = attributes[0]
            _entity.set_name()
            return 0
        
        def change_health(attributes = []):
            _entity = attributes[0]
            _value = attributes[1]
            _entity.change_health(_value)
            return 0
        
        def add_item(attributes = []):
            _entity = attributes[0]
            _item = attributes[1]
            return 0
        
        def remove_item_by_name(attributes = []):
            _entity = attributes[0]
            _iname = attributes[1]
            _entity.remove_item_by_name(_iname)
            return 0
        
        def remove_item_by_index(attributes = []):
            _entity = attributes[0]
            _index = attributes[1]
            _quest = attributes[2]
            _entity.remove_items_by_index(_index)
            return 0
        
        def add_effect(attributes = []):
            _entity = attributes[0]
            _effect = attributes[1]
            _entity.add_effect(_effect)
            return 0
        
        def show_effects(attributes = []):
            _entity = attributes[0]
            _entity.show_effects()
            return 0

        def remove_effect_by_name(attributes = []):
            _entity = attributes[0]
            _ename = attributes[1]
            _entity.remove_effect_by_name(_ename)
            return 0
        
        def change_stat(attributes = []):
            _entity = attributes[0]
            _effect = attributes[1]
            _entity.change_stat(_effect)
            return 0
        
        def check_level_up(attributes = []):
            _entity = attributes[0]
            _entity.check_level_up()

        

        



            




#How to use:
# call: actionparser.callfunction("applyeffect",["Entityname","Effectname"]))
