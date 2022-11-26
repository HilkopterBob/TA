from pystyle import Write, Colors, Colorate
from huepy import *

def n(text=""):
    Write.Print(text + "\n", Colors.white, interval=0.0025)

def a(text=""):
    Write.Print(text + "\n", Colors.white, interval=0.0025)
    
def inp(text=""):
    Input = Write.Input(text + "\n→ ", Colors.white, interval=0.0025)
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
    if errlvl == 0:
        print(info(Colorate.Color(Colors.yellow, 'DEBUG: ', True)) + str(text))
    else:
        print(bad(Colorate.Color(Colors.red, 'DEBUG: ', True)) + str(text))
    
def showcase():
    n("Das ist die standard Printanweisung")
    a("Allerts!")
    print(inp("Inputs!"))
    b("Bad shit")
    i("Information")
    g("Good")
    q("Quest(ion)")
    dbg("InfoLevel Debug")
    dbg("ErrorLevel Debug", 1)

