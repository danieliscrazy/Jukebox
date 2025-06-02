> WIP!

# Jukebox

This is my Minecraft jukebox IRL project I made for Hack Club's Highway program! It uses a Raspberry Pi Zero 2 with an NFC shield to detect when discs are put in, and plays them out of the speaker in the back! I'm gonna go a bit more in depth about it here.

### Hardware
> I link to parts that I know are from reputable sources. Things I already have/don't remember where I got them from, I didn't link as I don't want to vouch for something I haven't purchased, and if you want to make this project you'll have to look for it yourself. Sorry!

The brains of this project is a [Raspberry Pi Zero 2 W](https://www.adafruit.com/product/5291). I was originally going to use a Pi 3 B+, as it has AUX output and the Zero 2 does not, but that ended up being too expensive for my grant, so I went with a Pi Zero 2 plus an [I2S amp](https://www.adafruit.com/product/3006) and a [3" speaker (4Ω 3W)](https://www.adafruit.com/product/1314). Requires a bit more configuring (see [here](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/overview) for a tutorial), but works just fine. I used an RC522 board alongside a few 1" NFC tag stickers (NTAG215 tags, but it shouldn't matter really). I followed [this guide](https://pimylifeup.com/raspberry-pi-rfid-rc522/) by Pi My Life Up for the wiring and the initial setup. I used the script in their [GitHub README](https://github.com/pimylifeup/MFRC522-python/blob/master/README.md) as a test script. I want to add a wiring diagram here, but Fritzig is being finnicky and I don't have the patience to fix it right now. I'll add it soon. Once I followed that guide, I used the test script to test out the functionality and to get the IDs of the tags.

### Software

The [Python script I have](jukebox.py) is clunky, probably not efficient, and partially AI generated, but it gets the job done. For every song/disc/NFC tag, I just repeat the code. These are the songs themselves.

```
otherside = vlc.MediaPlayer("file:///home/danield/jukebox/otherside.mp3")
pigstep = vlc.MediaPlayer("file:///home/danield/jukebox/pigstep.mp3")
```

Each song has its own tag, and thus tag ID. To add a new disc, I just add an MP3 as shown above, add an `elif`, copy the code over, and replace the tag ID and the song. 

```
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
```

It reads every .2 seconds to see if the disc is there. Then I just have every song stop playing when the tags are removed. I also added some code to not immediately stop it unless it's been detected as gone 5 times, because it turns out the wall of the slot in the case is just barely too thick.

```
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
```
