from Utils import pr, prin, pra


class Player():

    #name = "Blankoname"
    #health = 100
    #wealth = 100
    #xp = 0
    #inv = [["Waffen"],["Rüstung"],["Usables"],["Questitems"],["Misc"]]
    #type = Tank, Thief, Elf, Ork, Dwarf, Hurensohn etc.

    def __init__(self, name, health, wealth, xp, inv, ptype):
        self.name = name
        self.health = health
        self.wealth = wealth
        self.xp = xp
        self.inv = inv
        self.ptype = ptype

    def set_name(self):
        while True:
            global name
            self.name = prin("Wie soll der Held deiner Geschichte heißen?")
            pr(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = prin("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
            if action == "y":
                break

    
        