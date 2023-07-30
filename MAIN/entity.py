import arcade
from constants import *
class Entity(arcade.Sprite):
    
    # Characteristics that both the player and enemy can call from
    def __init__(self, foldername, filename):
        super().__init__(ROOT_FOLDER.joinpath( foldername, filename + "_idle.png"))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(ROOT_FOLDER.joinpath(foldername, filename + "_idle.png"))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.jumping = False
        self.can_jump = True
        self.acc_y = 0
        self.odo = 0
        
        for i in range(10):
            tex = arcade.load_texture_pair(ROOT_FOLDER.joinpath( foldername, filename + f"_walk{i}.png"))
            self.walk_textures.append(tex)
        self.start_jump_y = None
            
    # Updates idle and move animations
    def update_animation(self):
        if self.change_x > 0:
             self.face_direction = 1
        if self.change_x < 0:
             self.face_direction = 0
        
        if self.change_x == 0:
            self.handle_idle_animation()
        else:
            self.handle_move_animation()

    # Sets idle animation
    def handle_idle_animation(self):
        self.texture = self.idle_textures[self.face_direction]
    
    #  Sets idle animation
    def handle_move_animation(self):
        self.texture = self.walk_textures[self.current_texture][self.face_direction]
        self.odo += 1
        if self.odo % 4 ==0:
            self.current_texture += 1
            self.current_texture = self.current_texture % 10


