from pystyle import  Colors, Write
from huepy import *




class Inp():

    """
    Utility Class for getting custom input prompts
    """

    def inp(text=""):
        Input = Write.Input(text + "\n >_ ", Colors.white, interval=0.0025)
        return Input