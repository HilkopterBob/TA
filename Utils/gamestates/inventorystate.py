"""implementation of inventory
"""

import questionary
from Utils import Logger


def inventorystate(Player):
    """implementation of inventory

    Args:
        Player (obj:entity): the player obj.
    """

    wants_exit = False
    default_choice_items = ["zurück"]

    def item_inv_helper(Player, choosen_item):
        for item in Player.inv:
            try:
                if choosen_item == item.name:
                    if item.useable:
                        action = questionary.select(
                            f"Möchtest du {choosen_item} verbrauchen?",
                            choices=["ja", "nein"],
                        ).unsafe_ask()
                        if action == "ja":
                            Logger.log(
                                f"Player Health:                  {Player.hp}", 3
                            )
                            Logger.log(f"Player inv:                 {Player.inv}", 3)
                            Player.consume_item(choosen_item)
                            Logger.log(
                                f"Player Health:                  {Player.hp}", 3
                            )
                            Logger.log(f"Player inv:                 {Player.inv}", 3)
                        else:
                            break
                    if item.equipable:
                        action = questionary.select(
                            f"Möchtest du {choosen_item} ausrüsten?",
                            choices=["ja", "nein"],
                        ).unsafe_ask()
                        if action == "ja":
                            if len(item.slots) > 1:
                                eaction = questionary.select(
                                    f"Wo möchtest du {choosen_item} ausrüsten?",
                                    choices=item.slots,
                                ).unsafe_ask()
                                Player.equip_item(choosen_item, eaction)
                            else:
                                Player.equip_item(choosen_item)
                            Logger.log(f"Player Slots: {Player.slots}", -1)
                        else:
                            break
            except Exception as e:
                Logger.log(e)
                Logger.log(item)

    while not wants_exit:
        weapons = []
        tools = []
        potions = []
        misc = []
        armor = []
        for item in Player.inv:
            if item.itype == "weapon":
                weapons.append(item.name)
            if item.itype == "tool":
                tools.append(item.name)
            if item.itype == "potion":
                potions.append(item.name)
            if item.itype == "misc":
                misc.append(item.name)
            if item.itype == "armor":
                armor.append(item.name)

        weapons.extend(default_choice_items)
        tools.extend(default_choice_items)
        potions.extend(default_choice_items)
        misc.extend(default_choice_items)
        armor.extend(default_choice_items)

        inventory_space = questionary.select(
            "Choose 1Type:",
            choices=[
                "Weapons",
                "Armor",
                "Tools",
                "Potions",
                "Misc",
                "Equipment",
                "zurück zum Spiel",
            ],
        ).unsafe_ask()

        match inventory_space:
            case "Weapons":
                if len(weapons) != 0:
                    choosen_item = questionary.select(
                        "Weapons", choices=weapons
                    ).unsafe_ask()
                    if choosen_item != "zurück":
                        item_inv_helper(Player, choosen_item)
                else:
                    choosen_item = questionary.select(
                        """Du hast momentan keine Waffen im Inventar.
                    Hast du sie vielleicht grade ausgerüstet?""",
                        choices=["zurück"],
                    ).unsafe_ask()
            case "Armor":
                if len(armor) != 0:
                    choosen_item = questionary.select(
                        "Armor", choices=armor
                    ).unsafe_ask()
                    if choosen_item != "zurück":
                        item_inv_helper(Player, choosen_item)
                else:
                    choosen_item = questionary.select(
                        """Du hast momentan keine Ausrüstung im Inventar.
                    Hast du sie vielleicht grade ausgerüstet?""",
                        choices=["zurück"],
                    ).unsafe_ask()
            case "Tools":
                if len(tools) != 0:
                    choosen_item = questionary.select(
                        "Tools", choices=tools
                    ).unsafe_ask()
                else:
                    choosen_item = questionary.select(
                        "Du hast momentan keine Tools im Inventar.", choices=["zurück"]
                    ).unsafe_ask()
            case "Potions":
                if len(potions) != 0:
                    choosen_item = questionary.select(
                        "Potions", choices=potions
                    ).unsafe_ask()
                    if choosen_item != "zurück":
                        item_inv_helper(Player, choosen_item)
                else:
                    choosen_item = questionary.select(
                        "Du hast momentan keine Tränke im Inventar.", choices=["zurück"]
                    ).unsafe_ask()
            case "Misc":
                if len(misc) != 0:
                    choosen_item = questionary.select("Misc", choices=misc).unsafe_ask()
                else:
                    choosen_item = questionary.select(
                        "Du hast momentan kein Zeugs im Inventar.", choices=["zurück"]
                    ).unsafe_ask()
            case "Equipment":
                equip = []
                for item in Player.slots:
                    if item == "placeholder":
                        continue
                    try:
                        if item.name != "placeholder":
                            equip.append(item.name)
                    except:
                        pass
                if len(equip) != 0:
                    choosen_item = questionary.select(
                        "Deine verwendete Ausrüstung:", choices=equip
                    ).unsafe_ask()
                    if choosen_item != "zurück":
                        choosen_choice = questionary.select(
                            "Deine verwendete Ausrüstung:",
                            choices=["ablegen", "zurück"],
                        ).unsafe_ask()
                        match choosen_choice:
                            case "ablegen":
                                Player.unequip_item(choosen_item)
                            case "zurück":
                                pass
                            case _:
                                Logger.log(
                                    "Ein Unerlaubtes Menüitem wurde unter"
                                    ">>Inv>>Equip>> ausgewählt.",
                                    2,
                                )
                else:
                    choosen_item = questionary.select(
                        "Du hast gerade nichts Ausgerüstet.", choices=["zurück"]
                    ).unsafe_ask()
                    if choosen_item != "zurück":
                        Player.unequip_item(choosen_item)
            case "zurück zum Spiel":
                wants_exit = True
            case "zurück":
                pass
            case _:
                Logger.log(
                    "Ein Unerlaubtes Menüitem wurde unter >>Inv>> ausgewählt.", 2
                )

        if wants_exit:
            break
