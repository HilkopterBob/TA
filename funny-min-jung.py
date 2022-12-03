from Entities import Entity, item, itemInit
from Level import Level
from Effect import Effect
import Utils as pr 
import json


##################
##Debug Variable##
global dbg
dbg = True
##################

###################
###ENV Variables###
items_file = "config/items.json"
###################


def interact_with_level(player, level, level_list):
    ##### ##### prints out choices and gets user input if choices got printed ##### #####
    if level.name == "Menu":
        printed = False
        i = 1
        pr.headline(level.descr)
        for llist in level.choices:
            if len(llist) == 1:
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
    else:
        printed = False
        i = 1
        pr.n(level.descr)
        for llist in level.choices:
            if len(llist) == 1:
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
            key = list(level.text[int(action) - 1][1].keys())

            if "action" not in str(key[0]):
                ##### ##### reads and changes triggers ##### #####
                for ddict in level.triggers:
                    if ddict.keys() == level.text[int(action) - 1][1].keys():
                        try:
                            triggered_dict = list(filter(lambda dict: dict[key[0]] != level.text[int(action) - 1][1][key[0]], level.triggers))
                            triggered_dict_index = level.triggers.index(triggered_dict[0])
                            level.triggers[triggered_dict_index] = level.text[int(action) - 1][1]
                        except IndexError as e:
                            if dbg:
                                pr.dbg(e)
                        if dbg:
                            pr.dbg(level.text[int(action) - 1][1])
                            pr.dbg(level.triggers)
                        #FUNKTIONIERT!!! refactor incoming...
            elif "action" in str(key[0]):
                ##### ##### reads and uses action calls (action parser)##### #####
                if dbg:
                    pr.dbg(key)
                    pr.dbg(level.text[int(action) - 1][1][key[0]])
                    pr.dbg(level.text[int(action) - 1][1][key[1]])
                match level.text[int(action) - 1][1][key[0]]:
                    case "remove_effect_by_name":
                        player.remove_effect_by_name(str(level.text[int(action) - 1][1][key[1]]))
                    case "change_location":
                        for llevel in level_list:
                            if llevel.name == str(level.text[int(action) - 1][1][key[1]]):
                                new_level = llevel
                                player.change_location(level, new_level)
                    case _:
                        if dbg:
                            pr.dbg("level.text[int(action) - 1][1][key[0]] is not defined in: [ACTIONPARSER]")
                    
        # except:
        #     pr.b("Deine Eingabe war falsch.")



def hud(player):
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

        hud(player)                                         #basic hud
        player.let_effects_take_effect(dbg)                 #effects 
        player.check_level_up()                             #check for levelups and level up if enough xp
        interact_with_level(player, current_level, level_list)
        #changes the entity location, deletes entity from old level and adds to the new one
        


        lap = lap + 1
        pr.pause()







if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,[item("Item1","weapon"),item("item2","misc")], location="Menu")
    h = Entity()
    #mPlayer.set_name()
    kopfschmerz = Effect("Kopfschmerz","Kopfschmerzen halt.","bad", -1, "hp")
    heilung = Effect("heilung","Nö","good", 5, "hp")
    heilung2 = Effect("heilung2","Nö","good", 5, "hp")
    heilung3 = Effect("heilung 3","Nö","good", 5, "hp")
    terror = Effect("Terror","Nö","evil", -100, "xp")
    #print(vars(vergiftung))
    mPlayer.add_effect(kopfschmerz)
    # mPlayer.add_effect(heilung)
    # mPlayer.add_effect(heilung2)
    # mPlayer.add_effect(heilung3)
    #mPlayer.add_effect(terror)
    # mPlayer.show_effects()
    #print(mPlayer.effects)
    #allItems = itemInit.load_all_items_from_json(items_file)
    #print(vars(itemInit.load_item_by_name_from_json(items_file, "Sword")))
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
    menu = Level(
        [
            [""],
            [""],
            [""],
            [""],
            ["",{"action":"dbg_true"}]
        ],
        [
            ["Spiel starten"],
            ["Spiel laden"],
            ["Optionen"],
            ["Beenden"],
            [""]                #dev mode (sets dbg true)
        ],
        "Menu",
        [],
        "neutral",

    )
    wiese = Level(
        [
            ["Du schüttelst deinen Kopf. Die kopfschmerzen verschwinden.",  {"action":"remove_effect_by_name",
                                                                            "effect.name":"Kopfschmerz"}],
            [ "Du siehst dich um. Etwas entfernt scheint ein Weg zu sein.", {"umgesehen":True}],
            ["Du gehst den Weg entlang.",  {"action":"change_location",
                                            "new_level_name":"Kreuzung"}]
        ],
        [
            ["etwas gegen deine Kopfschmerzen machen"],
            ["dich umsehen"],
            ["den Weg entlang gehen",{"umgesehen":True}]
        ],
        "Wiese",
        descr="Du wachst auf einer Wiese auf. Du hst kopfschmerzen. \nIn der Ferne siehst du die Umrisse einer Stadt.",
        entitylist=[],
        triggers=[{"umgesehen":False}]
    )
    kreuzung = Level(
        [
            ["Du gehst in die Stadt.", {"action":"change_location",
                                        "new_level_name":"Stadt"}],
            ["Du gehst in den Wald.",  {"action":"change_location",
                                        "new_level_name":"Wald"}],
            ["Du gehst in die Miene.", {"action":"change_location",
                                        "new_level_name":"Miene"}],
            ["Du gehst zur Wiese", {"action":"change_location", 
                                    "new_level_name":"Wiese"}]
        ],
        [
            ["In die Stadt gehen"],
            ["In den Wald gehen"],
            ["In die Miene gehen"],
            ["Zur Wiese gehen"]
        ],
        name="Kreuzung",
        ltype="friedlich",
        descr="Du folgst dem Weg bis zu einer Kreuzung.",
        entitylist=[],
        triggers=[]
    )
    ####Run Gameloop with nirvana as Level
    gameloop(mPlayer, [ wiese, kreuzung, menu])
    
    