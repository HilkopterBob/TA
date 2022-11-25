import Utils as pr



class Effect():

    def __init__(self, name="Effektnameplatzhalter", desrc="Effektbeschreibungsplatzhalter", etype="good", value=0, influenced="atk"):
        self.name = name
        self.descr = desrc
        self.etype = etype                  #:Effekttyp, good|bad|evil → siehe Gameloop
        self.value = value
        self.infl = influenced              #:Influenced Vale, welcher Wert beeinflusst wird (hp, xp, atk, def, speed etc)

    
