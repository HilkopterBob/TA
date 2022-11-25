import Utils as pr

class Player():

    #name = "Blankoname"
    #health = 100
    #wealth = 100
    #xp = 0
    #inv = [["Waffen"],["Rüstung"],["Usables"],["Questitems"],["Misc"]]
    #type = Tank, Thief, Elf, Ork, Dwarf, Hurensohn etc.

    def __init__(self, name, health, wealth, xp, inv, ptype, effects):
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
            pr(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = pr.inp("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
            if action == "y":
                break
    
    def change_health(self, value=0):
        self.health += value
        

