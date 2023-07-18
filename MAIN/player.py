import arcade
from entity import Entity

from constants import *

class Player(Entity):
    def __init__(self):
        super().__init__('Character', "owl")
        self.in_bounds = True
        # self.shaddow.texture. add opacity...
        self.idle_animating = False
        self.idle_odo = 1
        self.current_breathe_texture = 0
        self.active = False
        self.breathe_textures = []

        for i in range(9):
            idl = arcade.load_texture_pair(ROOT_FOLDER.joinpath( 'Character', f"owl_breathe{i}.png"))
            self.breathe_textures.append(idl)
    
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

    def handle_move_animation(self):
            self.idle_odo = 0
            self.idle_animating = False



    @property
    def out_of_bounds(self):
        return not self.in_bounds