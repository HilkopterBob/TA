"""Color Definitions"""


def purple(text: str) -> str:
    """Prints Green Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;35m{text}\033[0m"


def green(text: str) -> str:
    """Prints Green Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;32m{text}\033[0m"


def yellow(text: str) -> str:
    """Prints Yello Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;33m{text}\033[0m"


def red(text: str) -> str:
    """Prints Red Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;31m{text}\033[0m"


def blue(text: str) -> str:
    """Prints Blue Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;34m{text}\033[0m"


def cyan(text: str) -> str:
    """Prints Cyan Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;36m{text}\033[0m"


def white(text: str) -> str:
    """Prints White Text

    Args:
        text (String): Text to be Printed

    Returns:
        Print: String
    """
    return f"\033[1;37m{text}\033[0m"
