# import libs
print("importing libraries")
i = 0

import os
import time
import random
import pygame


#this one didn't quite meet the need yet, still working on it
#goal is to permit configuration of map name/title
#import pygame_textinput
#print('.',end='')

#import tool modules
#print a '.' for each module imported, iter i as well to give count later
print('importing tool modules')
import brickwall_vert
print('.',end='')
i = i + 1

import brickwall_horiz
print('.',end='')
i = i + 1

import spire
print('.',end='')
i = i + 1

import small_hut
print('.',end='')
i = i + 1
import terrain
print('.',end='')
i = i + 1

#bool to keep loop going
running = True
print("")
#define version
appVersion = 0.8

#print details
print("pyMapMaker v" + str(appVersion))
print("loaded " + str(i) + " modules")

# define app window size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
    
print("initialize GUI")
try:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("set screen size")
    
except Exception as e:
    print(e)

pygame.display.set_caption('Map-Maker')

print("set screen title")

font = pygame.font.SysFont("Consolas",16)
print("set font")

#todo: prompt user for filename
mapName = "test.blv"
print("set map filename")


#define tool module assignments
WALL_HORIZ = 1
WALL_VERT = 2
SPIRE = 3
HUT = 4
SPAWN = 5
HILL = 6
print('defined object types')

#define tool
toolScaleX = 1
toolScaleY = 1
toolOption = 1
toolColor = (255,255,255)
toolScale = 1
print("defined tool settings")

#set elevation above floor
Y = 0.0 
print("defined floor")

YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (32,32,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
ORANGE = (255,196,0)
PURPLE = (255,0,255)
print("taste the rainbow")

print("pondering the existential concept of a button")
#this class blatently ripped from https://github.com/furas/python-examples/blob/master/pygame/button-hover/example-1.py
class Button():

    def __init__(self, text, x=0, y=0, width=50, height=50, command=None):

        self.text = text
        self.command = command
        
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(BLACK)

        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill(RED)

        self.image = self.image_normal
        self.rect = self.image.get_rect()
        
        text_image = font.render(text, True, WHITE)
        text_rect = text_image.get_rect(center = self.rect.center)
        
        self.image_normal.blit(text_image, text_rect)
        self.image_hovered.blit(text_image, text_rect)

        # you can't use it before `blit` 
        self.rect.topleft = (x, y)

        self.hovered = False
        #self.clicked = False

    def update(self):

        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal
        
    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                print('Clicked:', self.text)
                if self.command:
                    self.command()
                if self.text == "Quit":
                    shutDownApp()
                if self.text == "Save":
                    saveMap(f)
                if self.text == "Save & Quit":
                    f.write(XMLfooter)
                    time.sleep(0.5)
                    saveMap(f)
                    time.sleep(0.5)
                    shutDownApp()
                if self.text == "Next Tool":
                    return 1
                if self.text == "Prev Tool":
                    return 1

#btnQuit = Button('Quit', 5, 0, 150, 20)
#btnSave = Button('Save', 200, 0, 150, 20)
#btnToolUp = Button('Next Tool', 400, 0, 150, 20)
#btnToolDown = Button('Prev Tool', 600,0,150,20)
#btnSaveQuit = Button('Save & Quit',800,0,150,20)

# === FUNCTIONS === (lower_case names)
    # empty

# === MAIN === (lower_case names)
print("creating buttons, now that we know what they are")
# buttons (text/label, x, y, width, height)
btnQuit = Button('Quit', 5, 0, 150, 20)
btnSave = Button('Save', 200, 0, 150, 20)
btnToolUp = Button('Next Tool', 400, 0, 150, 20)
btnToolDown = Button('Prev Tool', 600,0,150,20)
btnSaveQuit = Button('Save & Quit',800,0,150,20)

#hide OS cursor, we will generate custom ones for each tool
pygame.mouse.set_visible(False)
print("hid OS mouse cursor")

#instance of text-input object | still broken
#textinput = pygame_textinput.TextInput()

# open map file to write to
f = open(mapName, "w")
print("opened map file for writing")

# table of things we've spawned
objects = []
print("created table for objects")

# buffer for the window-header output text
headerBuffer = []
print("created buffer for output")

# scaling for tools
scale = 1
print("defining XML header")
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

print("defining XML footer")
XMLfooter = ('''</Objects></Level>''')

#close file out, incl XML for player spawn and footer.
def shutDownApp ():
    print("shutting down")
    f.close()
    print('closed file')
    time.sleep(1)
  #  input('[Enter] to terminate GUI and quit')
    pygame.quit()
    print('close GUI')
    time.sleep(0.5)
    print('exiting')
    quit()



print("defined how to shutdown app")

f = open(mapName, "w")
f.write(XMLheader)
# END XML map header
headerBuffer.append('main loop start')

def saveMap (f):
    headerBuffer.append("saved")
    f.flush()
    os.fsync(f.fileno())
    time.sleep(0.5)
    print("saved " + mapName)

def toolUp (toolOption):
    headerBuffer.append("next tool")
    toolOption = toolOption + 1
    return toolOption

def toolDown (toolOption):
    headerBuffer.append("prev tool")
    toolOption = toolOption - 1
    return toolOption

def mapReset (f):
    f.flush()
    os.fsync(f.fileno())
    print("file sync'd")
    f.close()
    print("file closed")
    try:
        f2 = open(mapName, "w")
    except Exception as e:
        print("IO Error: " + str(e))
    print("new file opened " + str(f.closed))
    f2.write(XMLheader)
    print("writing XML header")
    objects.clear()
    print("map memory cleared")
    headerBuffer.append("map reset")
    print("all done resetting the map")
    return f2
  
             
# start the main program loop

while running == True:
# get mouse position
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

# define player spawn XML

    XMLplayerSpawn = ('''			<Object ID="''' + str(objID) + '''" Prefab="9001">
			<Position x="''' + str(mouse_x - 500) +'''" y="5.0" z="''' + str(mouse_y - 500) + '''" />
			<Data />
		</Object>''')

# clear display
    screen.fill((255, 255, 255))
    #pygame.draw.rect(screen,BLUE,(495,495,10,10))
    for object in objects:
       # print(object[3])
        if object[3] == WALL_HORIZ:
            objX = int(object[1])
            objY = int(object[2])
            objScale = int(object[4] * 3)
            pygame.draw.line(screen, BLACK, (objX, objY), (int(objX + objScale), objY))
        if object[3] == WALL_VERT:
            objX = int(object[1])
            objY = int(object[2])
            objScale = int(object[4] * 3)
            pygame.draw.line(screen, BLUE, (objX, objY), (objX, int(objY + objScale)))
        if object[3] == SPIRE:
            objX = int(object[1])
            objY = int(object[2])
            objScale = int(object[4] * 0.75)
            pygame.draw.circle(screen,RED,[objX,objY],objScale,objScale)
        if object[3] == SPAWN:
            objX = int(object[1])
            objY = int(object[2])
            pygame.draw.rect(screen,ORANGE,(objX - 10,objY - 10,20,20))
        if object[3] == HUT:
            objX = int(object[1])
            objY = int(object[2])
            pygame.draw.rect(screen,GREEN,((objX - 17),(objY - 17),35,35))
        if object[3] == HILL:
            objX = int(object[1])
            objY = int(object[2])
            objScale = int(object[4])
            redTint = int(objScale * 5)
            blueTint = int(objScale * 5)
            pygame.draw.rect(screen,(redTint,0,blueTint),((objX),(objY),40,40))
            
            
# catch out of bounds stuff
    pygame.draw.circle(screen,BLACK,[int(SCREEN_WIDTH * 0.5),int(SCREEN_HEIGHT * 0.5)],1,1)
    if scale <= 0:
        scale = 1
    
#WIP: GUI information
    displayDelay = 0.0
    try:
        headerStr = headerBuffer.pop(-1)
    except Exception as e:
        headerStr = ""
    headerStr = str(len(objects)) + " objects | " + headerStr
    headerBar = font.render(headerStr, True, BLACK)
    #keyTipsBar = font.render("ESC: QUIT | F1: SAVE | F2: NEXT TOOL | F3: PREV TOOL | F4: RESET | F5: SAVE & QUIT | MouseWheel: Prefab Scale" , True, YELLOW)
    pygame.draw.rect(screen,BLACK,(0,0,1000,20))
    screen.blit(headerBar,(250,25))
    #screen.blit(keyTipsBar,(5,5))
    

# Tool/Cursor State-engine

    if toolOption == 0:
        toolOption = 6
        toolColor = ORANGE
        toolName = "PLAYER_SPAWN"
        pygame.draw.rect(screen,toolColor,(mouse_x,mouse_y,scale,scale))
    if toolOption == 1:
        toolColor = BLACK
        toolName = "WALL_H"
        toolScale = scale * 3
        pygame.draw.line(screen, toolColor, (mouse_x, mouse_y), (mouse_x + (toolScale), mouse_y))
        
    if toolOption == 2:
        toolColor = BLUE
        toolName = "WALL_V"
        toolScale = scale * 3
        pygame.draw.line(screen, toolColor, (mouse_x, mouse_y), (mouse_x, mouse_y + (toolScale)))
        
    if toolOption == 3:
        toolColor = RED
        toolName = "SPIRE"
        toolScale = int(scale * 0.75)
        pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],toolScale,toolScale)
        
    if toolOption == 4:
        toolColor = GREEN
        toolName = "HUT"
        
        pygame.draw.rect(screen,toolColor,((mouse_x - 17),(mouse_y - 17),35,35))
        
    if toolOption == 5:
        toolColor = ORANGE
        toolName = "PLAYER_SPAWN"
        pygame.draw.rect(screen,toolColor,(mouse_x - 10,mouse_y - 10,20,20))
        
    if toolOption == 6:
        toolColor = PURPLE
        toolName = "HILL (scale is elevation)"
        if scale >= 50:
            scale = 50
        toolScale = round((scale * 0.1),2)
        pygame.draw.rect(screen,toolColor,(mouse_x,mouse_y,40,40))
        
    if toolOption == 7:
        toolColor = BLACK
        toolOption = 1

    #print(toolOption)

    headerBuffer.append("tool selected: " + toolName + " | " + "scale: " + str(toolScale) + " | X: " + str(mouse_x - (SCREEN_WIDTH * 0.5)) + ", " + "Y: " + str(mouse_y - (SCREEN_WIDTH * 0.5)))
