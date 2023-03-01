## Test 1 EXAMPLE:
# Getting user input

Date: 1/1/2022

```python
if arcade.check_for_collisions_with_list(player, enemies):
	player.health -= 1
	if player.health <= 0:
		player.kill()
		Game.restart()
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Player not touching enemy    | nothing                         | nothing                        |
| Player touching health = 3 | health set to 2, heart disapear | health became 2, heart remained |
| Player touching health = 1   | Game restarts                   | As expected                               |


