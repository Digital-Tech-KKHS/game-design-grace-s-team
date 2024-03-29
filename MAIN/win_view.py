import arcade
from constants import *
from start_view import StartView
class WINView(arcade.View):
    
        # Draws view and puts in PNG
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture(ROOT_FOLDER.joinpath("Assets","win.png"))
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)
    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(WIDTH / 2, HEIGHT / 2,
                                WIDTH, HEIGHT)
        arcade.draw_text("You are free little owl...for now...", 500, 500, arcade.color.BLACK,20,0,"left","arial",True)

        # Switches to StartView"
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        start_view = StartView()
        self.window.show_view(start_view)
