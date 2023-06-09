import arcade
from arcade.experimental import CV2PlayerView
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

class Cutscene(CV2PlayerView):
    def __init__(self):
        super().__init__(ROOT_FOLDER.joinpath("screen-capture.webm"))

game = arcade.Window()
cutscene = Cutscene()
game.show_view(cutscene)
arcade.run()