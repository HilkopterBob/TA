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
        
        def applyeffect(attributes = []):
            _entity = attributes[0]
            _effectname = attributes[1]
            _effect = EffectInit.load_effect_by_name_from_json(config.effects_file,_effectname)
            pr.dbg(f"{pr.cyan(f'{_effect.name}')} applied to {pr.cyan(f'{_entity.name}')}")
            return 0
        
        def takeeffects(attributes = []):
            pr.dbg(attributes)
            _entity = attributes[0]
            _entity.let_effects_take_effect([attributes[1]])
            return 0



#How to use:
# call: actionparser.callfunction("applyeffect",["Entityname","Effectname"]))
