import arcade
from entity import Entity

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
       
        # if self.target.change_x == 0:
        #     if -200 < self.target.center_x - 

    
    def set_target(self, x, y):
        self.target = (x, y)

    def update_animation(self):
        if self.center_x > self.target:
             self.face_direction = 1
        if self.center_x < self.target:
             self.face_direction = 0
