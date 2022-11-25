class Player():

    #name = "Blankoname"
    #health = 100
    #wealth = 100
    #xp = 0
    #inv = [["Waffen"],["Rüstung"],["Usables"],["Questitems"],["Misc"]]

    def __init__(self, name, health, wealth, xp, inv):
        self.name = name
        self.health = health
        self.wealth = wealth
        self.xp = xp
        self.inv = inv

    def set_name(self):
        while True:
            global name
            self.name = pri("Wie soll der Held deiner Geschichte heißen?")
            pr(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = pri("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
            if action == "y":
                break

    def get_name(self):
        pr(f"Dein Held heißt {self.name}.")
        