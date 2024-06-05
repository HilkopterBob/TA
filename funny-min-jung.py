"""Main Module for Textadventure
"""

# project imports:
from __future__ import annotations
from pympler.asizeof import asizeof as getsize
from Entities import Entity
from Level import Level
from Effect import Effect
from Items import gitem
from Utils import Pr, Logger
from Utils.gamestates.inventorystate import inventorystate
from Utils.gamestates.combatstate import combatstate
from Utils.gamestates.mainstate import interact_with_level
from actionparser import Actionparser
from Assethandler import AssetHandler, load_game
from errorhandler import error


@error
def gameloop(player: Entity, level_list: list[Level] = None) -> None:
    """
    The Main Game Loop
    """
    current_level = Level
    if level_list is None:
        level_list = []

    lap = 0

    # Entering Gameloop
    while True:
        for level in level_list:
            if str(level.name) == str(player.location):
                Logger.log(
                    f"Player location ({player.location}) "
                    f"is equal to Level ({level.name}), "
                )
                if not player in level.entitylist:
                    Logger.log(
                        f"{player.name} not in {level.name} "
                        f"- adding {player.name} to {level.name} entitylist",
                        1,
                    )
                    level.change_entity_list("+", player)
                Logger.log(f"Setting CurrentLevel to Level: {level}")
                current_level = level

        # Loop through all Entities in CurrentLevel and Apply Actionstack
        if Actionparser.gamestate == "game":
            for e in current_level.entitylist:
                for action in e.actionstack:
                    Logger.log(action)
                    Actionparser.callfunction(action)
                    e.actionstack.remove(action)

        match Actionparser.gamestate:
            case "loading":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                # loding steps
                Actionparser.gamestate = "game"
            case "game":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")

                # Hier muss die interact_with_level() func ausgelagert werden.

                interact_with_level(player, current_level, level_list)
                Actionparser.gamestate = Actionparser.gamestate
            case "inv":
                if Actionparser.gamestate == "game" or player.location.name == "Menu":
                    Logger.log('Gamestate "inv" not available from here!', 1)
                    Pr.yellow('Gamestate "inv" kann hier nicht geöffnet werden!')
                    Actionparser.gamestate = "game"
                else:
                    Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                    inventorystate(player)
                    Actionparser.gamestate = "game"
            case "combat":
                Logger.log(f"Gamestate is now {Actionparser.gamestate}")
                Logger.log(f"{player} Entering Combatstate")
                combatstate(player, player.location.entitylist)  # pylint: disable=E0601
                Actionparser.gamestate = "game"
            case _:
                Pr.yellow(
                    f'Der Gamestate "{Actionparser.gamestate}" ist nicht bekannt.'
                )
                Logger.log(f"Gamestate {Actionparser.gamestate} unknown", 1)
                Actionparser.gamestate = "game"

        player.check_level_up()

        # changes the entity location, deletes entity from old level and adds to the new one

        # Increase Lap Counter by i
        lap = lap + 1

        # Loop through all Entities in CurrentLevel and Apply Actionstack
        Logger.log(f"Entitylist: {[str(x) for x in current_level.entitylist]}", -1)
        for e in current_level.entitylist:
            Logger.log(f"Working Actionstack for {e}", 1)
            Logger.log(f"Actionstack: {e.actionstack}")
            # Work through actionstack of Entity and process actions
            for i in range(0, len(e.actionstack)):
                Logger.log("#" * 50, -1)
                Logger.log(f"Length of Actionstack: {len(e.actionstack)}", -1)
                Logger.log(f"Current Actionstack: {e.actionstack}", -1)
                Logger.log(f"Current Index: {i}", -1)
                cur_action = e.actionstack.pop(0)
                Actionparser.callfunction(cur_action)
                Logger.log(f"Cur_Action: {cur_action}", -1)
                Logger.log(
                    f"Length of Actionstack after Action: {len(e.actionstack)}", -1
                )
                Logger.log(f"Current Actionstack after Action: {e.actionstack}", -1)
                Logger.log("#" * 50, -1)


if __name__ == "__main__":

    # Test loadgame Function
    load_game()

    # Checking Game File Integrity
    # AssetHandler.CheckGameIntegrity()

    # Importing Level Assets
    # AssetHandler.importLevels()
    allLevels = AssetHandler.allLevels

    # Importing Entity Assets
    # AssetHandler.importEntities()
    allEntities = AssetHandler.allEntities

    # importing Item Assets
    # AssetHandler.importItems()
    allItems = AssetHandler.allItems

    # Importing Effect Assets
    # AssetHandler.importEffects()
    allEffect = AssetHandler.allEffects

    # Creating seperate Player Entitiies
    mPlayer = Entity(
        "Player",
        100,
        100,
        0,
        allItems,
        location=allLevels[-2],
        attributes={"str": 8, "dex": 8, "int": 8, "ini": 80, "chr": 8},
        isPlayer=True,
    )
    # Creating seperate Effects
    kopfschmerz = Effect("Kopfschmerz", "Kopfschmerzen halt.", "bad", -1, "hp")
    heilung = Effect("heilung", "Nö", "good", 5, "hp")
    heilung2 = Effect("heilung2", "Nö", "good", 5, "hp")
    heilung3 = Effect("heilung 3", "Nö", "good", 5, "hp")
    terror = Effect("Terror", "Nö", "evil", -100, "xp")

    # put Kopfschmerz Effect in Actionstack
    mPlayer.actionstack.append(["add_effect", [mPlayer, "Kopfschmerz"]])
    mPlayer.actionstack.append(["take_effects", [mPlayer, True]])
    mPlayer.actionstack.insert(0, ["change_gamestate", ["game"]])

    # List all Loaded Levels and Entities
    # Debug.objlist(allLevels, "Levels")
    # Debug.objlist(allEntities, "Entities")
    # Debug.objlist(allItems, "Items")

    Logger.log(f"Speicherbedarf Levels: {getsize(Level())} B", 3)
    Logger.log(f"Speicherbedarf Items: {getsize(gitem())} B", 3)
    Logger.log(f"Speicherbedarf Entities: {getsize(Entity())} B", 3)
    Logger.log(f"Speicherbedarf Effects: {getsize(Effect())} B", 3)

    # Fill Player iventory with Placeholder Items
    while len(mPlayer.slots) < 11:
        mPlayer.slots.append("placeholder")

    # Run Game
    gameloop(mPlayer, allLevels)
