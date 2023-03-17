from tkinter import Scale
import opensimplex
import arcade
import random
class Game(arcade.Window):
    def __init__(self):
        super().__init__(1200, 1200, "tgen")
        arcade.set_background_color(arcade.color.VANILLA)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("walls")
        opensimplex.seed(random.randint(0, 10000000000000000000))
        for y in range(50):
            for x in range(50):
                chance = opensimplex.noise2(x/10,y/10) > 0
                scale = 0.2

                if chance:
                    wall = arcade.Sprite("ground1.png", scale)
                    wall.center_x = x *128 * scale
                    wall.center_y = y *128 * scale
                    self.scene["walls"].append(wall)  

 
    def on_draw(self):
        self.clear()
        self.scene.draw()


game = Game()
arcade.run()
