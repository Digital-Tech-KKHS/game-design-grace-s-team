import arcade
from constants import *
from player import Player
from enemy import Enemy
import time
import math

# Making main class "Gameview"
class GameView(arcade.View): 
    def __init__(self):
        super().__init__()
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

        self.music = arcade.Sound((ROOT_FOLDER.joinpath("Assets", "Main_Song.mp3")), streaming = True)
        self.setup()
    
    def play_song(self):
        self.music.play(3,0,True)
        
    # def on_show_view(self):
    #     self.play_song()
    
    
    
    # Game set up 
    
    
    def setup(self):
        
        # where the character spawns in and which map it uses
        self.player = Player()
        self.player.center_x = 100
        self.player.center_y = 500

        self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(F'Map_{self.level}.tmx'))
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        
        
        
        self.camera = arcade.Camera()
        self.HUD_camera = arcade.Camera()
        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
        
        # Characteristic sounds
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        
        
        
        self.current_song_index = 0
        
        
        self.scene.move_sprite_list_after('Foreground', 'player',)
        self.scene.add_sprite_list('shadows')
        
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        

        self.shaddow = arcade.Sprite(ROOT_FOLDER.joinpath(  'Character' , 'shaddow.png'))
        self.scene.add_sprite_list_before('shaddow', 'player')
        self.scene.add_sprite_list_before('Enemies', 'player')

        self.scene.add_sprite('shaddow', self.shaddow)

        # self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, , gravity_constant=0)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, walls=self.scene["Water"],
            platforms=self.scene[LAYER_NAME_MOVING_PLATFORMS],
            gravity_constant= 0,
            ladders=self.scene[LAYER_NAME_LADDERS],
        )

        # Adds in health and my health bar icons that I made
        for i in range(STARTING_HEALTH):
            x = 25 + 60 * i
            y = HEIGHT - 40
            health = arcade.Sprite(ROOT_FOLDER.joinpath("Assets",'health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(health)

        
        # Enemy in scene in tile map
        for enemy in self.scene["Enemy_tokens"]:
            new_enemy = Enemy(enemy.properties)
            new_enemy.center_x = enemy.center_x
            new_enemy.center_y = enemy.center_y
            self.scene["Enemies"].append(new_enemy)
            enemy.kill()

        for enemy in self.scene["Enemy_tokens"]:
            new_enemy = Enemy(enemy.properties)
            new_enemy.center_x = enemy.center_x
            new_enemy.center_y = enemy.center_y
            self.scene["Enemies"].append(new_enemy)
            enemy.kill()

        # # For enemy seek
        # for enemy in self.scene['Enemy_tokens']:
        #     dx = self.player.center_x - enemy.center_x
        #     dy = self.player.center_y - enemy.center_y
        #     theta = math.atan2(dy,dx)
            
        #     if math.dist(self.player.position, enemy.position) < 100:
        #         enemy.change_x = math.cos(theta)*enemy.speed
        #         enemy.change_y = math.sin(theta)*enemy.speed
        #     else: 
        #         enemy.change_x = 0
        #         enemy.change_y = 0
                                

        # Background
    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath("Assets",'background2.png'))

        # Draw functions
    def on_draw(self):
        # adding back round for game view   
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.camera.use()
        self.scene.draw()
        self.HUD_camera.use()
        self.HUD.draw()
        
        arcade.draw_text(f"Feathers: {self.score}", WIDTH-150, HEIGHT-50, arcade.color.WHITE, 18, 0, "left", "arial", True)
        

        # Text my npc will say about the point of the game, on my first level
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Text'])
        if colliding:
            arcade.draw_text("Hello little owl....",
             200, 550, arcade.color.WHITE, 22, 0,"left", "calibri", True)
            
            arcade.draw_text("Your goal is too collect feathers",
             200, 520, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("throughout the levels and survive. ",
             200, 490, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("If you die little owl,",
             200, 460, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("you will be forced to start over... ",
             200, 430, arcade.color.WHITE, 22, 0, "left", "calibri", True)

        # Text my npc will say about the point of feathers
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Feather_Text'])
        if colliding:
            arcade.draw_text("You must find... ",
             780, 580, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("At least 10 feathers like these,",
             780, 550, arcade.color.WHITE, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("to get your ability to fly back,",
             780, 520, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("to escape from this place and be free....",
             780, 490, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Bonus_Feather_Text'])
        if colliding:
            arcade.draw_text("Be on the look out for a bonus feather, ",
             400, 750, arcade.color.BLACK, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("it fills your hearts up and adds an extra one, ",
            
             400, 720, arcade.color.WHITE, 22, 0, "left", "calibri", True)
            
            arcade.draw_text("as well as 5 feathers..However it's quite well hidden.. ",
             400, 690, arcade.color.BLACK, 22, 0, "left", "calibri", True)






        # Function for things to update in this view
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()
        self.physics_engine.update()
        
        if not self.player.jumping:
            self.physics_engine.update()
        self.scene.update()

# Update walls, used with moving platforms
        self.scene.update([LAYER_NAME_MOVING_PLATFORMS])
        
       
        for coin in self.scene['Feather']:
            coin.on_update()
        self.center_camera_on_player()
        
        # Collison with coin adding to score and then deleting from map
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Feather'])
        for coin in colliding:
            coin.kill()
            self.score += 1
            self.collect_coin_sound.play()

            if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)
        
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Bonus_feather'])
        for coin in colliding:
            coin.kill()
            self.score += 5
            STARTING_HEALTH + 1
            health = arcade.Sprite(ROOT_FOLDER.joinpath("Assets",'health.png'), 0.5, center_x= 326, center_y=960)
            self.HUD['health'].append(health)
            self.collect_coin_sound.play()

        # Draws shadow on characters center
        self.shaddow.center_x = self.player.center_x + 20
        if not self.player.jumping:
            self.shaddow.center_y = self.player.center_y - 85
            self.shaddow.scale = 1
        else:
            self.shaddow.scale += self.player.change_y * -0.005

        # Damage to player when colliding
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Dont_touch'])
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_x *= -1
                self.player.change_y *= -1
                self.HUD['health'][-1].kill()
        # if health == EndView / ending screen will appear
        if self.player.center_y <0:
            self.HUD['health'][-1].kill()  
            self.player.center_x = 40
            self.player.center_y = 1000
        if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)

        # Speed potion (topright)
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_topright"])
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = 6
                self.player.change_x = 6

        #  Speed potion (topleft)       
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_topleft"])
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = 6
                self.player.change_x = -6

        #  Speed potion (bottemright) 
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_bottemright"])
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = -6
                self.player.change_x = 6

         #  Speed potion (bottemleft)        
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_bottemleft"])
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = -6
                self.player.change_x = -6
                
        # Player collides with an enemy and loses "health"
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Enemies'])
        if colliding:
            if colliding: 
                self.player.change_x *= -2
                self.player.change_y *= -2
                self.HUD['health'][-1].kill()
        # if health == EndView / ending screen will appear        
        if self.player.center_y <0:
            self.HUD['health'][-1].kill()  
            self.player.center_x = 40
            self.player.center_y = 1000
        if len(self.HUD['health']) == 0:
                self.window.show_view(self.window.end_view)

        # Player finishes levels and goes to "WinView"
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Next_level'])
        if colliding:
            self.level += 1
            self.setup(  )


            
        # colliding = arcade.check_for_collision_with_list(self.player, self.scene['to_level_1'])
        # if colliding:
        #     self.level = 1
        #     self.setup()
         
        #  Changes to Map_2 when colliding
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['to_level_2'])
        if colliding:
            self.level = 2
            self.setup()

        #  Changes to Map_3 when colliding
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['to_level_3'])
        if colliding:
            print("colliding")
            self.level = 3
            self.setup()
        
        # Changes to original layor when colliding
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Original_layer'])
        if colliding:
            self.level = 0
            self.setup() 

        # When colliding with Winner tile "Win_view" will appear
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Winner'])
        
        if self.level == 3 and self.score >= 10:
            if colliding:
                self.window.show_view(self.window.win_view)


        for enemy in self.scene["Enemies"]:
            enemy.set_target(self.player.center_x, self.player.center_y)
        
        # Centers camera onto player 
    def center_camera_on_player(self):
        camera_x = self.player.center_x - WIDTH / 2
        camera_y = self.player.center_y - HEIGHT / 2
       
        if self.player.center_x < WIDTH / 2:
            camera_x = 2
        if self.player.center_y < HEIGHT / 2:
            camera_y = 2
        self.camera.move_to((camera_x, camera_y))

        # When a key is pressed the character will move a certain amount in a specific direction
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 10
            self.jump_sound.play()
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
  
        if not self.player.jumping:
            if symbol == arcade.key.W:
                self.player.change_y = 4
            if symbol == arcade.key.S:
                self.player.change_y = -4
            if symbol == arcade.key.A:
                self.player.change_x = -2.8
            if symbol == arcade.key.D:
                self.player.change_x = 2.8
            
        # When a key is released the character will stop moving
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0