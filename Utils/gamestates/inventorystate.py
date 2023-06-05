import questionary
from Utils import pr


"""
TODO:
Gamelogic: Was wird actionpaser und was direkt abgeabreitet?




"""

def inventorystate(Player):

    def consume_item(item_name, Player):
        for item in Player.inv:
            if item.name == item_name:
                consumable = item

        if consumable.effects and consumable.type != "Food":
            Player.remove_item_by_name(consumable.name)
            for effect in consumable.effects:
                Player.add_effect(effect)

        if consumable.type == "Food":
            Player.change_health(consumable.dmg)

    def equip_item(item_name, Player):
        
        for item in Player.inv:
            if item.name == item_name:
                cur_item = item
        
        #["Head_slot", "Torso_slot", "Underwear", "Left_arm", "Right_arm", 
        #"Left_leg", "Right_leg", "Gloves_slot", "Meele Weapon", "Ranged Weapon", 
        #"Quick_draw potion"]

        
        match cur_item.equip_slot:
            case "head":
                Player.equip_slot[0] = cur_item
            case "torso":
                Player.equip_slot[1] = cur_item
            case "underwear":
                Player.equip_slot[2] = cur_item
            case "left_arm":
                Player.equip_slot[3] = cur_item
            case "right_arm":
                Player.equip_slot[4] = cur_item
            case "left_leg":
                Player.equip_slot[5] = cur_item
            case "right_leg":
                Player.equip_slot[6] = cur_item
            case "gloves":
                Player.equip_slot[7] = cur_item
            case "meele":
                Player.equip_slot[8] = cur_item
            case "ranged":
                Player.equip_slot[9] = cur_item
            case "quick_draw_potion":
                Player.equip_slot[10] = cur_item
            





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

