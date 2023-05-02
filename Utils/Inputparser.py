"""
Inputparser Module which holds 1 Function
    inputparser()
"""

#from Utils import Inp
from config import dbg
from Utils import Debug
from Utils import pr
from Entities import Entity

def inputparser(    min_len=0,
                    max_len=150,
                    user_input=None
                    ):

    """Parses the User Inputs

    Args:
        user_input (String): Input from user
        minl (int, optional): Min length of String. Defaults to 5.
        maxl (int, optional): Max length of String. Defaults to 50.

    Returns:
        String: user_input
    """
    #user_input = Inp.inp()
    befehlszeichen = "#"
    userbefehl = [" inv: Öffnet das Inventar"," opt: Öffnet die Optioen"," men: Öffnet das Menü","save: Speichert das Spiel","exit: Schließt das Spiel"]
    devbefehl = ["test: test","","","","","","",]
    
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
                
                #dev Befehle
                case "hallo":
                    print("Hallo")
                    for e in input_list:
                        print(e)
                
                
                
                
                
                #User Befehle
                
                case "help":
                    pr.headline ("userbefehle")
                    for einzelwert in userbefehl:
                            pr.i(einzelwert)
                    if (dbg == True) :
                        pr.n ("")
                        pr.headline ("devbefehle")
                        for einzelwert in devbefehl:
                            pr.i(einzelwert)
                
                    

                case "opt":
                    pass

                case "inv":
                    pass
                
                case "men":
                    Entity.change_location()
                        

                case "save":
                    pr.i("Die Funktion ist noch nicht implementiert")

                case "exit":
                    Debug.stop_game()

                case _:
                    pass

            return inputparser()
        return user_input
        

    except ValueError as e:
        pr.a (f"Fehler bei Eingabe: {e}")
        return None
    except:
        pr.a ("Unbekannter Fehler beim Input")
        return None
    



#inputparser()
