import arcade
from constants import *
class Entity(arcade.Sprite):
    # Character
    def __init__(self, foldername, filename):
        super().__init__(ROOT_FOLDER.joinpath( foldername, filename + "_idle.png"))
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
            tex = arcade.load_texture_pair(ROOT_FOLDER.joinpath ( foldername, filename + f"_walk{i}.png"))
            self.walk_textures.append(tex)

        for i in range(8):
            idl = arcade.load_texture_pair (ROOT_FOLDER.joinpath( f"{foldername}", f"{filename}_breathe{i}.png"))
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
