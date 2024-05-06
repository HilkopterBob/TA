"""AdventureForge
"""

# TODO: start mainscreen
# TODO: get editor-selection
# TODO: goto Editor

# TODO: ##### Editor #####
# TODO: start json-parser
# TODO: get definitions of object-attributes
# TODO: create possible widget-tree
# TODO: populate widgets with schema data, eg. type-descriptions as shadow-texts
# TODO: start generated app
# TODO: get user input
# TODO: create object
# TODO: dump to json
# TODO: go back to main

from blessed import Terminal

term = Terminal()


# Leveleditor-Funktion
def level_editor():
    print(term.clear)
    print(term.center(term.bold("Leveleditor")))
    term.inkey()  # Hier kann die Funktionalität des Leveleditors implementiert werden


# Effecteditor-Funktion
def effect_editor():
    print(term.clear)
    print(term.center(term.bold("Effecteditor")))
    term.inkey()  # Hier kann die Funktionalität des Effecteditors implementiert werden


# Itemeditor-Funktion
def item_editor():
    print(term.clear)
    print(term.center(term.bold("Itemeditor")))
    term.inkey()  # Hier kann die Funktionalität des Itemeditors implementiert werden


# Entityeditor-Funktion
def entity_editor():
    print(term.clear)
    print(term.center(term.bold("Entityeditor")))
    term.inkey()  # Hier kann die Funktionalität des Entityeditors implementiert werden


def main():
    while True:
        print(term.clear)
        print(term.center(term.blink("AdventureForge")))
        print(term.center(term.italic("Hauptmenü")))
        print()
        print("")
        print("1. Leveleditor")
        print("2. Effecteditor")
        print("3. Itemeditor")
        print("4. Entityeditor")
        print("0. Beenden")

        with term.cbreak():
            val = term.inkey()
            if val == "1":
                level_editor()
            elif val == "2":
                effect_editor()
            elif val == "3":
                item_editor()
            elif val == "4":
                entity_editor()
            elif val == "0":
                break


if __name__ == "__main__":
    main()
