from pystyle import Write, Colors
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

def showcase():
    n("Das ist die standard Printanweisung")
    a("Allerts!")
    print(inp("Inputs!"))
    b("Bad shit")
    i("Information")
    g("Good")
    q("Quest(ion)")

