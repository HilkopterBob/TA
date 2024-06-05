"""Module for all Print Statements
"""

# pylint: disable=W,E
import inspect
from datetime import datetime, date
from pystyle import Colors, Colorate, Box, Center, Write
from huepy import *
from config import dbg, log_file, dbg_level, logbymodule, exclude_dbg_lvl


class Pr:
    """
    Utility Class for custom Prints, headlines, Inputs etc...
    """

    # ===== Color Definitions ===== #
    def purple(text: str) -> None:
        """Prints Green Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.purple, f"{text}", True))

    def green(text: str) -> None:
        """Prints Green Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.green, f"{text}", True))

    def yellow(text: str) -> None:
        """Prints Yello Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.yellow, f"{text}", True))

    def red(text: str) -> None:
        """Prints Red Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.red, f"{text}", True))

    def blue(text: str) -> None:
        """Prints Blue Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.blue, f"{text}", True))

    def cyan(text: str) -> None:
        """Prints Cyan Text

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        return print(Colorate.Color(Colors.cyan, f"{text}", True))

    # =====                  ===== #

    # ===== Print Definitions ===== #
    def n(text: str = "") -> None:
        """Prints White Text with new Line

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        Write.Print(text + "\n", Colors.white, interval=0.0025)

    def a(text: str = "") -> None:
        """Prints Red Text with new Line

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        Write.Print(text + "\n", Colors.red, interval=0.0025)

    def b(text: str = "") -> None:
        """Prints Text with negative Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(bad(text))

    def i(text: str = "") -> None:
        """Prints Text with neutral Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(info(text))

    def g(text: str = "") -> None:
        """Prints Text with positive Indicator

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(good(text))

    def q(text: str = "") -> None:
        """Prints Text with Question Mark

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(que(text))

    def dbg(text: str = "", errlvl: int = 0) -> None:
        """
            Prints Debug Information into Console
        Args:
            text (str): Text to be Displayed. Defaults to "".
            errlvl (int): Errorlevel -1=Dbg, 0=Inf, 1=Warn, 2=Err, 3=Highlight. Defaults to 0.
        """

        today = date.today().strftime("%d-%m-%Y")

        module = inspect.currentframe().f_back.f_globals["__name__"]
        function = inspect.stack()[1].function
        line_number = inspect.stack()[1].lineno

        stack_1 = f"[{line_number}] DBG - {module} - {function}: "
        stack0 = f"[{line_number}] INFO - {module} - {function}: "
        stack1 = f"[{line_number}] WARN - {module} - {function}: "
        stack2 = f"[{line_number}] ERR - {module} - {function}: "

        message = str(text)
        timestamp = datetime.now().strftime("%H:%M:%S")

        match errlvl:
            case -1:  # Debug
                logstr = f"{stack_1}{message}"
                if exclude_dbg_lvl:
                    logstr = None
                if dbg_level >= 3:
                    if dbg:
                        print(
                            f'{info("")} {good("")} \
                                    {str(purple(stack_1))} {message}'
                        )
            case 0:  # Informational
                logstr = f"{stack0}{message}"
                if dbg_level >= 2:
                    if dbg:
                        print(
                            f'{info("")} {good("")} \
                                    {str(green(stack0))} {message}'
                        )

            case 1:  # Warning
                logstr = f"{stack1}{message}"
                if dbg_level >= 1:
                    if dbg:
                        print(
                            f'{info("")} {info("")} \
                                    {str(yellow(stack1))} {message}'
                        )

            case 2:  # Err
                logstr = f"{stack2}{message}"
                if dbg_level >= 0:
                    if dbg:
                        print(
                            f'{info("")} {bad("")} \
                                    {str(red(stack2))} {message}'
                        )

            case 3:  # Highlight
                logstr = f"{stack2}{message}"
                if dbg_level >= 0:
                    if dbg:
                        print(
                            f'{info("")} {cyan("")} \
                                    {str(yellow(stack2))} {message}'
                        )

        with open(log_file, "a") as log:
            if logstr:
                log.write(f"{timestamp} - {logstr}\n")

        if logbymodule:
            _log_file = log_file.split("/")
            _log_file.insert(1, f"/{module} - ")
            _log_file = "".join(_log_file)
            with open(_log_file, "a") as log:
                log.write(f"{timestamp} - {logstr}\n")

    def headline(text: str = "") -> None:
        """Prints Headlines

        Args:
            text (String): Text to be Printed

        Returns:
            Print: String
        """
        print(Center.XCenter(Box.Lines(text)))
