
# Getting user input

Date: 22/03/2023



```python
self.tilemap = arcade.load_tilemap(ROOT_FOLDER.joinpath(F'Map_{self.level}.tmx'))

        self.scene = arcade.Scene.from_tilemap(self.tilemap)
```

| Test Data                        | Expected                                    | Observed                         |
| -------------------------------- | ------------------------------------------- | -------------------------------- |
| Loading in Tilemap               | Map called "Map_0" loads up onto the screen | "Map_0" loaded up onto game_view |
| Tilemap changes to different map | Tile map to + 1 each cycle                  | New map is created               |
|                                  |                                             |                                  |
## Test 2 EXAMPLE:
# Getting user input

Date: 03/04/2023

```python

```

| Test Data                  | Expected                        | Observed                        |
| -------------------------- | ------------------------------- | ------------------------------- |
| Player not touching enemy  | nothing                         | nothing                         |
| Player touching health = 3 | health set to 2, heart disapear | health became 2, heart remained |
| Player touching health = 1 | Game restarts                   | As expected                     |
|                            |                                 |                                 |
|                            |                                 |                                 |



