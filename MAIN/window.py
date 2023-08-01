# Imports all views
import arcade
from constants import *
from start_view import StartView
from end_view import EndView
from win_view import WINView
from game_view import GameView

# Main class
class Window(arcade.Window):
    # identifys classes
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.start_view = StartView()
        self.game_view = GameView()
        self.end_view = EndView()
        self.win_view = WINView()
        self.show_view(self.start_view)
        self.game_view.play_song()

