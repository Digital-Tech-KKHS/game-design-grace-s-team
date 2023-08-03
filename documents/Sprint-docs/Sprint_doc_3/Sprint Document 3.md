# Details
**Name:**
Grace
**Git Hash:**
7def5e259d29718fb6d041c421e216e649f08e7d
**Sprint Number:**
3
**Start Date:**
15/05/2023
**End Date:**
02/06/2023
**Work hard rating**
☆☆☆☆☆

# Project at the start of the sprint
## **KANBAN board at the start of the sprint**
![[Pasted image 20230529141926.png]]
## **Screenshot of the game at the start of the sprint**
![[Pasted image 20230522141057.png]]
# Sprint Summary
## **Sprint Reflection and summary**
In this sprint I tested going to different levels and I tested how trees would be used to block my character from going to specific places. and I also had a lot of trouble making my trees work to be the walls, so I had help from my class mates and I also experimented with different ways to deal with the issue in tiled. The main issue with my trees that I was having was a issue where when my character collided at a certain point with the trees my game would close and an error message would appear. The issue itself turned out to be an issue in tiled like I predicted and so I had to work my way around that to solve it. I also wanted to work on damage and I successfully made it so that I my owl character would get damaged when it came into contact with a "coil of barbed wire", and would "jump" backwards away from the wire. I also added more art and made another entire level that used the trees as a way for the character to be blocked in. Jumping was a big thing that I wanted to implement into my game so that my character would have another element to it that would make it fun and more enjoyable for the players to use. I first had problems with the gravity function, with it wanting to revert gravity to 0 and so my player would drop, and then I had issues with my character jumping too high and it not reverting back to its original position. In the end I was able to get my player to jump around WITH a shadow that would shrink when the player was "air born" and would expand when my player came back to the ground.

## **Briefly describe other team members contributions**
- No team-mates
## **Major Changes and Achievements Described**
 - I changed my maps a bit and added an extra on 1 to 2, so that I was slowly moving towards the goal of having 3 maps
 - Making the player jump was a massive achievement because it meant that I was able to add in jumps in to my game and it allowed me to make a shadow underneath my player which gave it almost a realistic affect
 - Adding a damage sprite was good as well because it meant that I had added more challenge to the game and it was something that my peers had asked if I would do and suggested for it.
 - Temporarily had a red shape around my character that symbolized the owls hit box and so when I took that away it really showed how much my game had developed from the very early designs which was an awesome achievement to see.
## **Brief Description of your testing**
- I tested how my character would jump and land, this meant that I needed to have a gravity component that allowed me to be able to lift from the ground in a straight vertical way and return back to that spot. This was actually quite challenging because it meant that I had to enable a gravity function but I couldn't have gravity normally in my game because it was a top down game. So I had to make my character have states when it was 1. jumping, and 2. Not jumping this meant that the gravity function would be secluded specifically to when the character was jumping.
- I also tested the issue that I had with collisions and I was able to solve it because it was caused when on the tilemap I had placed a ghost tile accidently, meaning that there wasn't actually anything on the tile, and so when the game tried to load it up it would crash because it was trying to draw something that wasn't there.
- I also tested how my character would get damaged and so I made a collision tile that would make the player "-health" each time that it collided with it
- I wanted to add a function that meant that when the character did get hurt, instead of staying in the same place and getting instant killed it would force the player to move backwards (-x, -y) away from the danger so that they player could keep going after the interaction
- I added a shadow onto the player so that when it jumped you could follow the characters path better instead of it just looking like the player was moving up the map, I drew the shadow onto the players center_x, and center_y and made it have a scale so that when my character jumped the shadow would shrink and when it would land it would have a larger shadow that was the size of the owls body

## **Link to testing results/tables**


# Project at the end of the sprint
## **KANBAN board at the end of the sprint**
![[Pasted image 20230607100439.png]]
## **Screenshot of the game at the end of the sprint**
![[Pasted image 20230529141204.png]]

## Link to **Video of the game at the end of the sprint**
![[sprint_3.webm]]

## **Notes for next time, future improvements**
- In the next sprint I really want to add some kind of text element in it so that it feels more interactable with the player and also so the end user can know to stay clear of certain things.
- I also would like to make enemies next sprint as well. I have wanted to make them for a long time because I believe that they will improve my game a lot and bring more challenge and enjoyment to it
- I also need to split my code up so that it isn't in one large file where it can get hard to find what I'm looking for
- 