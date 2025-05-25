# This code was partially made with the use of Copilot AI, specifically the functionality for detecting the removal of the NFC tag.
# Given that most of the non-AI code was cobbled together from posts on Reddit, StackOverflow, and the Raspberry Pi forum, this code is exempted from the GNU GPLv3 that the rest of the repository is under. I take no credit or ownership of its contents, and you are free to do whatever you want with it.

from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc
reader = SimpleMFRC522()

p = vlc.MediaPlayer("file:///home/danield/jukebox/song1.mp3")

last_id = None   

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read_no_block()
        if id == 584186575628:
            if last_id != id:
                print("Detected! Playing!")
                p.play()
            last_id = id
        else:
            if last_id is not None:
                print("No longer detected! Stopped!")
                p.stop()
                last_id = None
        sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    

