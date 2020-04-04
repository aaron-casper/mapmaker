import pygame
pygame.init()
# define app size
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0,0,0)
running = True
while running == True:
    for event in pygame.event.get():
        whathappen = str(event.type)
        print(whathappen)
        if whathappen == "12":
            running = False
        if whathappen == "5":
            whichbutton = str(event.button)
            print(whichbutton)
            if whichbutton == "1":
                print("left-click")
            if whichbutton  == "2":
                print("middle-click")
            if whichbutton  == "3":
                print("right-click")
            if whichbutton  == "4":
                print("scroll-up")
            if whichbutton  == "5":
                print("scroll-down")

        if whathappen == "2":
            whichkey = str(event.key)
            print(chr(int(whichkey)) + " " + whichkey)
            if whichkey == "113":
                running = False


        screen.fill((255, 255, 255))
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        pygame.draw.circle(screen,BLACK,[mouse_x,mouse_y],1,1)
        pygame.display.flip()