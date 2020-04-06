MAP MAKER (or really, prefab placer) 
-
v0.0.5

This is still in very eary alpha, if even that.  The goal is simple, to create a prefab-placer tool.

I found myself writing one-off tools to create prefab level geometry, which is fine, until you have three or four of them, then keeping them straight, ensuring you don't break one while building a new one... all a headache.

So, what I've done is create a front-end application that uses tool modules.  Don't worry about any of that if you don't want to, it's really simple to use.

The controls at the top are now mouse-clickable.  The hot-keys still work too.  As before, remember to save before quitting, otherwise it won't finalize the file.

Esc - Exit w/o saving

F1 - Save to file

F2 - Next tool/prefab

F3 - Prev tool/prefab

F4 - Reset (wipes everything on the map) (disabled until bugfix)

F5 - Save & Quit


It will save test.blv in the same location as the application "mapmaker.exe".  You will need to copy or move this file to the correct location for the game.

Example: D:\SteamLibrary\steamapps\common\Besiege\Besiege_Data\CustomLevels\

![alt text](https://raw.githubusercontent.com/flozenstein/mapmaker/master/prefabs.PNG "Before")

![alt text](https://raw.githubusercontent.com/flozenstein/mapmaker/master/prefabs_destroyed.PNG "After")

![alt text](https://raw.githubusercontent.com/flozenstein/mapmaker/master/editorGameComparison.PNG "Editor and Game side-by-side")

Coming attractions:

-More prefabs

-More prefabs

-Terrain features (mountains or smth?)

-And last but not least, your suggestions.

That's right, if you've read this far, I want you to suggest new ideas for prefabs, or if you feel like taking on a challenge, creating new prefabs yourself.  They're not terribly hard.  Everything in this application is written for Python 3.7/3.8.  I've tried to comment the code so that if you understand python, you should be able to make sense of it (and probably laugh at my messy code).

[Instructional Video (may be outdated)](https://youtu.be/kztvYCTBSB4)

Current prefabs:
![alt text](https://github.com/flozenstein/mapmaker/blob/master/test.png?raw=true "Editor")
![alt text](https://github.com/flozenstein/mapmaker/blob/master/test2.png?raw=true "in-Game")

Brick wall (N/S and E/W) (scale determines length

Spire/Post (scale determines height)

Hut (scale does nothing)

Player Spawn (scale does nothing)

Hill (scale determines elevation of the hill)


I think the cursor/marker tool for where a hill prefab has been placed might be a little too small, or the hill itself is scaled too big.  Something to work on in the future.
