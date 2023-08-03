
# Getting user input

Date: 07/06/2023



| Test Data                           | Expected                                                 | Observed                                                                                                         |
| ----------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Enemy speed                         | Enemy speed changes when set to different number         | I was able to see that the code worked and that there was a clear difference in speed when I changed it in tiled |
| No speed property                   | Key Error raised                                         | As expected                                                                                                      |
| Additional property set             | Property inexistant in tilemap, property not found error | Error occurs                                                                                                     |
| Class called not from tilemap token | Print my predetermined error message                     | As expected                                                                                                                 |
| No properties                       | Key Error raised                                         | Predetermined error message made                                                                                 | 

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

Date: 23/06/2023


| Test Data                    | Expected                                                                     | Observed                                                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Enemy tracking               | Enemy to track player as it moves along, changing both x, and y co-ordinates | I was able to see that the code worked and that there was a clear difference in speed when I changed it in tiled |
| Enemy center_x - targert > 0 | Enemy doesnt go towards player                                               | as expected                                                                                                      |
| Enemy has no chance x or y   | No movement                                                                  | Enemy doesnt follow player                                                                                       |
| No postive direction         | Enemy moves in one direction                                                 | As expected                                                                                                      |
| No speed property            | Error raised                                                                 | Error raised                                                                                                     | 



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