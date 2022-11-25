import Utils as pr

class Player():

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
                
    
class item():
    def __init__(self,name="placeholder", itype="weapon"):
        self.name = name
        self.itype = itype
        
