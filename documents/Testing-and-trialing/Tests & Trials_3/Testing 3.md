   _Name:_ Grace McDonald
# Getting user input

Date: 15/05/2023


```python
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Dont_touch'])
        # COLLIDING WITH Danger
        if colliding:
            if colliding and not self.player.jumping:
                self.score -= 1
                self.HUD['health'][-1].kill()
                self.player.change_x *= -1
                self.player.change_y *= -1
```

| Test Data                  | Expected                        | Observed                        |
| -------------------------- | ------------------------------- | ------------------------------- |
| Player hasn't been damaged | hearts remain at 5  | No change |
| Player touching danger | health set to 4, heart disappear | health became 4, heart disappered |
| Player loses heart | player y and x moves back -1 per hit of damage | As expected                     |

## Test 2 EXAMPLE:
# Getting user input

Date: 02/06/2023

```python
    def jump(self):
        self.jumping = True
        self.change_y = PLAYER_JUMP_SPEED
        self.acc_y = GRAVITY
        self.start_jump_y = self.center_y
    def update(self):
        super().update()
        if self.jumping:
            self.change_y += self.acc_y
            if self.center_y <= self.start_jump_y:
                self.jumping = False
                self.can_jump = True
                self.change_y = 0
                self.acc_y = 0
                self.start_jump_y = None
```

| Test Data                             | Expected                                               | Observed                          |
| ------------------------------------- | ------------------------------------------------------ | --------------------------------- |
| Character jumping                     | Character moves vertical with predetermined jump speed | As expected                       |
| Character jumps but gravity = 1       | Error raised                                           | Error seen                        |
| self.jumping = true                   | Character jumps                                        | Character moves vertical          |
| self.center <= self.start_jump_y      | No jump, no acceleration                               | As expected                       |
| self.change_y doesnt equal an integer | Error raised                                           | Game dosen't load and error occurs | 



