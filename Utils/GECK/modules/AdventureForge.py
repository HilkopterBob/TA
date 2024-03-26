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

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Markdown, Button

TITLE = """\
# AdventureForge

## The Text Adventure Engine Editor
"""


class LevelEditor(Screen):
    """Level-Editor Screen"""

    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Static(" Windows ", id="title")
        yield Static("Press any key to continue [blink]_[/]", id="any-key")


class AdventureForge(App):
    """Main-App Framework"""

    # BINDINGS = [("b", "push_screen('bsod')", "BSOD")]

    CSS_PATH = "AdventureForge.tcss"

    def compose(self) -> ComposeResult:
        yield Markdown(TITLE, id="title")
        yield Button("Level Editor!", variant="primary", classes="box")
        yield Button("Item Editor!", variant="primary", classes="box")
        yield Button("Entity Editor!", variant="primary", classes="box")
        yield Button("Effect Editor!", variant="primary", classes="box")

    def on_mount(self) -> None:
        """mount screens at runtime"""
        # self.install_screen(Mainscreen(), name="Mainscreen")
        self.install_screen(LevelEditor(), name="LevelEditor")


if __name__ == "__main__":
    app = AdventureForge()
    app.run()
