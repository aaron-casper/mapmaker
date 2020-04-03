# import libs
print("importing libraries",end='')
import time
print('.',end='')
import random
print('.')
import pygame
#this one didn't quite meet the need yet, still working on it
#import pygame_textinput
#print('.',end='')

#import tool modules
import brickwall_vert
print('.',end='')
import brickwall_horiz
print('.',end='')
import spire
print('.')

# define app size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
    
print("initialize GUI")
try:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("set screen size")
    print('.',end='')
except Exception as e:
    print(e)

pygame.display.set_caption('Map-Maker')

print("set screen title")

font = pygame.font.SysFont("Consolas",16)
print("set font")

mapName = "test.blv"
print("set map filename")


#define tool module assignments
WALL_HORIZ = 1
WALL_VERT = 2
SPIRE = 3
print('defined object types')

#define tool
toolScaleX = 1
toolScaleY = 1
toolOption = 1
toolColor = (255,255,255)

print("defined tool settings")

#set elevation above floor
Y = 0.0 
print("defined floor")

YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (96,96,255)
BLACK = (0,0,0)
print("taste the rainbow")

pygame.mouse.set_visible(False)
print("hid OS mouse cursor")

#instance of text-input object
#textinput = pygame_textinput.TextInput()

# open map file to write to
f = open(mapName, "w")
print("opened map file for writing")

# table of things we've spawned
objects = []
print("created table of objects")

# buffer for the window-header output text
headerBuffer = []
print("created buffer for output")

# scaling for tools
scale = 1
print("writing XML header")

#headerBuffer.append('writing XML header')

