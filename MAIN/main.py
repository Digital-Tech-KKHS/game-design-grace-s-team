

# Different plugins
from tracemalloc import start
import arcade
import random
from pathlib import Path
from arcade.pymunk_physics_engine import PymunkPhysicsEngine

# where to get files from

ROOT_FOLDER = Path(__file__).parent
WIDTH = 1400
HEIGHT = 1000
TITLE = "Game"
STARTING_HEALTH = 5
PLAYER_JUMP_SPEED = 10
GRAVITY = -0.2
DEFAULT_FONT_SIZE = 20

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
    def __init__(self, foldername, filename):
        super().__init__(ROOT_FOLDER.joinpath(foldername, filename + "_idle.png"))
        self.walk_textures = []
        self.breathe_textures = []
        self.idle_textures = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, filename + "_idle.png"))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.jumping = False
        self.can_jump = True
        self.acc_y = 0
        self.odo = 0
        
        for i in range(10):
            tex = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, filename + f"_walk{i}.png"))
            self.walk_textures.append(tex)

        for i in range(14):
            idl = arcade.load_texture_pair (ROOT_FOLDER.joinpath(f"{foldername}", f"{filename}_breathe{i}.png"))
            self.breathe_textures.append(idl)
        
        self.start_jump_y = None
            
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

    # Character jumping:   
    def jump(self):
        self.jumping = True
        self.change_y = PLAYER_JUMP_SPEED
        self.acc_y = GRAVITY
        self.start_jump_y = self.center_y

    def update(self):
        super().update()
        # print(self.change_y)
        if self.jumping:
            self.change_y += self.acc_y
            if self.center_y <= self.start_jump_y: # caution not a good choice of logic
                self.jumping = False
                self.can_jump = True
                self.change_y = 0
                self.acc_y = 0
                self.start_jump_y = None
                print('landed')

class Enemy(Entity):
    def __init__(self, properties=None):
        super().__init__("Enemy", "enemy")
        print(properties)
        if properties is not None:
            for key, value in properties.items():
                setattr(self, key, value)

        try:
            self.speed
        except: # fix this!
            raise KeyError("enemy without speed custom property found. Check tilemap")
        self.target = (0, 0)

        self.in_bounds = True
        # self.shaddow.texture. add opacity...

    @property
    def out_of_bounds(self):
        return not self.in_bounds
    
    def update(self):
        super().update()
        if self.center_x - self.target[0] < 0:
            self.change_x = self.speed 
        if self.center_x - self.target[0] > 0:
            self.change_x = -self.speed 
        if self.center_y - self.target[1] < 0:
            self.change_y = self.speed 
        if self.center_y - self.target[1] > 0:
            self.change_y = -self.speed 

    
    def set_target(self, x, y):
        self.target = (x, y)




class Player(Entity):
    def __init__(self):
        super().__init__('Character', "owl")
        self.in_bounds = True
        # self.shaddow.texture. add opacity...
        self.idle_animating = False
        self.idle_odo = 1
        self.current_breathe_texture = 0
        self.active = False

    def update_animation(self):
        super().update_animation()

        if self.change_x == 0:
            if self.idle_animating:
                self.texture = self.breathe_textures[self.current_breathe_texture][self.face_direction]
                self.idle_odo += 1
                if self.idle_odo % 4 == 0: 
                    self.current_breathe_texture += 1600
                    if self.current_breathe_texture >= 4:
                        self.idle_animating = False
                        self.idle_odo = 0
                        self.current_breathe_texture = 0

            else:
                self.texture = self.idle_textures[self.face_direction]
                self.idle_odo += 1
                if self.idle_odo >= 160:
                    self.idle_animating  = True 
        else:
            self.idle_odo = 0
            self.current_blink_texture = 0
            self.adle_animating = False




    @property
    def out_of_bounds(self):
        return not self.in_bounds


    

