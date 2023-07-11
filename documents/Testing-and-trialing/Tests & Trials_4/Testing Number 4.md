
# Getting user input

Date: 
23/06/2023

| Test Data                           | Expected                                         | Observed                                                                                                         |
| ----------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Enemy speed                         | Enemy speed changes when set to different number | I was able to see that the code worked and that there was a clear difference in speed when I changed it in tiled |
| No speed property                   | Key Error raised                                 |                                                                                                                  |
| additional property set             |                                                  |                                                                                                                  |
| Class called not from tilemap token | print my predetermined error message                                               |                                                                                                                  |
| No properties                       | Key Error raised                                                 |                                                                                                                  |

```python
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
```



## Test 2 EXAMPLE:
# Getting user input

Date: 26/06/2023


| Test Data    | Expected                                        | Observed                        |
| -------------| ------------------------------------------------| ------------------------------- |
| Enemy tracking | Enemy to track player as it moves along, changing both x, and y co-ordinates| I was able to see that the code worked and that there was a clear difference in speed when I changed it in tiled



``````python

```
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