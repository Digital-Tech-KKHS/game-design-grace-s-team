import arcade
from constants import *
from player import Player
from enemy import Enemy
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
            health = arcade.Sprite(ROOT_FOLDER.joinpath("Assets",'health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(health)
            # health = [0, 1, 2, 3, 4]

        self.shaddow = arcade.Sprite(ROOT_FOLDER.joinpath(  'Character' , 'shaddow.png'))
        self.scene.add_sprite_list_before('shaddow', 'player')
        self.scene.add_sprite_list_before('Enemies', 'player')

        self.scene.add_sprite('shaddow', self.shaddow)

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

    def on_show_view(self):
        self.background = arcade.load_texture(ROOT_FOLDER.joinpath("Assets",'background2.png'))

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
             570, 340, arcade.color.WHITE, 20, 0)





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


        # SPEED POWERUPS..............
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_topright"])
        # Speed
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = 6
                self.player.change_x = 6

                
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_topleft"])
        # Speed
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = 6
                self.player.change_x = -6

        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_bottemright"])
        # Speed
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = -6
                self.player.change_x = 6

                
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["Speed_boost_bottemleft"])
        # Speed
        if colliding:
            if colliding and not self.player.jumping:
                self.player.change_y = -6
                self.player.change_x = -6

                
                
                
                
            
            
                
        # Ememy DAMAGE:
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Enemy_tokens'])
        # COLLIDING WITH Danger
        if colliding:
            if colliding:
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