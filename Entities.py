import Utils as pr
import Effect 
import json

class Entity():

    #name = "Blankoname"
    #health = 100
    #wealth = 100
    #xp = 0
    #inv = [["Waffen"],["Rüstung"],["Usables"],["Questitems"],["Misc"]]
    #type = Tank, Thief, Elf, Ork, Dwarf, Hurensohn etc.

    def __init__(self, name="Blanko", health=100, wealth=100, xp=0, inv=[], ptype="", effects=[]):
        self.name = name
        self.health = health
        self.wealth = wealth
        self.xp = xp
        self.inv = inv
        self.ptype = ptype
        self.effects = effects

    def set_name(self):
        while True:
            self.name = pr.inp("Wie soll der Held deiner Geschichte heißen?")
            pr.n(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = pr.inp("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
            if action == "y":
                break
    
    def change_health(self, value=0):
        """
            Changes the Player Health

            :value: Amount to Change
            
            =return= Returns True if successfull otherwise returns false
        """ 
        try:
            self.health += value
            return True
        except:
            return False
        
    def add_item(self, iname="", itype=""):
        """
            Adds Item to Inventory

            :iname: Name of Item
            :itype: Type of Item
            
            =return= Returns True if successfull otherwise returns false
        """ 
        try:
            self.inv.append(item(iname, itype))
            return True
        except:
            return False
        
    def remove_item_by_name(self, iname=""):
        """
            Removes Item by given Itemname, if no Name is given no Item will be removed.

            :iname: Name of Item which should be removed
            
            =return= Returns True if successfull otherwise returns false
        """ 
        try:
            self.inv = list (filter(lambda i: i.name != iname, self.inv))
            return True
        except:
            return False
        
    def remove_item_by_index(self, index=-1):
        """
            Removes Item by given Index, if no Index is given the last Item in Inventory will be removed.

            :index: Index of Item which should be removed
            
            =return= Returns True if successfull otherwise returns false
        """ 
        try:
            self.inv.pop(index)
            return True
        except:
            return False

    def add_effect(self, effect):
        """
            appends effect to coresponding list

            :effect: OBJECT! 

            =return= Returns True if successfull otherwise returns false
        """
        try:
            self.effects.append(effect)
            return True
        except:
            return False
        
    def show_effects(self, names=True):
        """
            prints element.name of effects[]

            :names: shows only the effect.name if True, false shows var(effect)

            only for debug!
        """
        try:
            if names==True:
                try:
                    for e in self.effects:
                        print(e.name)
                    return True
                except e:
                    print(e)
                    return False
            else:
                try:
                    for e in self.effects:
                        print(vars(e))
                    return True
                except:
                    return False
        except:                                     #Python: *unterstützt fehlerabfragen*, Nick: "Hold my Beer!"
            return False
        
    def remove_effect_by_name(self, ename=""):
        """
            removes effect from entity by given name
            :ename: effect.name as string
        
            =return= returns true if successfull, else false
        """
        try:
            self.effects = list (filter(lambda e: e.name != ename, self.effects))
            return True
        except:
            return False

    def reomove_effect_by_index(self, index=-1):
        """
            removes effect by given index
        
            :index: index of effect that should be removed
        
            =return= true if successfull else false
        """
        try:
            self.effects.pop(index)
            return True
        except:
            return False
        
class item():
    def __init__(self, name="placeholder", itype="misc", dmg=0, condition=0, effects = [],useable=False, equipable=False, questitem=False, ):
        self.name = name
        self.itype = itype
        self.dmg = dmg
        self.condition = condition
        self.effects = effects
        self.usable = useable
        self.equipable = equipable
        self.questitem = questitem
        
    @staticmethod   #Generate Object from Json
    def from_json(json_dct, iname):
      return item(iname, json_dct['type'], json_dct['dmg'], json_dct['condition'], json_dct['effects'], json_dct['useable'],json_dct['equipable'],json_dct['questitem'])



class itemInit():
    def load_all_items_from_json(json_file):
        """
            Return alls Items from Json file
            
            :json_file (File): Json file to load Items from

            =return= List of all Items loaded from Json
        """
        curItems = []
        with open('items.json') as json_data:
            data = json.load(json_data)
            
        for iname in data.keys():
            curItems.append(item.from_json(data[iname], iname))
        return curItems

    def load_item_by_name_from_json(json_file, name):
        """
            Return a single item Object from Json by given Name
            
            :json_file (File): Json File to load Item from

            =return= Item object
        """
        with open('items.json') as json_data:
            data = json.load(json_data)
            

        for iname in data.keys():
            if iname == name:
                return item.from_json(data[iname], iname)
            else: 
                return False