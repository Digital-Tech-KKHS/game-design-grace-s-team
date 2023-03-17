import arcade
import random
class Game(arcade.Window):
    def __init__(self):
        super().__init(1000, 1000, "terrain-gen")
        self.player = arcade.Sprite(":res")
        self.camera = arcade.Camera()
        arcade.set_background_color(arcade.color.VANILLA)
        map_name = ""
        self.tilemap = arcade.load_tilemap(map_name)
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        self.scene.add_sprite("player", self.player)

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()

    def on_update(self):
        self.camera.move_to((self.player.center_x-500, self.player.center_y-500))

    def on_onmouse_motion(self, x, y, dx, dy):
        self.player,change_x = (x - 500) / 100
        self.player.change_y = (y - 500) / 100

    def on_key_press(self, symbol, modifiers):
        head = '''<?xml version="1.0" encoding="UTF-8"?>
<map version="1.8" tiledversion="1.8.2" orientation="orthogonal" renderorder="right-down" width="50" height="50" tilewidth="128" tileheight="128" infinite="0" nextlayerid="2" nextobjectid="1">
 <tileset firstgid="1" source="spritesheet_ground.tsx"/>
 <layer id="1" name="Tile Layer 1" width="50" height="50">
  <data encoding="csv">'''

        tail = '''</data>
 </layer>
</map>'''

        with open("Map_Practice.tmx", "w") as file:
            for i in range(50):
                for j in range(50):
                    file.write(f"{random.choice([0,2])},")
                file.write("\n")
            file.write(tail)

        self.tilemap = arcade.load_tilemap("Map_Practice.tmx")
        self.Scene
            
            # tile_map = []
            # for i in range(50):
            #     tile_map.append([])



game = Game()
arcade.run()