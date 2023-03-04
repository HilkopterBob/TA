def inputphraser(user_input, min=5, max=50, itype="text"):
    # type = "text" o. int


    try:
        if not user_input.strip():
            raise ValueError("Leere Eingabe")
        
        
        user_input = user_input.lower() #alles kleinbuchstaben
        user_input = user_input.strip() #entfernt Leerzeichen vor und Nach Input

        if len(user_input) < min:
            raise ValueError(f"Der Input muss mindestens {min} Zeichen lang sein")
        
        if len(user_input) > max:
            raise ValueError(f"Der Input darf nicht länger als {max} Zeichen sein")

        if(itype) == "int":
            match user_input.isdigit():
                case True:
                   user_input = int(user_input)
                case False:
                    raise ValueError("Der Input muss eine Zahl sein")
                case _:
                    pass


        return user_input
    
    except ValueError as e:
        print ("Fehler bei Eingabe:", e)
        return None
    except:
        print ("Unbekannter Fehler beim Input")
        return None
    
user_input = input("Geben Sie eine Benutzereingabe ein: ")
processed_input = inputphraser(user_input, min=2, max=10, itype="int")
if processed_input is not None:
    print(processed_input)
    print(type(user_input))
    print(type(processed_input))

#befehlserkennung
#nur zalen/text erlaubt