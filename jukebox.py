# This code was partially made with the use of Copilot AI, specifically the functionality for detecting the removal of the NFC tag.
# Given that most of the non-AI code was cobbled together from posts on Reddit, StackOverflow, and the Raspberry Pi forum, this code is exempted from the GNU GPLv3 that the rest of the repository is under. I take no credit or ownership of its contents, and you are free to do whatever you want with it.

from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc
reader = SimpleMFRC522()

chirp = vlc.MediaPlayer("file:///home/danield/jukebox/chirp.mp3")
otherside = vlc.MediaPlayer("file:///home/danield/jukebox/otherside.mp3")
mellohi = vlc.MediaPlayer("file:///home/danield/jukebox/mellohi.mp3") 
cat = vlc.MediaPlayer("file:///home/danield/jukebox/cat.mp3") 
ward = vlc.MediaPlayer("file:///home/danield/jukebox/ward.mp3")
blocks = vlc.MediaPlayer("file:///home/danield/jukebox/blocks.mp3")
mall = vlc.MediaPlayer("file:///home/danield/jukebox/mall.mp3")
eleven = vlc.MediaPlayer("file:///home/danield/jukebox/eleven.mp3")
far = vlc.MediaPlayer("file:///home/danield/jukebox/far.mp3")
thirteen = vlc.MediaPlayer("file:///home/danield/jukebox/thirteen.mp3")
stal = vlc.MediaPlayer("file:///home/danield/jukebox/stal.mp3")
strad = vlc.MediaPlayer("file:///home/danield/jukebox/strad.mp3")
waiit = vlc.MediaPlayer("file:///home/danield/jukebox/wait.mp3") # not sure if "wait" can be a constant in python so just naming it "waiit"

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
                print("Detected Otherside! Playing!")
                otherside.play()
            last_id = id
            tries = 0
        elif id == 584187564821:
            if last_id != id:
                print("Detected Chirp! Playing!")
                chirp.play()
            last_id = id
            tries = 0
        elif id == 584197590179:
            if last_id != id:
                print("Detected Mellohi! Playing!")
                mellohi.play()
            last_id = id
            tries = 0
        elif id == 584189789991:
            if last_id != id:
                print("Detected Cat! Playing!")
                cat.play()
            last_id = id
            tries = 0
        elif id == 584191236310:
            if last_id != id:
                print("Detected Ward! Playing!")
                ward.play()
            last_id = id
            tries = 0
        elif id == 584190455573:
            if last_id != id:
                print("Detected Blocks! Playing!")
                blocks.play()
            last_id = id
            tries = 0
        elif id == 584195369639:
            if last_id != id:
                print("Detected Mall! Playing!")
                mall.play()
            last_id = id
            tries = 0
        elif id == 584197471632:
            if last_id != id:
                print("Detected 11! Playing!")
                eleven.play()
            last_id = id
            tries = 0
        elif id == 584184558949:
            if last_id != id:
                print("Detected Far! Playing!")
                far.play()
            last_id = id
            tries = 0
        elif id == 584192489952:
            if last_id != id:
                print("Detected 13! Playing!")
                thirteen.play()
            last_id = id
            tries = 0
        elif id == 584195431570:
            if last_id != id:
                print("Detected Stal! Playing!")
                stal.play()
            last_id = id
            tries = 0
        elif id == 584188748081:
            if last_id != id:
                print("Detected Strad! Playing!")
                strad.play()
            last_id = id
            tries = 0
        elif id == 584184358515:
            if last_id != id:
                print("Detected Wait! Playing!")
                waiit.play()
            last_id = id
            tries = 0
        else:
            if last_id is not None:
                tries += 1
                if tries >= 2:
                    print("No longer detected! Stopped!")
                    otherside.stop()
                    chirp.stop()
                    mellohi.stop()
                    cat.stop()
                    ward.stop()
                    blocks.stop()
                    mall.stop()
                    eleven.stop()
                    far.stop()
                    thirteen.stop()
                    stal.stop()
                    strad.stop()
                    waiit.stop()
                    last_id = None
                    tries = 0
        sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
