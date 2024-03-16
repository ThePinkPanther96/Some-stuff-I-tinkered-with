import os
import pygame
import random
import time
from datetime import datetime

dir = "path\\to\\mp3\\files\\Adirectory"

files = os.listdir(dir)

mp3_files = [os.path.join(dir, f)for f in files if f.endswith('.mp3')]

pygame.mixer.init()

try:
    while True:
        mp3_file = random.choice(mp3_files)

        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        maxtdelay = 3 # Change time delay - minutes
        timedelay = random.randrange(1, int(maxtdelay * 60))

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Time Delay:", current_time)

        time.sleep(timedelay)

except KeyboardInterrupt:
    pygame.mixer.music.stop()
    pygame.mixer.quit()
