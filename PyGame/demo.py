# 1 import pygame

import pygame
from pygame.locals import *

# 2 Initialize the game

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 3 load image
player = pygame.image.load("resources/images/dude.png")



# 4 keep the loop through
while 1:
    screen.fill(0)

    screen.blit(player, (100, 100))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
