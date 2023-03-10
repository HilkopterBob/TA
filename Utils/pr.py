from pystyle import  Colors, Colorate, Box, Center, Write
from huepy import *
import inspect



class pr():

    """
    Utility Class for custom Prints, headlines, Inputs etc...
    """


    # ===== Color Definitions ===== #
    def green(text):
        return print(Colorate.Color(Colors.green, f"{text}", True))
    
    def yellow(text):
        return print(Colorate.Color(Colors.yellow, f"{text}", True))
    
    def red(text):
        return print(Colorate.Color(Colors.red, f"{text}", True))
    
    def blue(text):
        return print(Colorate.Color(Colors.blue, f"{text}", True))
    
    def cyan(text):
        return print(Colorate.Color(Colors.cyan, f"{text}", True))
    # =====                  ===== #


    # ===== Print Definitions ===== #
    def n(text=""):
        Write.Print(text + "\n", Colors.white, interval=0.0025)
    
    def a(text=""):
        Write.Print(text + "\n", Colors.red, interval=0.0025)
        

    
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
        pr.n("Das ist die standard Printanweisung")
        pr.a("Allerts!")
        print(pr.inp("Inputs! >_"))
        pr.b("Bad shit")
        pr.i("Information")
        pr.g("Good")
        pr.q("Quest(ion)")
        pr.dbg("InfoLevel Debug")
        pr.dbg("ErrorLevel Debug", 1)
        pr.green("Green Text")
        pr.yellow("Yellow Text")
        pr.red("Red Text")
        pr.blue("Blue Text")
        pr.cyan("Cyan Text")
    
