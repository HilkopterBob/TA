""" this is the Helpfile you've just red. """


# Entry-Point = function with same name as File
def Help():
    """Help funktion & GECK entrypoint"""
    help_message = """

    This is the G.E.C.K. !

    It is designed to be an extensable TUI-based (T ext U ser I nterface) helper-program.
    It uses a siple yet extensable framework to execute helper-scripts inside the G.E.C.K. itself!


    How does it work

    The GECK simply prints all .py files inside the 'modules' directory and
    replaces '_' with spaces for bauty. It than starts the program that you have selected by opening
    the file and searching for a function that has the same name as the file itself.

    For example:

    Help.py would need to have a 'Help'-function witch the GECK than starts.

    This is called an Entry-Point. This entry-point can than be used to get all nessesary inputs or call
    other functions.


    Thats it. Look into the Help.py file inside the GECK/modules folder to find technical documentation.
    """

    # Get all nessesary data!
    name = input("Whats your name?\n")

    # Do stuff with data
    print(f"here {name}, this is your helpfile!")
    print(help_message)

    # call other functions from file!
    say_bye(name)


def say_bye(name):
    """Helper function to show GECK functions"""
    print(f"Thats all the help i can give {name}, c u!")
