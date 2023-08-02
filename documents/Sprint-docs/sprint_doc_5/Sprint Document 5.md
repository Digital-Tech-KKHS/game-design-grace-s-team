# Details
**Name:**
Grace McDonald
**Git Hash:**

**Sprint Number:**
5
**Start Date:**
17/07/2023
**End Date:**
04/08/2023
**Work hard rating**
☆☆☆☆☆

# Project at the start of the sprint
## **KANBAN board at the start of the sprint**
![[Pasted image 20230802212137.png]]
## **Screenshot of the game at the start of the sprint**
![[Pasted image 20230716124641.png]]
# Sprint Summary
## **Sprint Reflection and summary**
In this sprint I tested my game a lot on potential end users and class mates. I asked Gabby, Erin, Sylvie, and Zane to test my game and give me feedback. I learnt that both Gabby and Zane had issues doing a jump so I used this to make my jumps easier to jump across so that the game was more enjoyable. I wondered if it would be better to increase the speed of my character or shorten the jump. After testing the increasing speed idea I ended up going with making the jump shorter because I saw that if I increased the speed of the character it threw of the speed of it naturally and didn't look and feel as good to use. I also asked them what they thought of the art and they liked it however Erin said that she wanted me to add more small details so that it would feel more complete. I fixed my characters walking animation which ended up being a piece of code that I had somewhere else that was making the code contradict itself. I made my final map which I had to make new tiles for and I made "wings" at the end of the map that lead the player to an end view which shows the game was over. I also made a collision tile that if you didn't have enough feathers it would say that you need to go look for more. I went through all the levels multiple times with my character to make sure that there was no gaps in the tiles or any tiles that didn't belong there. I made completely new win, death, and start screen art as well which turned out better then I could have hoped. I redid my game design document because it still was about my old idea kelpie idea for my game, and I touched up my sprint docs, tests, and trials across all the sprints to make sure that I hadn't missed anything. I added an NPC which enabled me to have dialogue and bring more of the plot into and story into the game, as well as helping the end user understand what they needed to do. The NPC says to the player that they must get at least a certain amount of feathers to win, by feathers they mean coins because I changed all of my "bug coins" into feathers to fit better with the story. I ended up deciding that I would add a "bonus" feather somewhere on my map that would +5 onto your score when you collide with it, and I increased the the minimum amount of feathers required to get to the "win" screen because of this. I also asked my teacher to open my game on his computer so that I could see if it worked on a different computer but also I wanted the opinions of someone who hadn't played my game much. The current enemies that I had I feel didn't really add anything to the story and I wanted something kind of silly yet also practical so I swapped out my snake design for a mosquito. Overall in this sprint I did a lot of things, the reason being that it was the final one, and also I kept coming up with ideas that I wanted to add that I believed the end users would enjoy more. Another thing that I added was music. I made my own music in Sound Trap and I put it into my game to play in the background while the end users moved around and played my game. I felt like my game had a lack of something, and I realized that it was powerups, so I added 4 speed potions that were directionally controlled meaning that if you hit a certain one your speed would increase in that specific direction, until you released your key.
## **Briefly describe other team members contributions**
- No team-mates
## **Major Changes and Achievements Described**
- Major changes were the different win, lose, and start views that I made. Before they were blank PNG's that had writing on them and after they were full of the story and colour which I believe really helped the game pop.
- Also changing the enemy to a mosquito was a good change because there was a glitch that got created from the tracking engine of the enemies that would make it appear that the snakes were vibrating, and so with them being mosquitos they suited this because it made them look as if they were buzzing. And I honestly believe that it made them look better then just slowly floating towards the player.
- Music was something that I knew needed to be added but I just never had the time to spare to actually make it and then put it into my code. I am glad that I got around to doing it because it made everything feel more final. Like my game wasn't just a concept anymore but an actual game that had its own music instead of empty silence.
- Getting random people to look at my game and play it was a good achievement because it meant that it was a fully functioning game that end users could enjoy and give feedback on.
- Adding the NPC was a massive change because instead of a sign pointing and telling you something, there was an actual thing communicating with the player and it helped with the plot too which I believe is a good achievement.
- I think that the overall achievement of this sprint was simply getting a game that I was proud of. A game that I had spent so much time on and you could finally see it.  
## **Brief Description of your testing**
- I tested implementing my music into my game in several different ways, and they each had there pros and cons, I first tried to make the song and repeat it in my Gameview class but I kept running into issues like my game overplaying itself when I went from StartView to GameView and then it not running at all.
- I tested colliding with the win tile and what would happen if the player didn't have a sufficient number of feathers, I made it so that if the player had < then the desired amount of feathers no collision would occur. and a message would pop up saying that you needed to find more feathers
- I tested what the words the NPC would be and how they would appear on screen, what size and which x and y co ordinates they would be drawn at in correlation to my player
- I tested getting damaged by my enemy and how the character would react to it. If the player was moving and the enemy collided with the them the player would get moved back away from it and if the player was stationary then they would die instantly. health = 0 and death screen would appear.
- I tested how the player would control the character by looking at how my end users used the keys and I changed a few speeds around of different directions, increased to  x = -4 for moving left and so on.
- I tested how I would get my speed potions to work and increase my players speed, by making them be directional so that I could use them later on, to speed the player on when they were going to specific places. when colliding with potion(s) player speed + (certain amount).
## **Link to testing results/tables**


# Project at the end of the sprint
## **KANBAN board at the end of the sprint**
![[Pasted image 20230802222252.png]]
## **Screenshot of the game at the end of the sprint**
![[Pasted image 20230802211333.png]]
## Link to **Video of the game at the end of the sprint**


## **Notes for next time, future improvements**
- I do believe that one thing that I have learnt from the whole process was to manage my sprint docs as much as possible and make sure that they are up to date. That is something that I would definitely do different if I had to do the whole project again, I would take the warnings about running out of time more seriously.
- I also think that a way that I could improve my game would be if I was able to add more to do with the actual lore, so that it could feel deeper. 
- If given enough time I would have also improved how the character interacted with wall blocks and other components of working in oblique.
- I also would have liked as I said before to build on the lore and maybe have added a function that at the end of the game when you collect the wings (flying ability) the player was able to activate them and fly around for a bit, but I ran out of time.
- I would also make a more comprehensive plan at the beginning so that I have a somewhat solid idea of what my final product will look like instead of just presuming.
   