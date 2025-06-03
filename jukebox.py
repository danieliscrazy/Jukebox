# This code was partially made with the use of Copilot AI, specifically the functionality for detecting the removal of the NFC tag.
# Given that most of the non-AI code was cobbled together from posts on Reddit, StackOverflow, and the Raspberry Pi forum, this code is exempted from the GNU GPLv3 that the rest of the repository is under. I take no credit or ownership of its contents, and you are free to do whatever you want with it.

from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc
reader = SimpleMFRC522()

chirp = vlc.MediaPlayer("file:///home/danield/jukebox/chirp.mp3") # https://vgmsite.com/soundtracks/minecraft/adxomiqwds/2-20.%20Chirp.mp3
otherside = vlc.MediaPlayer("file:///home/danield/jukebox/otherside.mp3") 
mellohi = vlc.MediaPlayer("file:///home/danield/jukebox/mellohi.mp3") # https://vgmsite.com/soundtracks/minecraft/gmbkrizoms/2-22.%20Mellohi.mp3
cat = vlc.MediaPlayer("file:///home/danield/jukebox/cat.mp3") # https://vgmsite.com/soundtracks/minecraft/biwkbeziap/1-19.%20Cat.mp3
start = vlc.MediaPlayer("file:///home/danield/jukebox/start.mp3")

last_id = None

tries = 0
start.play()
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read_no_block()
        if id == 584186575628:
            if last_id != id:
                print("Detected! Playing!")
                otherside.play()
            last_id = id
            tries = 0
        elif id == 584187564821:
            if last_id != id:
                print("Detected! Playing!")
                chirp.play()
            last_id = id
            tries = 0
        elif id == 584197590179:
            if last_id != id:
                print("Detected! Playing!")
                mellohi.play()
            last_id = id
            tries = 0
        elif id == 584189789991:
            if last_id != id:
                print("Detected! Playing!")
                cat.play()
            last_id = id
            tries = 0
        else:
            if last_id is not None:
                tries += 1
                if tries >= 5:
                    print("No longer detected! Stopped!")
                    otherside.stop()
                    chirp.stop()
                    mellohi.stop()
                    cat.stop()
                    last_id = None
                    tries = 0
        sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
