import arcade
from entity import Entity
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
                if self.idle_odo % 10 == 0: 
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