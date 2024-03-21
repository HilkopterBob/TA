from textual.app import App, ComposeResult
from textual.widgets import Input, Select


class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Levelname:")
        yield Input(placeholder="Levelbeschreibung:")
        LINES = ["friendly", "evil", "nutral"]
        yield Select([(line, line) for line in LINES], value="nutral")


if __name__ == "__main__":
    app = InputApp()
    app.run()
