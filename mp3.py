import time
import pygame
import sys
file='music/shaonianshiwuershi.mp3'
pygame.init()
print("播放音乐1")
import pdb
# pdb.set_trace()
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
# time.sleep(10)
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print("播放下一首")
            file = 'music/夜空中最亮的星.mp3'
            sys.exit()

pygame.mixer.music.stop()
