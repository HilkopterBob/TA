import questionary
from Utils import pr


"""
TODO:
Gamelogic: Was wird actionpaser und was direkt abgeabreitet?




"""

def inventorystate(Player):

    wants_exit = False

    def consume_item_inv_helper(Player, choosen_item):
        print("consume_item_inv_helper called!!!")
        for item in Player.inv:
            print(Player.inv)
            print(item)
            try:
                if choosen_item == item.name:
                    if item.usable == True:
                        action = questionary.select(
                            f'Möchtest du {choosen_item} verbrauchen?',
                            choices=["ja", "nein"]).unsafe_ask()
                        if action == "ja":
                            pr.Pr.dbg(f"Player Health:                  {Player.hp}", 3)
                            pr.Pr.dbg(f"Player inv:                 {Player.inv}", 3)
                            Player.consume_item(choosen_item)
                            pr.Pr.dbg(f"Player Health:                  {Player.hp}", 3)
                            pr.Pr.dbg(f"Player inv:                 {Player.inv}", 3)
                        else:
                            break
                    if item.equipable == True:
                        action = questionary.select(
                        f'Möchtest du {choosen_item} ausrüsten?',
                        choices=["ja", "nein"]).unsafe_ask()
                        print(action)
                        if action == "ja":
                            pr.Pr.dbg(f"Player Health: {Player.equip_slots}", 3)
                            pr.Pr.dbg(f"Player inv: {Player.inv}", 3)
                            Player.equip_item(choosen_item)
                            pr.Pr.dbg(f"Player Health: {Player.equip_slots}", 3)
                            pr.Pr.dbg(f"Player inv: {Player.inv}", 3)
                        else:
                            break
                        
            except Exception as e:
                print(e)
                print(item)


    while wants_exit != True:

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
                print(item)
                potions.append(item.name)
            if item.itype == "misc":
                misc.append(item.name)
        print(potions)

        inventory_space = questionary.select(
            'Choose 1Type:',
            choices=[
                "Weapons",
                "Tools",
                "Potions",
                "Misc",
                "Equipment ablegen",
                "zurück zum Spiel"
            ]).unsafe_ask()
        
        match inventory_space:
            case "Weapons":
                if len(weapons) != 0:
                    choosen_item = questionary.select(
                    'Weapons',
                    choices=weapons).unsafe_ask()
                else:
                    choosen_item = questionary.select(
                    'Du hast momentan keine Waffen im Inventar. Hast du sie vielleicht grade ausgerüstet?',
                    choices=["zurück"]).unsafe_ask()
            case "Tools":
                if len(tools) != 0:
                    choosen_item = questionary.select(
                    'Tools',
                    choices=tools).unsafe_ask()
                else:
                    choosen_item = questionary.select(
                    'Du hast momentan keine Tools im Inventar.',
                    choices=["zurück"]).unsafe_ask()
            case "Potions":
                if len(potions) != 0:
                    choosen_item = questionary.select(
                    'Potions',
                    choices=potions).unsafe_ask()
                    if choosen_item != "zurück":
                        consume_item_inv_helper(Player, choosen_item)
                else:
                    choosen_item = questionary.select(
                    'Du hast momentan keine Tränke im Inventar.',
                    choices=["zurück"]).unsafe_ask()
            case "Misc":
                if len(misc) != 0:
                    choosen_item = questionary.select(
                    'Misc',
                    choices=misc).unsafe_ask()
                else:
                    choosen_item = questionary.select(
                    'Du hast momentan kein Zeugs im Inventar.',
                    choices=["zurück"]).unsafe_ask()
            case "Equipment":
                #print(Player.equip_slots)
                choosen_item = questionary.select(
                    'Du hast momentan kein Zeugs im Inventar.',
                    choices=["zurück"]).unsafe_ask()
                Player.unequip_item(choosen_item)
            case "zurück zum Spiel":
                wants_exit = True
            case "zurück":
                pass
            case _:
                print("No valid choice made")
        
        
        try:
            print(choosen_item)
            



        except UnboundLocalError as e:
            pr.Pr.dbg(f"Catched Error: {e}.\n\t\t\t\t\t\t It may be an empty Inventory Space, which tried to by printed.", 1)
        
        if wants_exit == True:
            break

