_Name:_ Grace McDonald
# Getting user input

Date: 17/07/2023

```python
self.game_view.play_song()

   self.music = arcade.Sound((ROOT_FOLDER.joinpath("Assets", "Main_Song.mp3")), streaming = True)

        self.setup()

    def play_song(self):

        self.music.play(3,0,True)

```

| Test Data                   | Expected                                           | Observed                         |
| --------------------------- | -------------------------------------------------- | -------------------------------- |
| self.game_view.play_song()  | Song starts playing as soon as StartView loads up  | Song plays                       |
| loop = False                | Song doesn't repeat after playing for a full cycle | As expected                      |
| Streaming = False           | Nothing happens                                    | Error message shown              |
| If song file wasn't MP3     | Error raised                                       | as expected                      |
| Not written in Window class | Error raised, causes overlap                       | Error message shown              |
| If volume = 0               | No audio                                           | Song plays but there is no audio |                            |                                                    |                                  |

## Test 2 EXAMPLE:
# Getting user input

Date: 17/07/2023

```python
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['Winner'])

        if self.level == 3 and self.score >= 10:
            if colliding:
                self.window.show_view(self.window.win_view)
```

| Test Data                             | Expected                                             | Observed                                   |
| ------------------------------------- | ---------------------------------------------------- | ------------------------------------------ |
| Self.score <= 10                       | Collison but no change to win_view                   | As expected                                |
| Self.score >= 10                       | Collides and show_view changes to win_view           | Change occurs                              |
| self.level = 2                        | No change                                            | As expected                                |
| No check for collision_with tile list | No collsion will occur because it wasn't checked for | Tile stays the same with no extra features |                                      |                                                      |                                            |

