_Name:_ Grace McDonald
# Getting user input

Date: 26/04/2023



```python
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 10
            self.jump_sound.play()
        if symbol == arcade.key.W:
            self.player.change_y = 4
        if symbol == arcade.key.S:
            self.player.change_y = -4
        if symbol == arcade.key.A:
            self.player.change_x = -5
        if symbol == arcade.key.D:
            self.player.change_x = 5
        if symbol == arcade.key.SPACE:
            self.player.jump()
```

| Test Data         | Expected                  | Observed                              |
| ----------------- | ------------------------- | ------------------------------------- |
| Key D not pressed | nothing                   | nothing                               |
| Key A pressed     | players' x -5             | Character moves left                  |
| No keys pressed   | Character has no movement | As expected                           |
| Key pressed       | Searches for key chosen   | character moves according to that key |
## Test 2 EXAMPLE:
# Getting user input

Date: 08/05/2023

```python
def on_key_press(self, symbol:int, modifiers:int):
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)```
        

| Test Data                  | Expected                        | Observed                        |
| -------------------------- | ------------------------------- | ------------------------------- |
| Player not touching any keys  | nothing                  | nothing                         |
| Player presses enter | View changes to GameView | View changed |
| Mouse key pressed  | GameView drawn up                 | As expected                     |
| Key "y" pressed         | nothing          | Start screen remains                            |                     |                                 |                                 |



