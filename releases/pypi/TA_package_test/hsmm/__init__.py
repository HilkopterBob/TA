from .Utils import *
from .Entities import Entity, EntityInit, item, itemInit
from .Level import Level, LevelInit
from .Effect import Effect, EffectInit
import hunter
from .actionparser import Actionparser
import os

PATH = os.path.dirname(os.path.realpath(__file__))
items_file = str(PATH + r"/conf/items.json")
levels_file = str(PATH + r"/conf/levels.json")
effects_file = str(PATH + r"/conf/effects.json")
entity_file = str(PATH + r"/conf/entities.json")


def interact_with_level(player, level, level_list):
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    if level.name == "Menu":
        n("\n" * 5)
        headline(level.descr)
        n("\n" * 2)
    else:
        hud(player)
        n(level.descr)
    for llist in level.choices:
        if len(llist) == 1 and llist[0] != "":
            n(f"{i}. {llist[0]}")
            printed = True
            i = i + 1
        elif len(llist) > 1:
            for ddict in level.triggers:
                if llist[1] == ddict:
                    n(f"{i}. {llist[0]}")
                    printed = True
                    i = i + 1
    if printed == True:
        action = inp()

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### #####

    n(level.text[int(action) - 1][0])
    if len(level.text[int(action) - 1]) > 1:
        i = 1
        while i < len(level.text[int(action) - 1]):
            key = list(level.text[int(action) - 1][i].keys())

            if "action" not in str(key[0]):
                for ddict in level.triggers:
                    if ddict.keys() == level.text[int(action) - 1][1].keys():
                        try:
                            # Enumerate als refactor nutzen
                            triggered_dict = list(
                                filter(
                                    lambda dict: dict.keys()
                                    != level.text[int(action) - 1][1][key[0]],
                                    level.triggers,
                                )
                            )
                            triggered_dict_index = level.triggers.index(
                                triggered_dict[0]
                            )
                            level.triggers[triggered_dict_index] = level.text[
                                int(action) - 1
                            ][1]
                        except IndexError as e:
                            if dbg:
                                dbg(e)
                        if dbg:
                            dbg(level.text[int(action) - 1][1])
                            dbg(level.triggers)
            elif "action" in str(key[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                if dbg:
                    try:
                        dbg(key)
                        dbg(level.text[int(action) - 1][i][key[0]])
                        dbg(level.text[int(action) - 1][i][key[1]])
                    except Exception as e:
                        dbg(Exception)
                match level.text[int(action) - 1][i][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(
                            str(level.text[int(action) - 1][i][key[1]])
                        )
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(
                                level.text[int(action) - 1][i][key[1]]
                            ):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "dbg_true":
                        if dbg:
                            b(
                                dbg(
                                    "UNBEDINGT DEBUG DEAKTIVIEREN WENN AUF PROD GEPUSHT WIRD!!!"
                                )
                            )
                    case "add_effect":
                        effect = EffectInit.load_effect_by_name_from_json(
                            effects_file,
                            str(level.text[int(action) - 1][i]["effect_name"]),
                        )
                        player.add_effect(effect)
                    case _:
                        if dbg:
                            dbg(
                                f"{level.text[int(action) - 1][i][key[0]]} is not defined "
                            )
            i = i + 1


def hud(player):
    if player.location != "Menu" and player.location != "Options":
        n("+" * 12 + f" " + "+" * 12)
        n(f"Du befindest dich in: {player.location}")
        if player.hp > 25:
            g(f"HP: {player.hp}")
        else:
            b(f"HP: {player.hp}")
        n(f"Gold: {player.wealth}")
        n(f"Level: {player.level} XP: {player.xp}")


def gameloop(player, level_list=[]):

    lap = 0  # rundenanzahl
    # start of loop
    while True:
        # Loop through all Levels and check if Player is inside level   ---  TODO: FIX because unperformant
        for level in level_list:
            if level.name == player.location:
                current_level = level

        # Loop through all Entities in CurrentLevel and Apply Actionstack
        for e in current_level.entitylist:
            """
            Todo Action parser for actionstack (pass entity to which the action applies,
            pass the action, process action on entity, return successfull or error)
            """
            # Work through actionstack of Entity and process actions
            for action in e.actionstack:
                dbg(action)
                Actionparser.callfunction(action)
                e.actionstack.remove(action)

        player.check_level_up()  # check for levelups and level up if enough xp
        interact_with_level(player, current_level, level_list)
        # changes the entity location, deletes entity from old level and adds to the new one

        # Increase Lap Counter by i
        lap = lap + 1

        # Wait for Player Input
        pause()


def start_game():
    mPlayer = Entity(
        "Player",
        100,
        100,
        0,
        [item("Item1", "weapon"), item("item2", "misc")],
        location="Menu",
    )
    hurensohn = Entity(
        "Hurensohn",
        100,
        100,
        0,
        [item("Item1", "weapon"), item("item2", "misc")],
        location="Wiese",
    )
    # mPlayer.set_name()
    kopfschmerz = Effect("Kopfschmerz", "Kopfschmerzen halt.", "bad", -1, "hp")
    heilung = Effect("heilung", "Nö", "good", 5, "hp")
    heilung2 = Effect("heilung2", "Nö", "good", 5, "hp")
    heilung3 = Effect("heilung 3", "Nö", "good", 5, "hp")
    terror = Effect("Terror", "Nö", "evil", -100, "xp")

    # Load all existing Levels
    print(levels_file)
    allLevels = LevelInit.load_all_levels_from_json(levels_file)
    objlist(allLevels, "Levels")

    # Load all existing Entities
    allEntities = EntityInit.load_entities_fromjson(entity_file)
    objlist(allEntities, "Entities")

    ###########################################
    #######___HOW TO USE ACTIONSTACK___########
    ###########################################
    ####Add actions to Player Actionstack
    # mPlayer.actionstack.put("Some Action from Actionstack")
    # mPlayer.actionstack.put("Another Action from Actionstack")
    # mPlayer.actionstack.put("And Another Action from Actionstack")
    # mPlayer.actionstack.put("let_effects_take_effect")

    # put Kopfschmerz Effect in Actionstack
    mPlayer.actionstack.append(["applyeffect", [mPlayer, "Kopfschmerz"]])
    mPlayer.actionstack.append(["takeeffects", [mPlayer, True]])

    gameloop(mPlayer, allLevels)
