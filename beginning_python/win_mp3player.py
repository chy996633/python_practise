import mp3play

filename = r'music/2.mp3'
clip = mp3play.load(filename)

clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()



