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

```

| Test Data                  | Expected                        | Observed                        |
| -------------------------- | ------------------------------- | ------------------------------- |
| Player not touching enemy  | nothing                         | nothing                         |
| Player touching health = 3 | health set to 2, heart disapear | health became 2, heart remained |
| Player touching health = 1 | Game restarts                   | As expected                     |
|                            |                                 |                                 |
|                            |                                 |                                 |



