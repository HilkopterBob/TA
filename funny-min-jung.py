from Entities import Entity, item, itemInit
from Level import Level, LevelInit
from Effect import Effect, EffectInit
import Utils as pr 
import json
import hunter 
import sys



##################
##Debug Variable##
global dbg
dbg = True
sys.stdout.reconfigure(encoding='utf-8')
#hunter.trace(module="__main__")
##################

###################
###ENV Variables###
items_file = r"C:\Users\npodewils\Desktop\p\Python\TA\config\items.json"
levels_file = r"C:\Users\npodewils\Desktop\p\Python\TA\config\levels.json"
effects_file = r"C:\Users\npodewils\Desktop\p\Python\TA\config\effects.json"
###################


def interact_with_level(player, level, level_list):
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    printed = False
    i = 1
    if level.name == "Menu":
        pr.n("\n"*5)
        pr.headline(level.descr)
        pr.n("\n"*2)
    else:
        hud(player)                                         #basic hud
        pr.n(level.descr)
    for llist in level.choices:
        if len(llist) == 1 and llist[0] != "":
            pr.n(f"{i}. {llist[0]}")
            printed = True
            i = i + 1
        elif len(llist) > 1:
            for ddict in level.triggers:
                if llist[1] == ddict:
                    pr.n(f"{i}. {llist[0]}")
                    printed = True
                    i = i + 1
    if printed == True:
        action = pr.inp()

    ##### ##### Reads triggers and action calls in level.text[dicts] ##### ##### 
    #try:

    pr.n(level.text[int(action) - 1][0])
    if len(level.text[int(action) - 1]) > 1:
        i = 1
        while i < len(level.text[int(action) - 1]):
            key = list(level.text[int(action) - 1][i].keys())
            # if "action" not in str(key[0]):
            #     ##### ##### reads and changes triggers ##### #####
            #     for ddict in level.triggers:
            #         if ddict.keys() == level.text[int(action) - 1][i].keys():
            #             pr.b(ddict)
            #             pr.b(level.text[int(action) - 1][i])
            #             pr.b(i)
            #             pr.b(key[0])
            #             pr.b(level.text[int(action) - 1][i][str(key[0])])
            #             pr.b("Kopfschmerzen" == key[0])
            #             try:
            #                 triggered_dict = list(filter(lambda dict: dict[key[0]] != level.text[int(action) - 1][i][key[0]], level.triggers))
            #                 triggered_dict_index = level.triggers.index(triggered_dict[i - 2])
            #                 level.triggers[triggered_dict_index] = level.text[int(action) - 1][i]
                            
            #             except KeyError as e:
            #                 if dbg:
            #                     pr.dbg(e)
            #                 continue
            #             if dbg:
            #                 pr.dbg(level.text[int(action) - 1][i])
            #                 pr.dbg(level.triggers)
            if "action" not in str(key[0]):
                """
                    alte Version des actionparsers, ca. 5 commits alt
                """
                for ddict in level.triggers:
                    if ddict.keys() == level.text[int(action) - 1][1].keys():
                        try:
                            #Enumerate als refactor nutzen
                            triggered_dict = list(filter(lambda dict: dict.keys() != level.text[int(action) - 1][1][key[0]], level.triggers))
                            triggered_dict_index = level.triggers.index(triggered_dict[0])
                            level.triggers[triggered_dict_index] = level.text[int(action) - 1][1]
                        except IndexError as e:
                            if dbg:
                                pr.dbg(e)
                        if dbg:
                            pr.dbg(level.text[int(action) - 1][1])
                            pr.dbg(level.triggers)
                        #FUNKTIONIERT!!! refactor incoming...
                        #FUNKTIONIERT NICHT!!! refactor incoming...
                        #Das Trigger:Value dict wird nicht gespeichert bug!!!
                        #
                        #
            elif "action" in str(key[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                if dbg:
                    try:
                        pr.dbg(key)
                        pr.dbg(level.text[int(action) - 1][i][key[0]])
                        pr.dbg(level.text[int(action) - 1][i][key[1]])
                    except Exception as e:
                        pr.dbg(Exception)
                match level.text[int(action) - 1][i][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(str(level.text[int(action) - 1][i][key[1]]))
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(level.text[int(action) - 1][i][key[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case "dbg_true":
                        if dbg:
                            pr.b(pr.dbg("UNBEDINGT DEBUG DEAKTIVIEREN WENN AUF PROD GEPUSHT WIRD!!!"))
                    case "add_effect":
                        effect = EffectInit.load_effect_by_name_from_json(effects_file, str(level.text[int(action) - 1][i]["effect_name"]))
                        player.add_effect(effect)
                    case _:
                        if dbg:
                            pr.dbg(f"{level.text[int(action) - 1][i][key[0]]} is not defined : [ACTIONPARSER]")
            i = i + 1
                    
    # except:
    #     pr.b("Deine Eingabe war falsch.")


def hud(player):
    if player.location != "Menu" and player.location != "Options":
        pr.n("+"*12+f" "+"+"*12)
        pr.n(f"Du befindest dich in: {player.location}")
        if player.hp > 25:
            pr.g(f"HP: {player.hp}")
        else:
            pr.b(f"HP: {player.hp}")
        pr.n(f"Gold: {player.wealth}")
        pr.n(F"Level: {player.level} XP: {player.xp}")




def gameloop(player, level_list=[]):
        
    lap = 0                                             #rundenanzahl
    while True:
        for level in level_list:
            if level.name == player.location:
                current_level = level
        for e in current_level.entitylist:
            for a in list(e.actionstack.queue):
                pr.dbg(a)
        ###Todo Action parser for actionstack (pass entity to which the action applies, pass the action, process action on entity, return successfull or error)
        ##############################################


        player.let_effects_take_effect(dbg)                 #effects 
        player.check_level_up()                             #check for levelups and level up if enough xp
        interact_with_level(player, current_level, level_list)
        #changes the entity location, deletes entity from old level and adds to the new one
        


        lap = lap + 1
        pr.pause()






if True:
#if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,[item("Item1","weapon"),item("item2","misc")], location="Menu")
    h = Entity()
    #mPlayer.set_name()
    kopfschmerz = Effect("Kopfschmerz","Kopfschmerzen halt.","bad", -1, "hp")
    heilung = Effect("heilung","Nö","good", 5, "hp")
    heilung2 = Effect("heilung2","Nö","good", 5, "hp")
    heilung3 = Effect("heilung 3","Nö","good", 5, "hp")
    terror = Effect("Terror","Nö","evil", -100, "xp")
    #print(vars(vergiftung))
    #mPlayer.add_effect(kopfschmerz)
    # mPlayer.add_effect(heilung)
    # mPlayer.add_effect(heilung2)
    # mPlayer.add_effect(heilung3)
    #mPlayer.add_effect(terror)
    # mPlayer.show_effects()
    #print(mPlayer.effects)
    #allItems = itemInit.load_all_items_from_json(items_file)
    wieseLevel = LevelInit.load_level_by_name_from_json(levels_file, "Wiese")
    kreuzungLevel = LevelInit.load_level_by_name_from_json(levels_file, "Kreuzung")
    menuLevel = LevelInit.load_level_by_name_from_json(levels_file, "Menu")
    





    
    #allLevels = LevelInit.load_all_levels_from_json(levels_file)
    #print(vars(itemInit.load_item_by_name_from_json(items_file, "Bat")))
    #print()
    #menu = Level(["Textadventure","Hauptmenü","spiel wird geladen"],["Spiel laden","Spiel starten","Spiel beenden"],"Hauptmenü",[],"zivilisiert","Mainmanu descr")
    #gameloop(mPlayer, menu)
    
    
    ####Add actions to Player Actionstack
    # mPlayer.actionstack.put("Some Action from Actionstack")
    # mPlayer.actionstack.put("Another Action from Actionstack")
    # mPlayer.actionstack.put("And Another Action from Actionstack")
    # mPlayer.actionstack.put("let_effects_take_effect")
    
    ####Create a New Level with Player as only Entity in Level
    #nirvana = Level(["Du siehst einen Weg.",], ["Atmen", "Den Wen entlanggehen"],"Nirvana", [], "Testtype", "nirvana",[])                  #hier chillen entitys die existieren ohne in einem level eingesetzt zu werden
    #nowhere = Level([""], [],"nowhere", [], "Testtype", "nowhere",[])                         #Hommage für alte Textadventures
    #newnewLevel = Level(["Du siehst einen Weg, der ins Nirvana führt."], ["Nachdenken","Ins Nirvana gehen"],"NewNewLevel", [], "Testtype", "NewNewLevel",[])

    ####Run Gameloop with nirvana as Level
    gameloop(mPlayer, [wieseLevel, kreuzungLevel, menuLevel])
    
