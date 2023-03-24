# Different plugins
from tracemalloc import start
import arcade
import random
from pathlib import Path

# where to get files from
ROOT_FOLDER = Path(__file__).parent

WIDTH = 1200
HEIGHT = 700
TITLE = "Game"
STARTING_HEALTH = 5

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
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath('background.png'))
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

# Win Menu Window
class WINView(arcade.View):
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture(ROOT_FOLDER.joinpath("win.png"))

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(WIDTH / 2, HEIGHT / 2,
                                WIDTH, HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        start_view = StartView()
        # start_view.setup()
        self.window.show_view(start_view)


class EndView(arcade.View):
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture(ROOT_FOLDER.joinpath("game_over.png"))

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(WIDTH / 2, HEIGHT / 2,
                                WIDTH, HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Entity(arcade.Sprite):
    # Character
    def __init__(self, foldername):
        super().__init__(ROOT_FOLDER.joinpath(foldername, "idle.png"))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, "idle.png"))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        
        for i in range(10):
            tex = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, f"walk{i}.png"))
            self.walk_textures.append(tex)
            
    def update_animation(self):
        if self.change_x > 0:
             self.face_direction = 1
        if self.change_x < 0:
             self.face_direction = 0
        
        if self.change_x ==0:
            self.texture = self.idle_textures[self.face_direction]
        else:
            self.texture = self.walk_textures[self.current_texture][self.face_direction]
            self.odo += 1
            if self.odo % 4 ==0:
                self.current_texture += 1
                self.current_texture = self.current_texture % 10

class Player(Entity):
    def __init__(self, foldername):
        super().__init__(foldername)

class GameView(arcade.View): 
    def __init__(self):
        super().__init__()
        # arcade.set_background_color(arcade.color.BURNT_UMBER)
        # def on_show_view(self):
        self.player = None
        self.tilemap = None
        self.scene = None
        self.HUD = None
        self.physics_engine = None
        self.camera = None
        self.HUD_camera = None
        self.score = 0
        self.level = 0
        player_sprite = 0
        self.background = None
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        self.setup()
    
    


    def setup(self):
        # where the character spawns in and which map it uses
        self.player = Player('Character')
        self.player.center_x = 40
        self.player.center_y = 1000
        self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(f'map_{self.level}.tmx'))
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.scene["Ground"])
        self.camera = arcade.Camera(WIDTH, HEIGHT)
        self.HUD_camera = arcade.Camera(WIDTH, HEIGHT)
        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
 
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        self.scene.move_sprite_list_after('Foreground', 'player')
        self.bullet_list = arcade.SpriteList()

        # Adds in health with my own made health art
        for i in range(STARTING_HEALTH):
            x = 25 + 60 * i
            y = HEIGHT - 40
            grass = arcade.Sprite(ROOT_FOLDER.joinpath('health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(grass)
            # health = [0, 1, 2, 3, 4]
            # index = health.index[ health-1 ]
        
    def update_animation(self):
        super().update_animation()

    def on_draw(self):
        # adding back round for game view   
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.camera.use()
        self.scene.draw()
        # self.player.draw_hit_box((255, 0,0,255), 2)
        self.HUD_camera.use()
        self.HUD.draw()
        arcade.draw_text(f"Coins: {self.score}", WIDTH-100, HEIGHT-50)
    
    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath('background2.png'))



# FOR SPRITE ON COINS
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()
        self.physics_engine.update()
        self.scene.update()
        for coin in self.scene['coins']:
            coin.on_update()
        self.center_camera_on_player()
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['coins'])
        for coin in colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()
  
        if self.player.center_y <0:
            self.HUD['health'][-1].kill()
            self.player.center_x = 40
            self.player.center_y = 1000
            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)
        # making my dragon spawn at the start and lose health when it falls off of map
        
        
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['DONT_TOUCH'])
        # COLLIDING WITH FIRE
        if colliding:
            self.score -= 1
            self.HUD['health'][-1].kill()
            self.player.change_x *= -1.3
            self.player.change_y *= -1.3
        
            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['coins'])
        if colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()


        colliding = arcade.check_for_collision_with_list(self.player, self.scene['WIN'])
        if colliding:
            self.level += 1
            self.setup()

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['WINNER'])
        if colliding:
            self.window.show_view(self.window.win_view)
            self.setup()


    def center_camera_on_player(self):
        camera_x = self.player.center_x - WIDTH / 2
        camera_y = self.player.center_y - HEIGHT / 2
       
        if self.player.center_x < WIDTH / 2:
            camera_x = 2
        if self.player.center_y < HEIGHT / 2:
            camera_y = 2
        self.camera.move_to((camera_x, camera_y))
   

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.physics_engine.can_jump():
            self.player.change_y = 10
            self.jump_sound.play()
        # if symbol == arcade.key.S:
        #     self.player.change_y = -10
        if symbol == arcade.key.A:
            self.player.change_x = -23
        if symbol == arcade.key.D:
            self.player.change_x = 23


    def on_key_release(self, symbol: int, modifiers: int):
        # if symbol == arcade.key.W or symbol == arcade.key.S:
        #     self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0
        pass
        
if __name__ == "__main__":
    game = Window()
    arcade.run()