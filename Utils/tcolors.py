"""Color Definitions"""


def purple(text):
    """Prints Green Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;35m{text}\033[0m"


def green(text):
    """Prints Green Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;32m{text}\033[0m"


def yellow(text):
    """Prints Yello Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;33m{text}\033[0m"


def red(text):
    """Prints Red Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;31m{text}\033[0m"


def blue(text):
    """Prints Blue Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;34m{text}\033[0m"


def cyan(text):
    """Prints Cyan Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;36m{text}\033[0m"


def white(text):
    """Prints White Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;37m{text}\033[0m"
