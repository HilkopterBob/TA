import questionary




def inventorystate(Player):
    wants_exit = False
    weapons = []
    tools = []
    potions = []
    misc = []
    for item in Player.inv:
        if item.itype == "weapon":
            weapons.append(item)
            print(weapons)
        if item.itype == "tool":
            tools.append(item)
        if item.itype == "potion":
            potions.append(item)
        if item.itype == "misc":
            misc.append(item)
        

    while wants_exit != True:

        inventory_space = questionary.select(
            'Choose 1Type:',
            choices=[
                "Weapons",
                "Tools",
                "Potions",
                "Misc",
                "zurück zum Spiel"
            ]).ask()
        
        match inventory_space:
            case "Weapons":
                inventory_space = questionary.checkbox(
                'Choose Type:',
                choices=weapons).ask()
            case "Tools":
                inventory_space = questionary.checkbox(
                'Choose Type:',
                choices=tools).ask()
            case "Potions":
                inventory_space = questionary.checkbox(
                'Choose Type:',
                choices=potions).ask()
            case "Misc":
                inventory_space = questionary.checkbox(
                'Choose Type:',
                choices=misc).ask()
            case "zurück zum Spiel":
                wants_exit = True
            case _:
                print("No valid choice made")
        
        if wants_exit == True:
            break