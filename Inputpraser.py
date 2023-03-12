"""
Inputparser Module which holds 1 Function
    inputparser()
"""
def inputparser(user_input, minl=5, maxl=50):
    """Parses the User Inputs

    Args:
        user_input (String): Input from user
        minl (int, optional): Min length of String. Defaults to 5.
        maxl (int, optional): Max length of String. Defaults to 50.

    Returns:
        String: user_input
    """
    befehlszeichen = "#"


    try:

        if not user_input.strip():
            raise ValueError("Leere Eingabe")

        if len(user_input) < minl:
            raise ValueError(f"Der Input muss mindestens {minl} Zeichen lang sein")

        if len(user_input.strip()) > maxl:
            raise ValueError(f"Der Input darf nicht länger als {maxl} Zeichen sein")

        #Wenn Eingabe == Zahl dann
        if user_input.isdigit():
            user_input = int(user_input)

        #Wenn Eingabe == String dann
        else:
            user_input = str(user_input)
            user_input = user_input.lower() #alles kleinbuchstaben

            #befehlserkennung
            if user_input[0]==befehlszeichen:
                return user_input[1:]

            print(f"Ich bin ein Text: {user_input}")

        return user_input

    except ValueError as e:
        print ("Fehler bei Eingabe:", e)
        return None
    except:
        print ("Unbekannter Fehler beim Input")
        return None


inputstr = input("Geben Sie eine Benutzereingabe ein: ")
processed_input = inputparser(inputstr, minl=2, maxl=10)
if processed_input is not None:
    print(processed_input)
    print(type(inputstr))
    print(type(processed_input))
