# Besiege maze generator, it's still not finished but should work well enough
# There is no guarantee it will generate solvable mazes
# by floz
#
# When the maze is as far along as you like, press Q to stop generation 
# and finalize the besiege map.
#
# *** Requires pygame for the visualization while it's generating a maze.
#
# It maintains a running list of where each wall is as it generates in an 
# attempt to avoid placing multiples in the same spot
print('''
***IMPORTANT***
This software comes with no guarantees -implied or otherwise-, and the author shall 
not be held responsible for the results of viewing or executing this software.

basically, if your computer blows up, your cat blows up, or anything else
horrible happens, you cannot and should not blame me.
''')
print("importing modules...\n")
#hide pygame splash text, because it will break your map
import os  
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#Import modules
import pygame
import inspect
import random
import time

# Define constants for the map
print("+-----------------+")
print("|  Maze Generator |")
print("+-----------------+\n\n")
print("I need some details from you\n")
print("Once we've gathered the details and generation runs, use 'Q' to end.\n")
print("Otherwise it just eventually makes a grid\n\n")
mapName = input("Map Name (no spaces, use _ ): ")

try:
    mapName = str(mapName) + ".blv"
except ValueError:
    print("that didn't work, ask the dev")

#this determines maze size
SCREEN_WIDTH = input ("Maze width: ")
try:
    SCREEN_WIDTH = int(SCREEN_WIDTH)
except ValueError:
    try:
        SCREEN_WIDTH = float(SCREEN_WIDTH)
    except ValueError:
        print("Enter a number, bonehead")
        quit()

SCREEN_HEIGHT= input ("Maze height: ")
try:
    SCREEN_HEIGHT = int(SCREEN_HEIGHT)
except ValueError:
    try:
        SCREEN_HEIGHT = float(SCREEN_HEIGHT)
    except ValueError:
        print("Enter a number, bonehead")
        quit()


#this determines the "grid" size of the maze
wallLength = input ("Maze grid size (10 to 50 is good): ")
try:
    wallLength = int(wallLength)
except ValueError:
    try:
        wallLength = float(wallLength)
    except ValueError:
        print("Enter a number, bonehead")
        quit()

#various things
existing = []
Xcenter = SCREEN_WIDTH * 0.5
Ycenter = SCREEN_HEIGHT * 0.5
X = 0
Y = 0


#one way, or t'other
lengthVerticalBlock = wallLength
widthVerticalBlock = 1
lengthHorizontalBlock = 1
widthHorizontalBlock = wallLength

#pick one to start with, chances of a collision are very very low
objID = random.randint(5259037513282550642,5259037513999999999)

print("randomizing by divisibles")
#get a random number divisible by N 
# (ex: random number between 10 and 100 divisible by 2:
# evenValue = getRandom(10,100,2)
def getRandom(a,b,n):
    if n > b-a:
        return -1

    #If a is divisible by n, use a as a start, using n as step size
    if a%n == 0:
        return random.randrange(a,b,n)

    # If a is not divisible by n, use a+n-(a%n) as a start, using n as step size
    else:
        return random.randrange(a+n-(a%n),b, n)

#define our block
print("defining what a block can be")
class block:
    def __init__(self, X, Y, D):
        self.X = getRandom(0,SCREEN_WIDTH,wallLength)
        self.Y = getRandom(0,SCREEN_HEIGHT,wallLength)
        self.D = random.randint(0,1)

print("initializing visualization...")
# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fill the screen with white
screen.fill((255, 255, 255))

# open file to write to
print("opening " + mapName + " for writing")
f = open(mapName, "w")

print("generation beginning")
#XML header for Besiege level
f.write('''<Level>
	<LevelSettings EditorVersion="0.8" UseVoting="False" CurtainMode="False" AllowExcessPlayers="True" HidePlayerLabels="False" AllowCopyMachine="True" allowModMachines="True" Environment="None">
		<DisableFire Enabled="False" Locked="False" />
		<DisableExplosions Enabled="False" Locked="False" />
		<DisableProjectiles Enabled="False" Locked="False" />
		<ZeroG Enabled="False" Locked="False" />
		<InfiniteAmmo Enabled="False" Locked="False" />
		<Invincibility Enabled="False" Locked="False" />
		<ExplosiveCannonballs Enabled="False" Locked="False" />
		<DisableBounds Enabled="False" Locked="False" />
	</LevelSettings>
	<CustomData>
		<StringArray key="requiredMods" />
	</CustomData>
	<Objects>''')

# Variable to keep the main loop running
running = True
id = objID
# Main loop
while running:
    objID = objID + 1 

    # Look at every event in the queue
    # look for quit signal, then shutdown

    for event in pygame.event.get():
         whathappen = str(event.type)
         if whathappen == "12":
             running = False
         if whathappen == "2":
             whichkey = str(event.key)
             if whichkey == "113":
                 running = False

#  DRAW STUFF!

    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 255))
    rect = surf.get_rect()

# instance a block

    myBlock = block(10,10,1)
# check if one's already been made there
    if myBlock not in existing:
        existing.append(myBlock)
    elif block in existing:
        myBlock = block

#if not, pull the variables out of it for use
    X = myBlock.X
    Y = myBlock.Y
    D = myBlock.D

# XML formatting part
# there's a lot of math mixed in with the string formatting.  good luck, have fun!

    f.write('''		<Object ID="''' + str(objID) + '''" Prefab="7000">''')
    horizOrVertical = D
#line goes one way
    if horizOrVertical == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(X,Y, lengthVerticalBlock, widthVerticalBlock))
        lineCenterX = X - lengthVerticalBlock * 0.5
        f.write('''		    <Position x= "''' + str(lineCenterX) + '''" y="0" z="''' + str(Y) + '''"/>''')
        f.write('''		    <Scale x="''' + str(lengthVerticalBlock) + '''" y="20" z="''' + str(widthVerticalBlock) + '''" />''')

#line goes other way
    elif horizOrVertical == 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(X,Y, lengthHorizontalBlock, widthHorizontalBlock))
        lineCenterY = Y - widthHorizontalBlock  * 0.5
        f.write('''		    <Position x= "''' + str(X) + '''" y="0" z="''' + str(lineCenterY) + '''"/>''')
        f.write('''		    <Scale x="''' + str(lengthHorizontalBlock) + '''" y="20" z="''' + str(widthHorizontalBlock) + '''" />''')
    f.write('''		    <Data>''')
    f.write('''		        <Boolean key="bmt-Disable Texture">True</Boolean>''')
    f.write('''		        <Boolean key="bmt-lel-enable-physics">False</Boolean>''')
    f.write('''		    </Data>''')
    f.write('''		</Object>''')

    #slow things down a bit so you can stop it when you want, and blit/flip the display
#    time.sleep(wallLength * 0.005)
    pygame.display.flip()

# XML player spawn and EOF, required for Besiege to load map
print("adding player spawn")
f.write('''		<Object ID="-4518529646287989289" Prefab="9001">
			<Position x="125" y="5.072" z="-50" />
			<Data />
		</Object>
		
	</Objects>
</Level>''')
print("finalizing the file: " + mapName)
f.close()
