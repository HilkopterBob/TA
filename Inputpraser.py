import json

with open('config/commands.json', 'r') as f:
     data = json.load(f)

def inputphraser(user_input, min_len=5, max_len=50):
    befehlszeichen = "#"


    try:

        if not user_input.strip():
            raise ValueError("Leere Eingabe")
        
        if len(user_input) < min_len:
            raise ValueError(f"Der Input muss mindestens {min_len} Zeichen lang sein")
        
        if len(user_input.strip()) > max_len:
            raise ValueError(f"Der Input darf nicht länger als {max_len} Zeichen sein")
        
        #Wenn Eingabe == Zahl dann
        if (user_input.isdigit()):
            user_input = int(user_input)

        #Wenn Eingabe == String dann
        else:
            user_input = str(user_input)
            user_input = user_input.lower() #alles kleinbuchstaben
            
            #befehlserkennung
            if (user_input[0]==befehlszeichen): 
                input_command = user_input[1:]
                for command in data['commands']:
                    if input_command == command['name']:
                        print("Processing " + command['name'] + " command...")
                       # print(command['action'])
                        exec(command['action'])
                        return None
                else:
                   raise ValueError("Ungültiger Befehl")
                    
                
                
                
            
            print(f"Ich bin ein Text: {user_input}")

        return user_input
    
    except ValueError as e:
        print ("Fehler bei Eingabe:", e)
        return None
    except:
        print ("Unbekannter Fehler beim Input")
        return None


user_input = input("Geben Sie eine Benutzereingabe ein: ")
processed_input = inputphraser(user_input, min_len=2, max_len=10)
if processed_input is not None:
    print(processed_input)
   # print(type(user_input))
   # print(type(processed_input))








