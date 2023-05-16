"""Debug Module
"""
import sys
from pystyle import Colors, Colorate
from Utils import Pr, Inp


class Debug():

    """
    Utility class for custom debuging
    """

    def objlist(listOfObjects=None, definition="Objects"):
        """
            Returns List of Object Names from List of Objects
    
            :listOfObjects: List of Objects to be parsed
            :definition: Naming scheme in Output like (Loaded {definition}: {listOfObjectNames})
                
            =return= Returns DBG Print
        """
        if listOfObjects is None:
            listOfObjects = []

        _curObjects = []
        for _object in listOfObjects:
            _curObjects.append(_object.name)
        return Pr.dbg(F"Loaded {definition}: {_curObjects}")

    def stop_game_on_exception(exception):
        """Halts the Game on Exception
        """
        Pr.b((Colorate.Color(Colors.red, "The following error occured:", True)))
        Pr.b((Colorate.Color(Colors.red, f"{exception}", True)))
        Pr.q("Do you want to continue the game?")
        action = Inp.inp("y/n")
        match action:
            case "y":
                pass
            case "n":
                sys.exit()

    def pause():
        """Pauses the Game for User Input
        """
        input("Press the <ENTER> key to continue...")
