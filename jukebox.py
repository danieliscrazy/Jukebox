# This code was partially made with the use of Copilot AI, specifically the functionality for detecting the removal of the NFC tag.
# Given that most of the non-AI code was cobbled together from posts on Reddit, StackOverflow, and the Raspberry Pi forum, this code is exempted from the GNU GPLv3 that the rest of the repository is under. I take no credit or ownership of its contents, and you are free to do whatever you want with it.

from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc
reader = SimpleMFRC522()

otherside = vlc.MediaPlayer("file:///home/danield/jukebox/otherside.mp3")
pigstep = vlc.MediaPlayer("file:///home/danield/jukebox/pigstep.mp3")

last_id = None

tries = 0

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
        elif id == 584196735387:
            if last_id != id:
                print("Detected! Playing!")
                pigstep.play()
            last_id = id
            tries = 0
        else:
            if last_id is not None:
                tries += 1
                if tries >= 5:
                    print("No longer detected! Stopped!")
                    otherside.stop()
                    pigstep.stop()
                    last_id = None
                    tries = 0
        sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
