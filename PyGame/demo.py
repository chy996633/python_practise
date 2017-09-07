# 1 import pygame

import pygame
from pygame.locals import *

# 2 Initialize the game
keys = [False, False, False, False]
playerpos = [100, 100]
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 3 load image
player = pygame.image.load("resources/images/dude.png")

grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")


# 4 keep the loop through
while 1:
    screen.fill(0)
    for x in range(width/grass.get_width() + 1):
        for y in range(height/grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    screen.blit(player, playerpos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False

    if keys[0] == True:
        if playerpos[1] > 0: playerpos[1] -= 5
    if keys[1] == True:
        if playerpos[0] > 0: playerpos[0] -= 5
    if keys[2] == True:
        if playerpos[1] < height - player.get_height(): playerpos[1] += 5
    if keys[3] == True:
        if playerpos[0] < width - player.get_width(): playerpos[0] += 5



