"""errorhandler with error decorator"""

from functools import wraps
import time

from rich import markdown, print  # pylint: disable=W0622

from Utils.logger import Logger

default_error_message = """
\n\n\n\n\n
# You've found a bug!

_Please report it as issue to:_
__www.github.com/HilkopterBob/TA__

_Please attach your current logfile from:_
__TA/logs/<logfile>__

Thank your for your Support!
_The Dev's_
"""


def error(function=None, errortype=None):
    """@error decorator"""

    def errorhandler(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            # TODO: add sensible errors

            # If no special error type given,
            # use general error handling
            try:
                return f(*args, **kwargs)
            except Exception as e:
                Logger.log(e, 4)
            finally:
                print(markdown.Markdown(default_error_message))
                time.sleep(5)
            # return f(*args, **kwargs)

        return wrapper

    if function:
        return errorhandler(function)
    return errorhandler
