"""Defines Input Method for User - exact copy of Inputparser-Module
"""
from os import listdir
from os import path
from pystyle import Colors, Write
from Utils.pr import Pr
from config import dbg, levels_folder


#from Assethandler import AssetHandler




class Inp:
    """
    Utility Class for getting custom input prompts
    """

    def assetlist(asset=None):
        """
        listing all assets of one type
        """
        match asset:
            case "level":
                fileList = listdir(levels_folder)
                levelList=[
                    path.splitext(file)[0]
                    for file in fileList
                    if file.lower().endswith(".json")
                    ]

                return levelList

    def inp(
        player="", text="", yes_no_flag=False
    ):  # pylint: disable=too-many-return-statements
        """Method to get User Input"""
        befehlszeichen = "#"
        userbefehl = [
            " inv: Öffnet das Inventar",
            " opt: Öffnet die Optioen",
            " men: Öffnet das Menü",
            "save: Speichert das Spiel",
            "exit: Schließt das Spiel",
        ]
        devbefehl = [
           "give: gibt ein Item",
           "changegamestate: wechselt den Gamestate",
           "effect: gibt einen Effect",
           "changehealth: ändert die Lebenzzahl des Spielers [+/-]",
           "kill: setzt die Lebenszahl des Spielers auf 0",
            "",
            "",
            "",
            "",
        ]

        min_len = 0
        max_len = 150
        user_input = Write.Input(text + "\n >_ ", Colors.white, interval=0.0025)

        try:
            if not user_input.strip():
                raise ValueError("Leere Eingabe")

            if len(user_input) < min_len:
                raise ValueError(
                    f"Der Input muss mindestens {min_len} Zeichen lang sein"
                )

            if len(user_input.strip()) > max_len:
                raise ValueError(
                    f"Der Input darf nicht länger als {max_len} Zeichen sein"
                )

            # alles kleinbuchstaben
            user_input = user_input.lower()
            # Wenn Eingabe == Zahl dann

            if yes_no_flag and user_input in ["y", "n", "Y", "N", "j", "J"]:
                pass
                # Pr.dbg(user_input, 0)

            elif user_input.isdigit():
                user_input = int(user_input)

            elif user_input[0] == befehlszeichen:
                # befehlserkennung
                input_command = user_input[1:]
                input_list = input_command.split()
                match input_list[0]:

                    #dev Befehle

#für give tp und effect wird liste an allen benötigt (assethandler circle imports)

                    #case "give" | "item":
                    #    Pr.i("Die Funktion ist noch nicht implementiert")
                    #    pass

                    case "tp" | "teleport" | "changelevel" | "cl":
                        llevel = Inp.assetlist("level")
                        print (llevel)

                        #Pr.dbg(f"{input_list[1]} - {gameloop.allLevels}",2)
                        #if [input_list[1]] in gameloop.allLevels :
                        #    player.change_location(player.location, [input_list[1]])
                        #else :
                        #    raise ValueError(f"{[input_list[1]]} ist kein gültiges Level")
                        return 34

                    case "changegamestate":
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", [input_list[1]]]
                        )
                        return 34

                    #case "effect":
                    #    player.add_effect([input_list[1]])
                    #    pass

                    case "changehealth" | "ch":
                        cvalue = int(input_list[1])
                        player.change_health (cvalue)    # pylint: disable=E1101

                    case "kill":
                        player.change_health (-player.hp)    # pylint: disable=E1101

                    case "god" | "tgm" | "gm1":
                        player.change_health (10000)    # pylint: disable=E1101

                    # User Befehle

                    case "help":
                        Pr.headline("userbefehle")
                        for einzelwert in userbefehl:
                            Pr.i(einzelwert)
                        if dbg:
                            Pr.n("")
                            Pr.headline("devbefehle")
                            for einzelwert in devbefehl:
                                Pr.i(einzelwert)
                        return 34

                    case "opt":
                        Pr.i("Die Funktion ist noch nicht implementiert")
                        return 34

                    case "inv":
                        # TODO: Pylint fix
                        Pr.dbg(f"{player}")
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", ["inv"]]
                        )
                        return 34

                    case "save":
                        Pr.i("Die Funktion ist noch nicht implementiert")
                        return 34

                    case "exit":
                        Pr.i("Bitte Kaufe das Exit DLC")
                        return 34

                    case _:
                        return 34

                return Inp.inp(player)
            else:
                raise ValueError("Unsupported type of Input")
            return user_input

        except ValueError as e:
            Pr.a(f"Fehler bei Eingabe: {e}")
            return 1
        except Exception as e:
            Pr.a(f"Unbekannter Fehler beim Input: {e}")
            return 1