XMLheader = ('''<Level>
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

objID = random.randint(5259037513282550642,5259037513999999999)

XMLfooter = ('''			<Object ID="''' + str(objID) + '''" Prefab="9001">
			<Position x="0" y="5.0" z="0" />
			<Data />
		</Object>
	</Objects>
</Level>''')

# XML map header
f = open(mapName, "w")
f.write(XMLheader)
# END XML map header
headerBuffer.append('main loop start')

# start the main program loop
running = True
while running == True:

# clear display
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen,BLUE,(495,495,10,10))
    for object in objects:
       # print(object[3])
        if object[3] == WALL_HORIZ:
            objX = object[1]
            objY = object[2]
            objScale = object[4]
            pygame.draw.line(screen, BLACK, (objX, objY), (objX - objScale, objY))
        if object[3] == WALL_VERT:
            objX = object[1]
            objY = object[2]
            objScale = object[4]
            pygame.draw.line(screen, BLUE, (objX, objY), (objX, objY - objScale))
        if object[3] == SPIRE:
            objX = object[1]
            objY = object[2]
            objScale = object[4]
            pygame.draw.circle(screen,RED,[objX,objY],objScale,objScale)


# mouse cursor
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

# catch out of bounds stuff
    if mouse_y <= 20:
        mouse_y = 20
    if scale <= 0:
        scale = 1
    
    pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],2,2)

#WIP: GUI information
    displayDelay = 0.0
    try:
        headerStr = headerBuffer.pop(-1)
    except Exception as e:
        headerStr = ""
    headerStr = str(len(objects)) + " objects | " + headerStr
    headerBar = font.render(headerStr, True, BLACK)
    keyTipsBar = font.render("ESC: QUIT | F1: SAVE | F2: NEXT TOOL | F3: PREV TOOL | F4: RESET | F5: SAVE & QUIT | MouseWheel: Prefab Scale" , True, YELLOW)
    pygame.draw.rect(screen,BLACK,(0,0,1000,20))
    screen.blit(headerBar,(250,25))
    screen.blit(keyTipsBar,(5,5))
    cursorInfo = font.render(str(scale), True, BLACK)

# Tool/Cursor State-engine
    if toolOption == 0:
        toolOption = 4
        toolColor = GREEN
        pygame.draw.rect(screen,toolColor,(mouse_x,mouse_y,scale,scale))
    if toolOption == 1:
        toolColor = BLACK
        pygame.draw.line(screen, toolColor, (mouse_x, mouse_y), (mouse_x - scale, mouse_y))
        screen.blit(cursorInfo,((mouse_x - 10) - scale, (mouse_y)))
    if toolOption == 2:
        toolColor = BLUE
        pygame.draw.line(screen, toolColor, (mouse_x, mouse_y), (mouse_x, mouse_y - scale))
        screen.blit(cursorInfo,((mouse_x), (mouse_y - 10) - scale))
    if toolOption == 3:
        toolColor = RED
        pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],scale,scale)
        screen.blit(cursorInfo,((mouse_x - 10) - scale, (mouse_y)))
    if toolOption == 4:
        toolColor = GREEN
        pygame.draw.rect(screen,toolColor,(mouse_x,mouse_y,scale,scale))
        screen.blit(cursorInfo,((mouse_x) + scale, (mouse_y)))
    if toolOption == 5:
        toolColor = BLACK
        toolOption = 1

    headerBuffer.append("tool selected: " + str(toolOption) + " | " + "scale: " + str(scale) + " | X: " + str(mouse_x) + ", " + "Y: " + str(mouse_y))
# check for inputs

    events = pygame.event.get()
    #textinput.update(events)
    for event in events:
         


# inputs

         whathappen = str(event.type)
         if whathappen == "12":
             running = False
# mouse
         if whathappen == "5":
             whichbutton = str(event.button)

             if whichbutton == "1":
                 #print("left-click")
                 pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],3,3)

                 # brick walls (vertical)
                 if toolOption == 1:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = (mouse_x - 500) - (scale * 1.5)
                     objY = mouse_y - 500
                     #headerBuffer.append("placing brick wall at: " + str(objX) + ", " + str(objY))
                     f.write(brickwall_horiz.bricklayer(objID,scale,20,objX,Y,objY))
                     objX = objX + 500 + (scale * 1.5)
                     objY = objY + 500
                     objects.append([objID,objX,objY, WALL_HORIZ, scale])

                 # brick walls (horizontal)
                 if toolOption == 2:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = mouse_x - 500
                     objY = mouse_y - 500 - (scale * 1.5)
                     #headerBuffer.append("placing brick wall at: " + str(objX) + ", " + str(objY))
                     f.write(brickwall_vert.bricklayer(objID,scale,20, objX,Y,objY))
                     objX = objX + 500
                     objY = objY + 500 + (scale * 1.5)
                     objects.append([objID,objX,objY, WALL_VERT, scale])
                     
                 if toolOption == 3:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = mouse_x - 500
                     objY = mouse_y - 500
                     #headerBuffer.append("placing spire at: " + str(objX) + ", " + str(objY))
                     f.write(spire.spirebuilder(objID,scale,objX,Y,objY))
                     objX = objX + 500
                     objY = objY + 500
                     objects.append([objID,objX,objY, SPIRE, scale])  

                 if toolOption == 3:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = mouse_x - 500
                     objY = mouse_y - 500
                     #headerBuffer.append("placing ____ at: " + str(objX) + ", " + str(objY))
                     #f.write(spire.spirebuilder(objID,scale,objX,Y,objY))
                     objX = objX + 500
                     objY = objY + 500
                     #objects.append([objID,objX,objY, SPIRE, scale])  


             if whichbutton  == "2":
                 print("middle-click")
                 pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],3,3)
             if whichbutton  == "3":
                 print("right-click")
                 pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],3,3)

# scroll wheel rotates through tool states
             if whichbutton  == "4":
                 scale = scale + 1
                 #headerBuffer.append("scale up " + str(scale))
             if whichbutton  == "5":
                 scale = scale - 1
                 #headerBuffer.append("scale down " + str(scale))

# keydown
         if whathappen == "2":
             whichkey = str(event.key)
             if whichkey == "116":
                 print("change tool")
             if whichkey == "114":
                 print("rotate tool")
             if whichkey == "283":
                 toolOption = toolOption + 1
             if whichkey == "284":
                 toolOption = toolOption - 1
             if whichkey == "27":
                 f.close()
                 f = open(mapName,'w')
                 f.close()
                 running = False
             if whichkey == "282":
                 f.close()
                 headerBuffer.append("saved")
                 f = open(mapName,'a')
             if whichkey == "285":
                 f.close()
                 f = open(mapName, "w")
                 f.write(XMLheader)
                 headerBuffer.append("new map opened")
                 objects.clear()
             if whichkey == "286":
                 f.write(XMLfooter)
                 headerBuffer.append("saved")
                 running = False
            # if whichkey == "113":
            #     running = False
            #     headerBuffer.append("quit")


            
    #blit display
    pygame.display.flip()    
    time.sleep(0.05) # debug/timescale

#close file out, incl XML for player spawn and footer.

print("shutting down",end='')
f.close()
print('.',end='')
time.sleep(1)
print('.',end='')
pygame.quit()
print('.',end='')
time.sleep(1)
print('.',end='')
quit()
