import Utils as pr

class Level():

    def __init__(self, text=[], choices=[], name="Levelnameplatzhalter", inv=[], ltype="Testtype", descr="Standartdescription du Sohn einer Dirne", entitylist = []):
        self.name = name
        self.descr = descr
        self.text = text
        self.choices = choices 
        self.inv = inv
        self.ltype = ltype              #zivilisiert, Wald, Wild, feindlich, höllisch, idyllisch etc. → leveleffekte (zivilisiert: human race atk+, wald: elben atk+, wild: animal spawn rate+ etc.)
        self.entitylist = entitylist    #List of child entities in level
    

