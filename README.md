# mapmaker
-
I found myself writing one-off tools to create prefab level geometry, which is fine, until you have
three or four of them, then keeping them straight, ensuring you don't break one while building a new
one... all a headache.

So, what I've done is create a front-end application that uses tool modules.  Don't worry about any
of that if you don't want to, it's really simple to use.

The controls are displayed at the top of the map maker window.  Important to note, if you press Esc
to exit, it does not save the map.  In fact, it saves an empty file instead.  You ***MUST*** press
F5 to save/exit.

It will save test.blv in the same location as the application "mapmaker.exe".  You will need to copy
or move this file to the correct location for the game.

Example: D:\SteamLibrary\steamapps\common\Besiege\Besiege_Data\CustomLevels\

I'm going to continue building more prefabs into it as I can find time to.  Currently the brick wall
and the spire are the only two I've got converted from standalone tool to module.

Coming attractions:

-Spires that don't look like... well, that.

-Terrain features (mountains or smth?)

-More prefabs once I come up with some ideas for what they should be

-And last but not least, your suggestions.

That's right, if you've read this far, I want you to suggest new ideas for prefabs, or if you feel
like taking on a challenge, creating new prefabs yourself.  They're not terribly hard.  Everything
in this application is written for Python 3.7/3.8.  I've tried to comment the code so that if you
understand python, you should be able to make sense of it (and probably laugh at my messy code).
