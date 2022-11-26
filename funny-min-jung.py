#ToDo's:
#Spielerklasse
#Levelklasse
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from Entities import Entity, item, itemInit
from Level import Level
from Effect import Effect
import Utils as pr 
import json

##################
##Debug Variable##
dbg = True
##################

###################
###ENV Variables###
items_file = "config/items.json"
###################


lvl = 0
action = ""




#lvl1 vars:
lvl1_umgesehen = False
#vereinfachte Printanweisung mit Write und Color


# while True:
#     while lvl == 0:
#         Write.Print(Box.Lines("Nicks Textadventure!"), Colors.dark_red, interval=0.02)
#         choices = "1. Spiel starten\n2. Spielstand laden\n3.Spiel beenden\n4.debug mode"
#         action = Write.Input(Center.XCenter(choices + "\n→ "), Colors.red_to_purple, interval=0.0025)
#         if action == "1":
#             lvl = 1
#             print("\n\n\n\n\n")
#         if action =="2":        
#             pass

#     while lvl == 1:
#         Write.Print("\n" + "#"*50 + "\n\n", Colors.red_to_purple, interval=0.0025)
#         if lvl1_umgesehen == False:
#             Write.Print("Du wachst auf.\nDein Schädel brummt.\nDu öffnest deine Augen und schaust dich um.\nGeblendet von der Sonne erkennst du, dass du auf einer Wiese bist.\n", Colors.red_to_purple, interval=0.0025)
#             choices = "\n1. Umsehen\n2. Etwas gegen deine Kopfschmerzen machen\n"
#             action = Write.Input(choices + "\n→ ", Colors.red_to_purple, interval=0.0025)
#         if lvl1_umgesehen == True:
#             Write.Print("Du wachst auf.\nDein Schädel brummt.\nDu öffnest deine Augen und schaust dich um.\nGeblendet von der Sonne erkennst du, dass du auf einer Wiese bist.\nDu siehst einen Weg.\nIn der Ferne siehst du die Umrisse einer Stadt.\n", Colors.red_to_purple, interval=0.0025)
#             choices = "1. Umsehen\n2. Etwas gegen deine Kopfschmerzen machen\n3. Den Weg entlanggehen\n"
#             action = Write.Input(choices + "\n→ ", Colors.red_to_purple, interval=0.0025)

#         if action == "1":
#             pr("Du siehst dich um.\nDu siehst einen Weg.\nIn der Ferne siehst du die Umrisse einer Stadt.\n")
#             lvl1_umgesehen = True
#             sleep(2)
#         if action == "2":
#             pr("Du schüttelst deinen Kopf, die Kopfschmerzen verschwinden.")
#             Write.Print("[Statuseffekt] (Kopfschmerz) verschwindet!" + "\n", Colors.red, interval=0.0025)
#             sleep(2)
#         if action == "3" and lvl1_umgesehen == True:
#             pr("Du stehst auf und gehst zu dem Weg.\nDer Weg ist ein schmutziger, kleiner Trampelpfad.\n")



if __name__ == "__main__":
    mPlayer = Entity("Blankoname", 100,100,0,[item("Item1","weapon"),item("item2","misc")])
    #mPlayer.set_name()
    vergiftung = Effect("Vergiftung","Nö","bad", -2, "hp")
    print(vars(vergiftung))
    mPlayer.add_effect(vergiftung)
    mPlayer.show_effects()
    allItems = itemInit.load_all_items_from_json(items_file)
    print(vars(itemInit.load_item_by_name_from_json(items_file, "Sword")))
    print()
    menu = Level(["Textadventure","Hauptmenü","spiel wird geladen"],["Spiel laden","Spiel starten","Spiel beenden"],"Hauptmenü",[],"zivilisiert","Mainmanu descr")
    def gameloop(player, level):

        print("*"*10 + "player" + "*"*10 + "\n")
        print(vars(player))
        print("*"*10 + "level" + "*"*10 + "\n")
        print(vars(level))
        print("*"*26 + "\n")
        pr.n()

    gameloop(mPlayer, menu)

