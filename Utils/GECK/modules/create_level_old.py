"""GECK Level-Generator module
"""

import questionary
import npyscreen

class Level:
    """
    Class which defines Levels
    Contains Functions:
    from_json : Creates Levels from JSON
    """

    __slots__ = (
        "name",
        "descr",
        # "text",
        "choices",
        "inv",
        "triggers",
        "ltype",
        "entitylist",
        "entityspawn",
    )

    def __init__(
        self,
        # text=None,
        choices=None,
        name="Levelnameplatzhalter",
        inv=None,
        ltype="Testtype",
        descr="Standartdescription du Sohn einer Dirne",
        entitylist=None,
        entityspawn=None,
        triggers=None,
    ):
        # if text is None:
        #     text = []
        if choices is None:
            choices = []
        if inv is None:
            inv = []
        if entitylist is None:
            entitylist = []
        if triggers is None:
            triggers = []
        if entityspawn is None:
            entityspawn = []

        self.name = name
        self.descr = descr
        # self.text = text
        self.choices = choices
        self.inv = inv
        self.triggers = triggers
        self.ltype = ltype
        self.entitylist = entitylist
        self.entityspawn = entityspawn


class Choice:
    """
    Class witch defines Choices.
    """

    def __init__(self, text, choice, allow_trigger=None):
        self.choice = choice
        self.text = text
        self.allow_trigger = allow_trigger

import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()

def create_Level():
    """GECK entry-point"""

    ASCII_ART = r"""
__/\\\__________________________________________________________/\\\\\\_______________/\\\\\\\\\\\\\\\_________/\\\__________________________________________________        
 _\/\\\_________________________________________________________\////\\\______________\/\\\///////////_________\/\\\__________________________________________________       
  _\/\\\____________________________________________________________\/\\\______________\/\\\____________________\/\\\___/\\\_____/\\\__________________________________      
   _\/\\\_________________/\\\\\\\\___/\\\____/\\\_____/\\\\\\\\_____\/\\\______________\/\\\\\\\\\\\____________\/\\\__\///___/\\\\\\\\\\\_____/\\\\\_____/\\/\\\\\\\__     
    _\/\\\_______________/\\\/////\\\_\//\\\__/\\\____/\\\/////\\\____\/\\\______________\/\\\///////________/\\\\\\\\\___/\\\_\////\\\////____/\\\///\\\__\/\\\/////\\\_    
     _\/\\\______________/\\\\\\\\\\\___\//\\\/\\\____/\\\\\\\\\\\_____\/\\\______________\/\\\______________/\\\////\\\__\/\\\____\/\\\_______/\\\__\//\\\_\/\\\___\///__   
      _\/\\\_____________\//\\///////_____\//\\\\\____\//\\///////______\/\\\______________\/\\\_____________\/\\\__\/\\\__\/\\\____\/\\\_/\\__\//\\\__/\\\__\/\\\_________  
       _\/\\\\\\\\\\\\\\\__\//\\\\\\\\\\____\//\\\______\//\\\\\\\\\\__/\\\\\\\\\___________\/\\\\\\\\\\\\\\\_\//\\\\\\\/\\_\/\\\____\//\\\\\____\///\\\\\/___\/\\\_________ 
        _\///////////////____\//////////______\///________\//////////__\/////////____________\///////////////___\///////\//__\///______\/////_______\/////_____\///__________
"""

    editor_loop = True
    editor_choices = ["Create new Level", "Edit existing Level"]
    app = CreateNewLevel().run()

    while editor_loop is True:
        print(ASCII_ART)

        print("\n\nModules:")

        for index, module in enumerate(editor_choices):
            print(f"[{index + 1}.] {module.replace('_', ' ')}")
        available_choices = []
        for index, _ in enumerate(editor_choices):
            available_choices.append(str(index + 1))

        choice = (
            int(
                Prompt.ask(
                    "Choose wich tool do you want to load:", choices=available_choices
                )
            )
            - 1
        )
        print(f"{choice} + {editor_choices[choice]}")
        module_to_load = editor_choices[choice]
        print(module_to_load)
        print(type(module_to_load))
        if module_to_load == "Create new Level":
            app = CreateNewLevel().run()
            #create_new_Level()
        # if choice == 0:
        #     create_new_Level()
        # elif choice == 1:
        #     edit_level()
        # else:
        #     print("Wrong Input. restarting...\n\n\n\n\n\n\n\n\n")


