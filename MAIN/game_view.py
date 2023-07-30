import arcade
from constants import *
from player import Player
from enemy import Enemy

# Making main class "Gameview"
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
    
    # Game set up 
    def setup(self):
        
        # where the character spawns in and which map it uses
        self.player = Player()
        self.player.center_x = 100
        self.player.center_y = 500

        self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(F'Map_{self.level}.tmx'))
        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene["Water"], gravity_constant=0)
        
        self.camera = arcade.Camera()
        self.HUD_camera = arcade.Camera()
        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
        
        # Characteristic sounds
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin4.wav')
        self.jump_sound = arcade.load_sound(':resources:sounds/phaseJump1.wav')
        
        self.scene.move_sprite_list_after('Foreground', 'player',)
        self.scene.add_sprite_list('shadows')
        
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        

        self.shaddow = arcade.Sprite(ROOT_FOLDER.joinpath(  'Character' , 'shaddow.png'))
        self.scene.add_sprite_list_before('shaddow', 'player')
        self.scene.add_sprite_list_before('Enemies', 'player')

        self.scene.add_sprite('shaddow', self.shaddow)


        # Adds in health and my health bar icons that I made
        for i in range(STARTING_HEALTH):
            x = 25 + 60 * i
            y = HEIGHT - 40
            health = arcade.Sprite(ROOT_FOLDER.joinpath("Assets",'health.png'), 0.5, center_x=x, center_y=y)
            self.HUD['health'].append(health)
            # health = [0, 1, 2, 3, 4]

        
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
        
        arcade.draw_text(f"Feathers: {self.score}", WIDTH-150, HEIGHT-50)
        

        # Text my npc will say about the point of the game, on my first level
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Text'])
        if colliding:
            arcade.draw_text("Hello adventurer! I am emmy,",
             220, 550, arcade.color.WHITE, 20, 0)
            
            arcade.draw_text("your goal is too collect feathers",
             220, 520, arcade.color.WHITE, 20, 0)
            
            arcade.draw_text("throughout the levels so that ",
             220, 490, arcade.color.WHITE, 20, 0)
            
            arcade.draw_text("you can get your wings back!",
             220, 460, arcade.color.WHITE, 20, 0)

        # Text my npc will say about the point of feathers
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Feather_Text'])
        if colliding:
            arcade.draw_text("You must find Feathers like these,",
             770, 550, arcade.color.WHITE, 20, 0)
            
            arcade.draw_text("collect all feathers to unlock wings",
             770, 520, arcade.color.WHITE, 20, 0)
            
            arcade.draw_text("and be free.",
             770, 490, arcade.color.WHITE, 20, 0)






        # Function for things to update in this view
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()
        self.physics_engine.update()
        
        if not self.player.jumping:
            self.physics_engine.update()
        self.scene.update()
       
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
                self.HUD['health'][-1].kill()
                self.player.change_x *= -2
                self.player.change_y *= -2
                
            

        # Player finishes levels and goes to "WinView"
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Win'])
        if colliding:
            self.level += 1
            self.setup()


            
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
        if colliding:
            self.window.show_view(self.window.win_view)
            self.setup()

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
        
    #    INTERACTABLES.....
        if symbol == arcade.key.ENTER:
            self.handle_interact()

    def handle_interact(self):
            interactables = arcade.check_for_collision_with_list(self.player, self.scene["interactables"])
            for interactable in interactables:
                getattr(self, interactable.properties["on_interact"])(interactable)

    def toggle_lever(self, interactable):
            levers = (l for l in self.scene["interactables"] if l.properties["type"] == "lever")
            toggled = not interactable.properties["toggled"]
            for lever in levers:
                lever.properties["toggled"] = toggled
                if toggled:
                    lever.texture = arcade.load_texture(ROOT_FOLDER.joinpath("Assets", f"LeverLeft.png"))
                else:
                    lever.texture = arcade.load_texture(ROOT_FOLDER.joinpath("Assets", f"Leverright.png"))

            
        # When a key is released the character will stop moving
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0