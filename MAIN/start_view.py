import arcade
from constants import *
from game_view import GameView

# starting menu window
class StartView(arcade.View):
    # STARTING SCREEN
    def __init__(self):
        super().__init__()
    def on_draw(self):
        self.clear()
        self.bullet_list = None
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        # text on start screen
        arcade.draw_text("WELCOME TO MY GAME", WIDTH/2, HEIGHT/2 -100, arcade.color.ALMOND)
        arcade.draw_text("PUSH TO START THE GAME ALREADY!!!", WIDTH/2, HEIGHT/2 - 150, arcade.color.ALMOND)
    
    # loads background
    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath("Assets",'background.png'))
        # arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    # starts game 
    def on_key_press(self, symbol:int, modifiers:int):
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
    # starts game
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)