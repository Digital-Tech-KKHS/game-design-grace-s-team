import arcade
from entity import Entity

# makes enemy class
class Enemy(Entity):
    def __init__(self, properties=None):
        super().__init__("Enemy", "enemy")
       
        # Making speed properties of enemy
        if properties is not None:
            for key, value in properties.items():
                setattr(self, key, value)

        try:
            self.speed
        except:
            raise KeyError("enemy without speed custom property found. Check tilemap")
        self.target = (0, 0)

        self.in_bounds = True

    @property
    def out_of_bounds(self):
        return not self.in_bounds
    
    # Making player tracker for enemy
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
       

    def set_target(self, x, y):
        self.target = (x, y)

    def update_animation(self):
        if self.change_x > 0:
             self.face_direction = 1
        if self.change_x < 0:
             self.face_direction = 0
