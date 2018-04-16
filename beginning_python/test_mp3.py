import pygame
filename = input("> file name: ")
file_template = 'music/%s.mp3'
file=file_template % filename
pygame.init()
print("play music")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
while 1:
     isBusy = pygame.mixer.music.get_busy()
     if isBusy != 1:
        pass

pygame.mixer.music.stop()
