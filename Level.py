import Utils as pr
from pystyle import Write, Colors, Colorate

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