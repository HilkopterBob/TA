import Utils as pr

class Level():

    def __init__(self, text=[], choices=[], name="Levelnameplatzhalter", inv=[], ltype="Testtype", descr="Standartdescription du Sohn einer Dirne"):
        self.name = name
        self.descr = descr
        self.choices = choices 
        self.inv = inv
        self.ltype = ltype

    #lvltype gibt an ob level feindlich, wild, zivilisiert


