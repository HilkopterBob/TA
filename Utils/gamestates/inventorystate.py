import questionary
from Utils import pr


"""
TODO:
Gamelogic: Was wird actionpaser und was direkt abgeabreitet?




"""

def inventorystate(Player):

    


            





    wants_exit = False
    weapons = []
    tools = []
    potions = []
    misc = []
    for item in Player.inv:
        if item.itype == "weapon":
            weapons.append(item.name)
        if item.itype == "tool":
            tools.append(item.name)
        if item.itype == "potion":
            potions.append(item.name)
        if item.itype == "misc":
            misc.append(item.name)
        

    while wants_exit != True:

        inventory_space = questionary.select(
            'Choose 1Type:',
            choices=[
                "Weapons",
                "Tools",
                "Potions",
                "Misc",
                "zurück zum Spiel"
            ]).unsafe_ask()
        
        match inventory_space:
            case "Weapons":
                choosen_item = questionary.select(
                'Weapons',
                choices=weapons).unsafe_ask()
            case "Tools":
                try:
                    choosen_item = questionary.select(
                    'Tools',
                    choices=tools).unsafe_ask()
                except ValueError as e:
                    pr.Pr.dbg(f"Catched Error: {e}.\n\t\t\t\t\t\t It may be an empty Inventory Space.", 1)
            case "Potions":
                try:
                    choosen_item = questionary.select(
                    'Potions',
                    choices=potions).unsafe_ask()
                except ValueError as e:
                    pr.Pr.dbg(f"Catched Error: {e}.\n\t\t\t\t\t\t It may be an empty Inventory Space.", 1)
            case "Misc":
                try:
                    choosen_item = questionary.select(
                    'Misc',
                    choices=misc).unsafe_ask()
                except ValueError as e:
                    pr.Pr.dbg(f"Catched Error: {e}.\n\t\t\t\t\t\t It may be an empty Inventory Space.", 1)
            case "zurück zum Spiel":
                wants_exit = True
            case _:
                print("No valid choice made")
        
        try:
            print(choosen_item)
            



        except UnboundLocalError as e:
            pr.Pr.dbg(f"Catched Error: {e}.\n\t\t\t\t\t\t It may be an empty Inventory Space, which tried to by printed.", 1)
        
        if wants_exit == True:
            break

