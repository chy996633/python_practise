import pygame

filename = [2,3]
file_template = 'music/%s.mp3'
i=0
file=file_template % filename[i]
pygame.init()
print("播放音乐")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
i+=1
pygame.mixer.music.queue("music/3.mp3")
# time.sleep(10)
while 1:
     isBusy = pygame.mixer.music.get_busy()
     if isBusy != 1:
        pass
     #    print("播放下一首")
     #    file = 'music/2.mp3'
     #    track = pygame.mixer.music.load(file)
     #    pygame.mixer.music.play()


pygame.mixer.music.stop()