def create_new_Level():
    """create new level"""
    new_level = Level(
        name=Prompt.ask("Wie willst du das Level nennen?"),
        descr=Prompt.ask("Welche Beschreibung soll das Level haben?"),
        ltype=Prompt.ask(
            "Welchen Typus soll das Level haben?",
            choices=["friedlich", "neutral", "feindlich", "böse"],
        ),
        choices=create_choices(),
        triggers=get_triggers(choices),
    )
    print("\n".join([f"{attr}: {getattr(new_level, attr)}" for attr in dir(new_level)]))
    for choice in new_level.choices:
        print("\n".join([f"{attr}: {getattr(choice, attr)}" for attr in dir(choice)]))


TODO: rework to de TUI-Based
def create_choices():
    """create choices, texts and allow_triggers"""
    create_choices_bool = Confirm.ask("Möchtest du eine Choice erstellen?")
    created_choices = []

    while create_choices_bool is True:
        new_choice = Choice(
            choice=Prompt.ask("Welchen Text soll die Choice anzeigen?"),
            text=Prompt.ask("Welchen Ausgabetext soll die Choice zeigen?"),
        )

        if (
            Confirm.ask(
                "Soll die Choice einen Allow_trigger haben?", choices=["yes", "no"]
            )
            is True
        ):
            new_choice.allow_trigger = {
                Prompt.ask("Bitte gebe den Trigger-Dict-Key ein:\n"): Prompt.ask(
                    "Biite gebe das Trigger-Dict-Value ein:\n"
                )
            }

        if (
            Confirm.ask("Soll die Choice eine Action haben?", choices=["yes", "no"])
            is True
        ):
            new_choice_action = Prompt.ask(
                "Welche Action soll die Choice haben?",
                choices=[
                    "close_game",
                    "add_effect",
                    "change_location",
                    "change_health",
                    "add_item",
                    "remove_item_by_name",
                    "remove_item_by_index",
                    "remove_effect_by_name",
                    "change_stat",
                    "take_damage",
                    "change_gamestate",
                    "show_wip",
                ],
            )
            new_choice_action_attr_bool = Confirm.ask(
                "Soll die Action ein zusätzliches Datenattribut bekommen?",
                choices=["yes", "no"],
            )
            new_choice_action_attr = []
            while new_choice_action_attr_bool is True:
                new_choice_action_attr.append(
                    Prompt.ask("Gebe das Choice-Action-Datenattribut als Dict an:\n")
                )
                new_choice_action_attr_bool = Confirm.ask(
                    "Soll die Action ein zusätzliches Datenattribut bekommen?",
                    choices=["yes", "no"],
                )
                if new_choice_action_attr_bool is not True:
                    break

        created_choices.append(new_choice)

        create_choices_bool = Confirm.ask("Möchtest du weitere Choices erstellen?")
        if create_choices_bool is False:
            print(created_choices)
            return created_choices


def get_triggers(choices):
    """somehow get the level default triggers"""
    # TODO: Develop Trigger-Editor
    list_created_choice_triggers = []
    for choice in choices:
        for trigger in choice:
            list_created_choice_triggers.append(trigger)

    edit_triggers_bool = Confirm.ask("welche Defaultwerte sollen ?")

    create_choices_bool = Confirm.ask("Möchtest du weitere Choices erstellen?")


def edit_level():
    """edit existing level"""


if __name__ == "__main__":
    create_Level()
