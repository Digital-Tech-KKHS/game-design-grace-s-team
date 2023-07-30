import arcade
from entity import Entity
from constants import *

# Makes player class
class Player(Entity):
    def __init__(self):
        super().__init__('Character', "owl")
        self.in_bounds = True
        self.idle_animating = False
        self.idle_odo = 1
        self.current_breathe_texture = 0
        self.active = False
        self.breathe_textures = []

        # Gets character breathe texture
        for i in range(9):
            idl = arcade.load_texture_pair(ROOT_FOLDER.joinpath( 'Character', f"owl_breathe{i}.png"))
            self.breathe_textures.append(idl)
    
    # Code for characters idle animation function
    def handle_idle_animation(self):
        if self.idle_animating:
            self.idle_odo += 1
            if self.idle_odo % 10 == 0: 
                self.current_breathe_texture += 1
                if self.current_breathe_texture >= len(self.breathe_textures):
                    self.idle_animating = False
                    self.idle_odo = 0
                    self.current_breathe_texture = 0
                    return 
                self.texture = self.breathe_textures[self.current_breathe_texture][self.face_direction]

        else:
            self.texture = self.idle_textures[self.face_direction]
            self.idle_odo += 1
            if self.idle_odo >= 160:
                self.idle_animating  = True 
                self.current_breathe_texture = 0
                self.texture = self.breathe_textures[self.current_breathe_texture][self.face_direction]

    # Character jumping:   
    def jump(self):
        self.jumping = True
        self.change_y = PLAYER_JUMP_SPEED
        self.acc_y = GRAVITY
        self.start_jump_y = self.center_y

    def update(self):
        super().update()
        if self.jumping:
            self.change_y += self.acc_y
            if self.center_y <= self.start_jump_y: # caution not a good choice of logic
                self.jumping = False
                self.can_jump = True
                self.change_y = 0
                self.acc_y = 0
                self.start_jump_y = None


    @property
    def out_of_bounds(self):
        return not self.in_bounds