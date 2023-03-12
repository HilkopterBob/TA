"""
Inputparser Module which holds 1 Function
    inputparser()
"""

from actionparser import Actionparser
from Utils import Inp


def inputparser(    min_len=0, 
                    max_len=150
                    ):
    
    """Parses the User Inputs

    Args:
        user_input (String): Input from user
        minl (int, optional): Min length of String. Defaults to 5.
        maxl (int, optional): Max length of String. Defaults to 50.

    Returns:
        String: user_input
    """
    user_input = Inp.inp()
    befehlszeichen = "#"

    try:
        if not user_input.strip():
            raise ValueError("Leere Eingabe")

        if len(user_input) < min_len:
            raise ValueError(f"Der Input muss mindestens {min_len} Zeichen lang sein")

        if len(user_input.strip()) > max_len:
            raise ValueError(f"Der Input darf nicht länger als {max_len} Zeichen sein")

        #alles kleinbuchstaben
        user_input = user_input.lower() 
        #Wenn Eingabe == Zahl dann
        if user_input.isdigit():
            user_input = int(user_input)

        #Wenn Eingabe == String dann
        elif user_input[0]==befehlszeichen:
            #befehlserkennung
            input_command = user_input[1:]
            input_list = input_command.split()
            match input_list[0]:
                case "hallo":
                    print("Hallo")
                    for e in input_list:
                        print(e)

                case _:
                    pass

            return inputparser()
        return user_input

    except ValueError as e:
        print ("Fehler bei Eingabe:", e)
        return None
    except:
        print ("Unbekannter Fehler beim Input")
        return None


inputparser()