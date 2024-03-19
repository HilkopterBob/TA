"""GECK Level-Generator module
"""

import questionary
from rich.prompt import Prompt


class Level:
    """
    Class which defines Levels
    Contains Functions:
    from_json : Creates Levels from JSON
    """

    __slots__ = (
        "name",
        "descr",
        "text",
        "choices",
        "inv",
        "triggers",
        "ltype",
        "entitylist",
        "entityspawn",
    )

    def __init__(
        self,
        text=None,
        choices=None,
        name="Levelnameplatzhalter",
        inv=None,
        ltype="Testtype",
        descr="Standartdescription du Sohn einer Dirne",
        entitylist=None,
        entityspawn=None,
        triggers=None,
    ):
        if text is None:
            text = []
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
        if editor_choices[choice] == "Create new Level":
            create_new_Level()
        if editor_choices[choice] == "Edit existing Level":
            edit_level()
        else:
            print("Wrong Input. restarting...\n\n\n\n\n\n\n\n\n")


def create_new_Level():
    """create new level"""
    new_level = Level(
        name=questionary.text("Wie willst du das Level nennen?"),
        descr=questionary.text("Welche Beschreibung soll das Level haben?"),
        ltype=questionary.select(
            "Welchen Typus soll das Level haben?",
            choices=["friedlich", "neutral", "feindlich", "böse"],
        ),
        choices=create_choices(),
        triggers=get_triggers(),
    )

    print("Dein neues level!")
    print(vars(new_level))


def create_choices():
    """create choices, texts and allow_triggers"""
    create_choices_bool = True

    while create_choices_bool is True:
        new_choice = Choice(
            choice=questionary.text("Welchen Text soll die Choice anzeigen?"),
            text=questionary.text("Welchen Ausgabetext soll die Choice zeigen?"),
        )

        if questionary.confirm("Soll die Choice einen Allow_trigger haben?") is True:
            new_choice.allow_trigger = {
                questionary.text(
                    "Bitte gebe den Trigger-Dict-Key ein:\n"
                ): questionary.text("Biite gebe das Trigger-Dict-Value ein:\n")
            }

        if questionary.confirm("Soll die Choice eine Action haben?") is True:
            new_choice_action = questionary.select(
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

        # TODO: further develop Actions

        create_choices_bool = questionary.confirm(
            "Möchtest du weitere Choices erstellen?"
        )
        if create_choices_bool is False:
            return []


def get_triggers():
    """somehow get the level default triggers"""


def edit_level():
    """edit existing level"""


if __name__ == "__main__":
    create_Level()
