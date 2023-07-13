"""Defines Input Method for User - exact copy of Inputparser-Module
"""
from os import listdir
from os import path
from pystyle import Colors, Write
from Utils.pr import Pr
from config import dbg, levels_folder
from Utils import Debug as Dbg


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
            "changegamestate: wechselt den Gamestate",
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

                    case "tp" | "teleport" | "changelevel" | "cl":
                        Dbg.show_wip()
                        llevel = Inp.assetlist("level")
                        print (llevel)
                        return 34

                    case "changegamestate":
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", [input_list[1]]]
                        )
                        return 34

                    case "changehealth" | "ch":
                        cvalue = int(input_list[1])
                        player.change_health(cvalue)    # pylint: disable=E1101
                        return 34

                    case "kill":
                        player.change_health(-player.hp)    # pylint: disable=E1101
                        return 34

                    case "god" | "tgm" | "gm1":
                        player.change_health(10000)    # pylint: disable=E1101
                        return 34

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
                        Dbg.show_wip()
                        return 34

                    case "inv":
                        # TODO: Pylint fix
                        Pr.dbg(f"{player}")
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", ["inv"]]
                        )
                        return 34

                    case "save":
                        Dbg.show_wip()
                        return 34

                    case "exit":
                        Pr.i("Bitte Kaufe das Exit DLC")
                        Dbg.show_wip()
                        return 34

                    case _:
                        return 34

            else:
                raise ValueError("Unsupported type of Input")
            return user_input

        except ValueError as e:
            Pr.a(f"Fehler bei Eingabe: {e}")
            return 1
        except Exception as e:
            Pr.a(f"Unbekannter Fehler beim Input: {e}")
            return 1