# check for inputs


    
    events = pygame.event.get()
    #textinput.update(events)
    for event in events:
         
# GUI buttons
        btnQuit.handle_event(event)
        btnSave.handle_event(event)
        btnToolUp.handle_event(event)
        changeUp = btnToolUp.handle_event(event)
        #print("tool up " + str(changeUp))
        if changeUp == 1:
            toolOption = toolUp(toolOption)
            changeUp = 0
            
        btnToolDown.handle_event(event)
        changeDn = btnToolDown.handle_event(event)
        #print("tool up " + str(changeDn))
        if changeDn == 1:
            toolOption = toolDown(toolOption)
            changeDn == 0
        btnSaveQuit.handle_event(event)
# inputs

        whathappen = str(event.type)
        if whathappen == "12":
             shutDownApp()
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
                     objX = (mouse_x - (SCREEN_WIDTH * 0.5))
                     objY = mouse_y - (SCREEN_WIDTH * 0.5)
                     #headerBuffer.append("placing brick wall at: " + str(objX) + ", " + str(objY))
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         f.write(brickwall_horiz.bricklayer(objID,scale,30,objX,Y,objY))
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, WALL_HORIZ, scale])
                         objID = objID + 9000
                         f.flush()
                         os.fsync(f.fileno())
                                           
                 # brick walls (horizontal)
                 if toolOption == 2:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = mouse_x - (SCREEN_WIDTH * 0.5)
                     objY = mouse_y - (SCREEN_WIDTH * 0.5)
                     #headerBuffer.append("placing brick wall at: " + str(objX) + ", " + str(objY))
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         f.write(brickwall_vert.bricklayer(objID,scale,30,objX,Y,objY))
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, WALL_VERT, scale])
                         objID = objID + 9000
                         f.flush()
                         os.fsync(f.fileno())
                                            
                #spire generator
                 if toolOption == 3:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     objID = objID + 1
                     objX = mouse_x - (SCREEN_WIDTH * 0.5)
                     objY = mouse_y - (SCREEN_WIDTH * 0.5)
                     #headerBuffer.append("placing spire at: " + str(objX) + ", " + str(objY))
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         f.write(spire.spirebuilder(objID,scale,objX,Y,objY))
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, SPIRE, scale])
                         objID = objID + 10
                         f.flush()
                         os.fsync(f.fileno())
                   
                 if toolOption == 4:
                     #create an object ID and offset by half the area size (to center things up in-game)
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         objID = objID + 1
                         objX = mouse_x - (SCREEN_WIDTH * 0.5)
                         objY = mouse_y - (SCREEN_WIDTH * 0.5)
                         f.write(small_hut.hutbuilder(objID,objX,objY))
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, HUT, scale])
                         objID = objID + 21
                         f.flush()
                         os.fsync(f.fileno())
                     #objects.append([objID,objX,objY, SPIRE, scale])
                 if toolOption == 5:
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         #create an object ID and offset by half the area size (to center things up in-game)
                         objID = objID + 1
                         objX = mouse_x - (SCREEN_WIDTH * 0.5)
                         objY = mouse_y - (SCREEN_WIDTH * 0.5)
                         f.write(XMLplayerSpawn)
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, SPAWN, scale])
                         f.flush()
                         os.fsync(f.fileno())
                     #objects.append([objID,objX,objY, SPIRE, scale])

                 if toolOption == 6:
                     if mouse_y <= 20:
                         print("not placing, in menu area")
                     if mouse_y > 20:
                         #create an object ID and offset by half the area size (to center things up in-game)
                         objID = objID + 1
                         objX = mouse_x - (SCREEN_WIDTH * 0.5)
                         objY = mouse_y - (SCREEN_WIDTH * 0.5)
                         f.write(terrain.terrainplacer(objID,objX,objY,toolScale))
                         objX = objX + (SCREEN_WIDTH * 0.5)
                         objY = objY + (SCREEN_WIDTH * 0.5)
                         objects.append([objID,objX,objY, HILL, scale])
                         f.flush()
                         os.fsync(f.fileno())
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
                 toolOption = toolUp(toolOption)
             if whichkey == "284":
                 toolOption = toolDown(toolOption)
             if whichkey == "27":
                 shutDownApp()
             if whichkey == "282":
                 saveMap(f)
             if whichkey == "285":
                 #print("map reset broken, issue on github")
                 f = mapReset(f)
             if whichkey == "286":
                 f.write(XMLfooter)
                 saveMap(f)
                 time.sleep(0.5)
                 shutDownApp()
            # if whichkey == "113":
            #     running = False
            #     headerBuffer.append("quit")

    btnQuit.update()
    btnSave.update()
    btnToolUp.update()
    btnToolDown.update()
    btnSaveQuit.update()

    btnQuit.draw(screen)
    btnSave.draw(screen)
    btnToolUp.draw(screen)
    btnToolDown.draw(screen)
    btnSaveQuit.draw(screen)
    
    # mouse cursor
    
    if mouse_y <= 20:
        #pygame.draw.circle(screen,GREY,[mouse_x,mouse_y],2,2)
        pygame.mouse.set_visible(True)
    if mouse_y > 20:
        pygame.draw.circle(screen,toolColor,[mouse_x,mouse_y],2,2)
        pygame.mouse.set_visible(False)
        font = pygame.font.SysFont("Consolas",10)
        cursorInfo = font.render((str(mouse_x - 500) + "x, " + str(mouse_y - 500) + "y"), True, BLACK)
        screen.blit(cursorInfo,((mouse_x + 10), (mouse_y + 10)))
        font = pygame.font.SysFont("Consolas",16)
    #blit display
    pygame.display.flip()    
    time.sleep(0.05) # debug/timescale

