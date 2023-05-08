

# Different plugins
from tracemalloc import start
import arcade
import random
from pathlib import Path
from arcade.pymunk_physics_engine import PymunkPhysicsEngine

# where to get files from

ROOT_FOLDER = Path(__file__).parent
WIDTH = 1490
HEIGHT = 1000
TITLE = "Game"
STARTING_HEALTH = 5
PLAYER_JUMP_SPEED = 10
GRAVITY = -0.2

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
        super().__init__(ROOT_FOLDER.joinpath(foldername, "owl_idle.png"))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, "owl_idle.png"))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.jumping = False
        self.can_jump = True
        self.acc_y = 0
        self.odo = 0
        for i in range(10):
            tex = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, f"owl_walk{i}.png"))
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

    # Character jumping:   
    def jump(self):
        self.jumping = True
        self.change_y = PLAYER_JUMP_SPEED
        self.acc_y = GRAVITY

    def update(self):
        # print(self.change_y)
        if self.jumping:
            self.change_y += self.acc_y
            if self.change_y <= -PLAYER_JUMP_SPEED: # caution not a good choice of logic
                self.jumping = False
                self.can_jump = True
                self.change_y = 0
                self.acc_y = 0
        super().update()

class Player(Entity):
    def __init__(self, foldername):
         super().__init__(foldername)
         self.in_bounds = True
    @property
    def out_of_bounds(self):
        return not self.in_bounds

# class Enemy(Entity):
#     def __init__(self, foldername):
#         super().__init__(foldername)`
#         self.walk_textures = []
#         self.idle_textures = arcade.load_texture_pair(ROOT_FOLDER.joinpath (foldername, "Enemy.png"))
#         self.face_direction = 0
#         self.current_texture = 0
#         self.cur_texture_index = 0
    
class GameView(arcade.View): 
    def __init__(self):
        super().__init__()
        # arcade.set_background_color(arcade.color.BURNT_UMBER)
        # def on_show_view(self):
        self.player = None
        self.tilemap = None
        self.enemy_list = None
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
        self.player = Player('Character')
        self.player.center_x = 35
        self.player.center_y = 100
        self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(F'Map_{0}.tmx'))
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene["water"], gravity_constant=0)
        self.camera = arcade.Camera(WIDTH, HEIGHT)
        self.HUD_camera = arcade.Camera(WIDTH, HEIGHT)
        self.HUD = arcade.Scene() 
        self.enemy_list = arcade.SpriteList()   
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        self.scene.move_sprite_list_after('Foreground', 'player',)
        self.scene.add_sprite_list('shadows')
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        # self.wall_list = arcade.SpriteList()


        # Adds in health with my own made health art
        for i in range(STARTING_HEALTH):
            x = 25 + 60 * i
            y = HEIGHT - 40
            grass = arcade.Sprite(ROOT_FOLDER.joinpath('health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(grass)
            # health = [0, 1, 2, 3, 4]
            # index = health.index[ health-1 ]

        # -- Draw an enemy on the ground
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png")

        enemy.bottom = 34
        enemy.left = 34 * 2

        # Set enemy initial speed
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Draw a enemy on the platform
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png")

        enemy.bottom = 34 * 4
        enemy.left = 34 * 4

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 34 * 8
        enemy.boundary_left = 34 * 3
        enemy.change_x = 2
        self.enemy_list.append(enemy)

    def on_draw(self):
        # adding back round for game view   
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.camera.use()
        self.scene.draw()
        # self.player.draw_hit_box((255, 0,0,255), 2)
        self.HUD_camera.use()
        self.HUD.draw()
        # self.wall_list.draw()
        # self.wall_list.draw()
        arcade.draw_text(f"Coins: {self.score}", WIDTH-100, HEIGHT-50)

    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath('background2.png'))




# FOR SPRITE ON COINS
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()
        self.physics_engine.update()
        if not self.player.jumping: # THIS IS A BAD IDEA
            self.physics_engine.update()
        self.scene.update()
        
        # Coins
        for coin in self.scene['coins']:
            coin.on_update()
        self.center_camera_on_player()
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['coins'])
        for coin in colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()
        # Health
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['DONT_TOUCH'])
        if self.player.center_y <0:
            self.HUD['health'][-1].kill()
            self.player.center_x = 40
            self.player.center_y = 1000
            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)
        # self.player.in_bounds = arcade.check_for_collision_with_list(self.player, self.scene['background'])
        
        
        # making my dragon spawn at the start and lose health when it falls off of map
        
        
        # colliding = arcade.check_for_collision_with_list(self.player, self.scene['CANT_TOUCH'])
        # # COLLIDING WITH BACKDROP
        # if colliding:
        #     self.player.change_x = -1 + 1
        #     self.player.change_y = -1 + 1 
        
        # Enemy:
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

        
       



        # COLLIDING WITH FIRE
        if colliding:
            if colliding and not self.player.jumping:
                self.score -= 1
                self.HUD['health'][-1].kill()
                self.player.change_x *= -0.9
                self.player.change_y *= -0.9
        
            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['coins'])

        if colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()
        
       
        # # COLLIDING WITH BACKDROP
        # colliding = arcade.check_for_collision_with_list(self.player, self.scene['CANT_TOUCH'])
        # if colliding:
        #     self.player.change_x = 0
        #     self.player.change_y = 0

        # colliding with win tile and changing level
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['WIN'])
        if colliding:
            self.level += 1
            self.setup()

        # colliding with winner tile to create a win_view
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

    # Pressing keys
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE: # and self.physics_engine.can_jump():
            self.player.change_y = 10
            self.jump_sound.play()
        if symbol == arcade.key.W:
            self.player.change_y = 4
        if symbol == arcade.key.S:
            self.player.change_y = -4
        if symbol == arcade.key.A:
            self.player.change_x = -4
        if symbol == arcade.key.D:
            self.player.change_x = 4
        if symbol == arcade.key.SPACE:
            self.player.jump()
            shadow = arcade.SpriteSolidColor(32, 32, (0, 0, 0))
            shadow.center_x = self.player.center_x
            shadow.center_y = self.player.center_y - 32
            # self.scene['shadows'].append(shadow)
        # if key == arcade.key.UP or key == arcade.key.W:
        #      if self.physics_engine.can_jump():
        #          self.player_sprite.change_y = PLAYER_JUMP_SPEED
        #     self.jump_sound.play()
        if not self.player.jumping:
            if symbol == arcade.key.W:
                self.player.change_y = 4
            if symbol == arcade.key.S:
                self.player.change_y = -4
            if symbol == arcade.key.A:
                self.player.change_x = -2.8
            if symbol == arcade.key.D:
                self.player.change_x = 2.8
    #   When keys are released
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0
        pass
        if not self.player.jumping:
            if symbol == arcade.key.SPACE:
                self.player.change_y = 0
            if symbol == arcade.key.W or symbol == arcade.key.S:
                self.player.change_y = 0
                self.player.change_x = 0
            if symbol == arcade.key.A or symbol == arcade.key.D:
                self.player.change_x = 0
                self.player.change_y = 0

if __name__ == "__main__":
    game = Window()
    arcade.run()