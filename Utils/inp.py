"""Defines Input Method for User - exact copy of Inputparser-Module
"""
from pystyle import Colors, Write
from Utils.pr import Pr
from config import dbg


class Inp:
    """
    Utility Class for getting custom input prompts
    """

    def inp(player, text=""):  # pylint: disable=too-many-return-statements
        """Method to get User Input"""
        Pr.dbg(f"{player}")
        befehlszeichen = "#"
        userbefehl = [
            " inv: Öffnet das Inventar",
            " opt: Öffnet die Optioen",
            " men: Öffnet das Menü",
            "save: Speichert das Spiel",
            "exit: Schließt das Spiel",
        ]
        devbefehl = [
            "test: test",
            "",
            "",
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
            if user_input.isdigit():
                user_input = int(user_input)

            # Wenn Eingabe == String dann
            elif user_input[0] == befehlszeichen:
                # befehlserkennung
                input_command = user_input[1:]
                input_list = input_command.split()
                match input_list[0]:
                    # dev Befehle
                    case "hallo":
                        print("Hallo")
                        for e in input_list:
                            print(e)

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
                        return 34

                    case "inv":
                        # TODO: Pylint fix
                        Pr.dbg(f"{player}")
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", ["inv"]]
                        )
                        return 34
                    case "changegamestate":
                        player.actionstack.insert(  # pylint: disable=E1101
                            0, ["change_gamestate", [input_list[1]]]
                        )
                        return 34
                    case "save":
                        Pr.i("Die Funktion ist noch nicht implementiert")
                        return 34
                    case "exit":
                        return 34

                    case _:
                        return 34

                return Inp.inp(player)
            return user_input

        except ValueError as e:
            Pr.a(f"Fehler bei Eingabe: {e}")
            return 1
        except Exception as e:
            Pr.a(f"Unbekannter Fehler beim Input: {e}")
            return 1
