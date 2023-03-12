"""Defines Input Method for User
"""
from pystyle import  Colors, Write


class Inp():

    """
    Utility Class for getting custom input prompts
    """

    def inp(text=""):
        """Method to get User Input
        """
        Input = Write.Input(text + "\n >_ ", Colors.white, interval=0.0025)
        return Input
