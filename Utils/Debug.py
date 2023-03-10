from pystyle import Write, Colors, Colorate, Box, Center
from huepy import *

from Utils import pr




class Debug():

    """
    Utility class for custom debuging
    """

    def objlist(listOfObjects, definition="Objects"):
        """
            Returns List of Object Names from List of Objects
    
            :listOfObjects: List of Objects to be parsed
            :definition: Naming scheme in Output like (Loaded {definition}: {listOfObjectNames})
                
            =return= Returns DBG Print
        """ 
        _curObjects = []
        for _object in listOfObjects:
            _curObjects.append(_object.name)
        return pr.dbg(F"Loaded {definition}: {_curObjects}")
    
    def stop_game_on_exception(exception):
        pr.b((Colorate.Color(Colors.red, f"The following error occured:", True)))
        pr.b((Colorate.Color(Colors.red, f"{exception}", True)))
        pr.q("Do you want to continue the game?")
        action = pr.inp("y/n")
        match action:
            case "y":
                pass
            case "n":
                exit()

    def pause():
        programPause = input("Press the <ENTER> key to continue...")