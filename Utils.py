from pystyle import Write, Colors

class Utils():

    def __init__(self) -> None:
        pass

    def pr(text):
        Write.Print(text + "\n", Colors.red_to_purple, interval=0.0025)

    #verinfachte Printanweisung in roter farbe für alerts
    def pra(text):
        Write.Print(text + "\n", Colors.red, interval=0.0025)
    
    def prin(text):
        Input = Write.Input(text + "\n→ ", Colors.red_to_purple, interval=0.0025)
        return Input