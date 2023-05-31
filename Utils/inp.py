"""Defines Input Method for User
"""
from pystyle import  Colors, Write
from Inputparser import inputparser


class Inp():

    """
    Utility Class for getting custom input prompts
    """

    def inp(text=""):
        """Method to get User Input
        """
        Input = Write.Input(text + "\n >_ ", Colors.white, interval=0.0025)
        inputparser.user_input = Input
        return inputparser.user_input
