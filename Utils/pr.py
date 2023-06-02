"""Module for all Print Statements
"""
# pylint: disable=W,E
import inspect
from datetime import datetime
from pystyle import  Colors, Colorate, Box, Center, Write
from huepy import *
from config import dbg, log_file, dbg_level

class Pr():

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
            errlvl (int): Errorlevel 0=Inf, 1=Warn, 2=Err, 3=Highlight. Defaults to 0.
        """

        if not dbg:
            return

        module = inspect.currentframe().f_back.f_globals['__name__']
        function = inspect.stack()[1].function
        line_number = inspect.stack()[1].lineno

        stack0 = f"[{line_number}] INFO - {module} - {function}: "
        stack1 = f"[{line_number}] WARN - {module} - {function}: "
        stack2 = f"[{line_number}] ERR - {module} - {function}: "

        message = str(text)

        match errlvl:
            case 0: #Informational
                if dbg_level >= 2:
                    logstr = f'{stack0}{message}'
                    print(f'{info("")} {good("")} \
                                {str(green(stack0))} {message}')

            case 1: #Warning
                if dbg_level >= 1:
                    logstr = f'{stack1}{message}'
                    print(f'{info("")} {info("")} \
                                {str(yellow(stack1))} {message}')

            case 2: #Err
                if dbg_level >= 0:
                    logstr = f'{stack2}{message}'
                    print(f'{info("")} {bad("")} \
                                {str(red(stack2))} {message}')

            case 3: #Err
                if dbg_level >= 0:
                    logstr = f'{stack2}{message}'
                    print(f'{info("")} {cyan("")} \
                                {str(yellow(stack2))} {message}')

        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(log_file, "a") as log:
            log.write(f'{timestamp} - {logstr}\n')


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
        Pr.n("Das ist die standard Printanweisung")
        Pr.a("Allerts!")
        Pr.b("Bad shit")
        Pr.i("Information")
        Pr.g("Good")
        Pr.q("Quest(ion)")
        Pr.dbg("InfoLevel Debug")
        Pr.dbg("WarningLevel Debug",1)
        Pr.dbg("ErrorLevel Debug",2)
        Pr.green("Green Text")
        Pr.yellow("Yellow Text")
        Pr.red("Red Text")
        Pr.blue("Blue Text")
        Pr.cyan("Cyan Text")
