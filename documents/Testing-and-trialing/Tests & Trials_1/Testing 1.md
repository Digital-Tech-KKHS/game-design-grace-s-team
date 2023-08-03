
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
| Calls scene                      | Map from tiled is set to current scene      | Map is added                              |
## Test 2 EXAMPLE:
# Getting user input
  

Date: 03/04/2023

```python
# Main class

class Window(arcade.Window):
    # identifys classes
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.start_view = StartView()
        self.game_view = GameView()
        self.end_view = EndView()
        self.win_view = WINView()
        self.show_view(self.start_view)
```

| Test Data                | Expected                              | Observed              |
| ------------------------ | ------------------------------------- | --------------------- |
| No call to StartView     | Error raised                          | Error loaded          |
| EndView called           | Set game to EndView                   | as expected           |
| Calls window             | Window drawn                          | As expected           |
| Make GameView class open | class loads on screen after StartView | GameView class loaded | 





