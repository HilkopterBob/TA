"""Debug Module
"""

import sys
from pystyle import Colors, Colorate
from Utils import Pr, Inp


class Debug:
    """
    Utility class for custom debuging
    """

    def objlist(
        listOfObjects: list[object] = None, definition: str = "Objects"
    ) -> None:
        """
        Returns List of Object Names from List of Objects

        :listOfObjects: List of Objects to be parsed
        :definition: Naming scheme in Output like (Loaded {definition}: {listOfObjectNames})

        =return= Returns DBG Print
        """
        from Utils.logger import Logger  # pylint: disable=C0415

        return Logger.log(f"Loaded {definition}: {Debug.getNames(listOfObjects)}", -1)

    def getNames(listOfObjects: list[object] = None) -> list[str]:
        """Returns a List of Objectnames from list of Objects

        Args:
            listOfObjects (List, optional): List of Objects. Defaults to None.
        """
        if listOfObjects is None:
            listOfObjects = []

        _curObjects = []

        for _object in listOfObjects:
            _curObjects.append(_object.name)
        return _curObjects

    def stop_game() -> None:
        """Pauses the Game and Asks for Continue or Stop"""
        Pr.q("Do you want to continue the game?")
        action = Inp.inp("y/n")
        match action:
            case "y":
                pass
            case "n":
                sys.exit()

    def stop_game_on_exception(exception: str) -> None:
        """Halts the Game on Exception"""
        Pr.b((Colorate.Color(Colors.red, "\nThe following error occured:", True)))
        Pr.b((Colorate.Color(Colors.red, f"{exception}", True)))
        Pr.q(
            "Do you want to continue the game? No technical \
            support from this point onward, if you don't restart!"
        )
        action = Inp.inp(text="y/n", yes_no_flag=True)
        match action:
            case "y":
                pass
            case "n":
                sys.exit()

    def pause() -> None:
        """Pauses the Game for User Input"""
        input("Press the <ENTER> key to continue...")
