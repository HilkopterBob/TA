"""Module for all Print Statements
"""
# pylint: disable=W,E
import inspect
from pystyle import  Colors, Colorate, Box, Center, Write
from huepy import *
from config import dbg


class pr():

    """
    Utility Class for custom Prints, headlines, Inputs etc...
    """


    # ===== Color Definitions ===== #
    def green(text):
        """Prints Green Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.green, f"{text}", True))

    def yellow(text):
        """Prints Yello Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.yellow, f"{text}", True))

    def red(text):
        """Prints Red Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.red, f"{text}", True))

    def blue(text):
        """Prints Blue Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.blue, f"{text}", True))

    def cyan(text):
        """Prints Cyan Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.cyan, f"{text}", True))
    # =====                  ===== #


    # ===== Print Definitions ===== #
    def n(text=""):
        """Prints White Text with new Line

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        Write.Print(text + "\n", Colors.white, interval=0.0025)

    def a(text=""):
        """Prints Red Text with new Line

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        Write.Print(text + "\n", Colors.red, interval=0.0025)

    def b(text=""):
        """Prints Text with negative Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(bad(text))

    def i(text=""):
        """Prints Text with neutral Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(info(text))

    def g(text=""):
        """Prints Text with positive Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(good(text))

    def q(text=""):
        """Prints Text with Question Mark

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(que(text))

    def dbg(text="", errlvl=0):
        """
            Prints Debug Information into Console
        Args:
            text (str): Text to be Displayed. Defaults to "".
            errlvl (int): Errorlevel 0=Inf, 1=Err. Defaults to 0.
        """

        if not dbg:
            return

        module = inspect.currentframe().f_back.f_globals['__name__']
        function = inspect.stack()[1].function
        line_number = inspect.stack()[1].lineno

        if errlvl == 0:
            print(f'{info("")} {good("")} \
                  {str(yellow(f"[{line_number}] DBG - {module} - {function}: "))} {str(text)}')
        else:
            print(f'{info("")} {bad("")} \
                  {str(yellow(f"[{line_number}] DBG - {module} - {function}: "))} {str(text)}')

    def headline(text=""):
        """Prints Headlines

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(Center.XCenter(Box.Lines(text)))

    def showcase():
        """Prints all the print functions

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        pr.n("Das ist die standard Printanweisung")
        pr.a("Allerts!")
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