class GameView(arcade.View): 
    def __init__(self):
        super().__init__()
        # arcade.set_background_color(arcade.color.BURNT_UMBER)
        # def on_show_view(self):
        self.player = None
        self.tilemap = None
        self.enemy = None
        self.scene = None
        # self.walls = None
        self.HUD = None
        self.physics_engine = None
        self.camera = None
        self.HUD_camera = None
        self.score = 0
        self.level = 0
        self.background = None
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        self.setup()
    
    
    def setup(self):
        # where the character spawns in and which map it uses
        self.player = Player()
        self.player.center_x = 100
        self.player.center_y = 500

        self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(F'Map_{self.level}.tmx'))
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene["Water"], gravity_constant=0)
        #self.physics_engine = PymunkPhysicsEngine(gravity=gravity)
        
        self.camera = arcade.Camera()
        self.HUD_camera = arcade.Camera()
        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
        
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        
        self.scene.move_sprite_list_after('Foreground', 'player',)
        self.scene.add_sprite_list('shadows')
        
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        
        # self.enemy = Enemy()
        # self.player.center_x = 100
        # self.player.center_y = 500


        # Adds in health with my own made health art
        for i in range(STARTING_HEALTH):
            x = 25 + 60 * i
            y = HEIGHT - 40
            grass = arcade.Sprite(ROOT_FOLDER.joinpath('health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(grass)
            # health = [0, 1, 2, 3, 4]

        self.shaddow = arcade.Sprite(ROOT_FOLDER / 'Character' / 'shaddow.png')
        self.scene.add_sprite_list_before('shaddow', 'player')
        self.scene.add_sprite_list_before('Enemies', 'player')

        self.scene.add_sprite('shaddow', self.shaddow)

        for enemy in self.scene["Enemy_tokens"]:
            new_enemy = Enemy(enemy.properties)
            new_enemy.center_x = enemy.center_x
            new_enemy.center_y = enemy.center_y
            self.scene["Enemies"].append(new_enemy)
            enemy.kill()

    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath('background2.png'))

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
        

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Text'])
        if colliding:
            arcade.draw_text("This looks dangerous....",
             570, 340, arcade.color.WHITE, 20, 0, "left", "merlin")





# FOR SPRITE ON COINS
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()

        
        self.physics_engine.update()
        if not self.player.jumping: # THIS IS A BAD IDEA
            self.physics_engine.update()
        self.scene.update()
        for coin in self.scene['Coins']:
            coin.on_update()
        self.center_camera_on_player()
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Coins'])
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
        
        self.shaddow.center_x = self.player.center_x + 20
        if not self.player.jumping:
            self.shaddow.center_y = self.player.center_y - 85
            self.shaddow.scale = 1
        else:
            self.shaddow.scale += self.player.change_y * -0.005
        # self.player.in_bounds = arcade.check_for_collision_with_list(self.player, self.scene['background'])
        
        
        # making my dragon spawn at the start and lose health when it falls off of map
        
        
        # colliding = arcade.check_for_collision_with_list(self.player, self.scene['CANT_TOUCH'])
        # # COLLIDING WITH BACKDROP
        # if colliding:
        #     self.player.change_x = -1 + 1
        #     self.player.change_y = -1 + 1
        

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Dont_touch'])
        # COLLIDING WITH Danger
        if colliding:
            if colliding and not self.player.jumping:
                self.score -= 1
                self.HUD['health'][-1].kill()
                self.player.change_x *= -1
                self.player.change_y *= -1
                
            
        
            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Coins'])

        if colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Win'])
        if colliding:
            self.level += 1
            self.setup()


            

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Change'])
        if colliding:
            self.level = 2
            self.setup()

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Original_layer'])
        if colliding:
            self.level = 0
            self.setup()

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Winner'])
        if colliding:
            self.window.show_view(self.window.win_view)
            self.setup()

        for enemy in self.scene["Enemies"]:
            enemy.set_target(self.player.center_x, self.player.center_y)

    def center_camera_on_player(self):
        camera_x = self.player.center_x - WIDTH / 2
        camera_y = self.player.center_y - HEIGHT / 2
       
        if self.player.center_x < WIDTH / 2:
            camera_x = 2
        if self.player.center_y < HEIGHT / 2:
            camera_y = 2
        self.camera.move_to((camera_x, camera_y))


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE: # and self.physics_engine.can_jump():
            self.player.change_y = 10
            self.jump_sound.play()
        # if symbol == arcade.key.G:

        if symbol == arcade.key.W:
            self.player.change_y = 4
        if symbol == arcade.key.S:
            self.player.change_y = -4
        if symbol == arcade.key.A:
            self.player.change_x = -5
        if symbol == arcade.key.D:
            self.player.change_x = 5
        if symbol == arcade.key.SPACE:
            self.player.jump()
        #     shadow = arcade.SpriteSolidColor(32, 32, (0, 0, 0))
        #     shadow.center_x = self.player.center_x
        #     shadow.center_y = self.player.center_y - 32
        #       self.scene['shadows'].append(shadow)
        #     if key == arcade.key.UP or key == arcade.key.W:
        #     if self.physics_engine.can_jump():
        #       self.player_sprite.change_y = PLAYER_JUMP_SPEED
        #       self.jump_sound.play()
        if not self.player.jumping:
            if symbol == arcade.key.W:
                self.player.change_y = 4
            if symbol == arcade.key.S:
                self.player.change_y = -4
            if symbol == arcade.key.A:
                self.player.change_x = -2.8
            if symbol == arcade.key.D:
                self.player.change_x = 2.8
            

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0
        # pass
        # if not self.player.jumping:
        # if symbol == arcade.key.SPACE:
        #     self.player.change_y = 0
        # if symbol == arcade.key.W or symbol == arcade.key.S:
        #     self.player.change_y = 0aa
        #     self.player.change_x = 0
        # if symbol == arcade.key.A or symbol == arcade.key.D:
        #     self.player.change_x = 0
        #     self.player.change_y = 0

if __name__ == "__main__":
    game = Window()
    arcade.run()