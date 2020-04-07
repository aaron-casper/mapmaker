#!/usr/bin/env python3
import pygame

# === CONSTANTS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400
running = True
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# === CLASSES === (CamelCase names)
while running == True:
    pygame.draw.line(screen, WHITE, (10,10),(50,50))
    pygame.display.update()
