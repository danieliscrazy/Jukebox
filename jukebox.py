from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc
reader = SimpleMFRC522()

p = vlc.MediaPlayer("file:///home/danield/jukebox/song1.mp3")
                    
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print(id)
        sleep(5)
        if id == 584186575628:
            print("Detected! Playing!")
            p.play()
            
except KeyboardInterrupt:
    GPIO.cleanup()
    

