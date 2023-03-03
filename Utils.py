from pystyle import Write, Colors, Colorate, Box, Center
from huepy import *
import inspect

def n(text=""):
    Write.Print(text + "\n", Colors.white, interval=0.0025)

def a(text=""):
    Write.Print(text + "\n", Colors.red, interval=0.0025)
    
def inp(text=""):
    Input = Write.Input(text + "\n → ", Colors.white, interval=0.0025)
    return Input

def b(text=""):
    print(bad(text))

def i(text=""):
    print(info(text))

def g(text=""):
    print(good(text))

def q(text=""):
    print(que(text))

def dbg(text="", errlvl=0):
    """
        Prints Debug Information into Console
    Args:
        text (str): Text to be Displayed. Defaults to "".
        errlvl (int): Errorlevel 0=Inf, 1=Err. Defaults to 0.
    """
    
    module = inspect.currentframe().f_back.f_globals['__name__']
    function = inspect.stack()[1].function
    
    if errlvl == 0:
        print(f'{info("")} {good("")} {str(yellow(f"DBG - {module} - {function}: "))} {str(text)}')
    else:
        print(f'{info("")} {bad("")} {str(yellow(f"DBG - {module} - {function}: "))} {str(text)}')

def showcase():
    n("Das ist die standard Printanweisung")
    a("Allerts!")
    print(inp("Inputs! >_"))
    b("Bad shit")
    i("Information")
    g("Good")
    q("Quest(ion)")
    dbg("InfoLevel Debug")
    dbg("ErrorLevel Debug", 1)
    green("Green Text")
    yellow("Yellow Text")
    red("Red Text")
    blue("Blue Text")
    cyan("Cyan Text")



###Action Definitions
def stop_game_on_exception(exception):
    b((Colorate.Color(Colors.red, f"The following error occured:", True)))
    b((Colorate.Color(Colors.red, f"{exception}", True)))
    q("Do you want to continue the game?")
    action = inp("y/n")
    match action:
        case "y":
            pass
        case "n":
            exit()

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def headline(text=""):
    print(Center.XCenter(Box.Lines(text)))




####Color Definitions
def green(text):
    return Colorate.Color(Colors.green, f"{text}", True)

def yellow(text):
    return Colorate.Color(Colors.yellow, f"{text}", True)

def red(text):
    return Colorate.Color(Colors.red, f"{text}", True)

def blue(text):
    return Colorate.Color(Colors.blue, f"{text}", True)

def cyan(text):
    return Colorate.Color(Colors.cyan, f"{text}", True)


####Debug List of Objects
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
    return dbg(F"Loaded {definition}: {_curObjects}")