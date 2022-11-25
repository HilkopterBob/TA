from pystyle import Write, Colors

def n(text):
    Write.Print(text + "\n", Colors.red_to_purple, interval=0.0025)

#verinfachte Printanweisung in roter farbe für alerts
def a(text):
    Write.Print(text + "\n", Colors.red, interval=0.0025)
    
def inp(text):
    Input = Write.Input(text + "\n→ ", Colors.red_to_purple, interval=0.0025)
    return Input