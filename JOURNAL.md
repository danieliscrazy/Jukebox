---
title: "Jukebox"
author: "@dld"
description: "Physical Minecraft Jukebox that plays discs!"
created_at: "2025-05-22"
---
> I spent approximately 7 hours on this so far.

This is the start of my journal file! This project is a physical Minecraft jukebox that plays physical discs! This will be accomplished using a 3d printed model with a Pi Zero W powering it, an RC522 RFID shield, a wired speaker (maybe Bluetooth if I can't get OTG working), and RFID chips I put into the discs (hardware choices are not final). Everything will be 3D printed. I'd add more but I need to go to my next class, so I'll add more later.

### May 23, 2025
Going to start doing work and research on this stuff. Time is 1:17 PM for my own future reference. I know this might be bad practice but I'm just gonna make a commit every time I edit the journal. Anyways, I think that I might instead of a Pi Zero use a 3 B+, because the Zero has no native wired output, and getting it and a HAT would be about the same cost as getting a Pi 3 B+. Gonna look at how I could do the NFC interface and code now.

1:32 PM: Using [this](https://www.instructables.com/RFID-RC522-Raspberry-Pi/) for reference for wiring and maybe the basis of the RC522 interface. My dumb ass just remembered I need to actually flash Pi OS onto my Pi. I'm gonna do that first lol.

2:00 PM: Finally put my Hack Club SD card to good use! Trying to wire up and test out the RFID board now.

2:10 PM: Nevermind, that tutorial uses Python 2 (despite being from only 2017). Gonna try [this one](https://pimylifeup.com/raspberry-pi-rfid-rc522/) instead.

2:53 PM: Had to take a roughly 45 minute break. Didn't get to wiring up anything yet, will do it now!

3:09 PM: Wired up and basic tests are working! Going to take a break for now (even though I've only gotten a bit done). Not sure how much of the time I've spent was just me slacking off but I'd say between getting it set up and the bit of research I did before starting this journal entry I've done about an hour of work.

![IMG_3839 (1)](https://github.com/user-attachments/assets/7a3792c3-5d5c-441e-b36f-8dab55adc964)
> My crappy photo of my setup, scanning a Dave and Busters card (yes ik my floor's dirty)

![image](https://github.com/user-attachments/assets/8bc12483-85d8-4514-a342-84923e08bdf2)
> The terminal output on my Pi

### May 24, 2025
10:24 AM: I'm gonna work on the 3D models now. Gonna make them in TinkerCAD as that's what I'm most experienced with. I think for size I'm basically going to do each pixel is 8 mm (so the whole jukebox will be a 128 mm cube).

10:50 AM: Got one face of the jukebox done. I'm gonna need to make the discs at a weird scale so that they fit, they'll be around 5mm pixels. Taking a break now and will log again right when I come back.

![image](https://github.com/user-attachments/assets/87b942b6-64e1-44c4-971e-d9b2a5c0aa6d)
> A side of a jukebox!
 
12:06 PM: Back! Getting back to work.

12:26 PM: Finished the basic structure. Gonna try to work on how the electronics fit in now.

![image](https://github.com/user-attachments/assets/75807609-f29d-4d2f-a878-2c99937b0f38)
> A jukebox!

12:59 PM: Got the basic structure of how it's gonna work down. Basically now all I need is to put in space for the Raspberry Pi (and the speaker, which I'm just now realizing I've done no work on researching) and divy it up so it can be printed. I made a GIF!

![image](https://i.imgur.com/0uyaF67.gif)
> How the discs will work. The circle in the disc is for the NFC tags.

1:45 PM: Just remembered I got my current Pi 3 B+ from a Kano kit, which had a speaker case in it. I think I can easily adapt it to fit this. With that, I think my case is nearing completion, just need to figure out how I'll assemble it. Also, I found out that someone else online made something like this before! They used a software called [PhonieBox](https://phoniebox.de/index-en.html), which seems to be exactly what I need, but I do want to try to make this myself because I feel like that wouldn't be in the spirit of Highway. If I can't get it to work in Python though, I will use that.

![image](https://github.com/user-attachments/assets/da1da90f-6023-4e61-8953-001d19ab3618)
> The jukebox with a speaker hole and a hole for the Raspberry Pi's ports.

2:43 PM: Haven't worked any more since 2. Gonna work more now.

3:13 PM: Split it up into 6 pieces, but currently can't figure out how to connect them. Was going to just use pegs but that didn't really work, because in order to take it apart the way I wanted, I'd need to put supports in the holes, which would be impossible to remove. Stopping for today. Believe I've worked around 3 hours (bringing the total to 4).

7:30 PM: Been working on this a bit more for like 30 minutes, I think I'm gonna try using this sort of jigsaw style way to join it, making it altogether 4 pieces printed out, the bottom and 3 sides as one piece, the side with the speaker and the Pi as another, the top piece as one, and then the slot for the disc. Gonna try making a test print of the case to see if it all works together.

![image](https://github.com/user-attachments/assets/20c846df-675e-4763-8c33-8771692ab79f)
> The back of the jukebox, with the new joining method

![image](https://github.com/user-attachments/assets/f8694b2e-bb59-4223-8d4b-97bb9a41e8b4)
> All of the parts laid out

### May 25, 2025

9:15 AM: Test print failed, filament got tangled, need to run it again but honestly I've been too lazy to relevel the printer (I really need to get a BLTouch), I'll get around to it. Been working on the software aspect of it for about half an hour now. Not great at Python so basically just cobbling bits and pieces of code that come up when I Google search "rc522 python" and "python playing music". Gonna make the first commit in a few with some test code so that I can just grab the code from GitHub instead of messing with SCP.

10:20 AM: After some issues with the speaker, I got the base code to work, it plays a song when 1 of the tags. Now what I need to do is to implement multiple discs, and figure out how to detect when it's been removed. I'm rather stumped on that last part. I might need to use Copilot for help. If I do, I'll make it blatantly clear what sections are helped by AI. I've been working for about an hour and 15 minutes so far today, today, bringing the toal to like 5 hours and 45 minutes I've worked on this.

10:33 AM: I did end up using Copilot, and I added a disclaimer to my code file, but it seems to work now! I just need to make a bunch of different tags and make it work for multiple of them. Signing off for now, got some school work I need to get done, and I think that brings me up to about a nice even 6 hours. Once I get the code finished, I'll finalize the 3D files, upload them, and get ready to submit it!

### May 26, 2025

12:18 PM: I've been working for I'd say 45 minutes on this, mostly the code but also some wiring (damn thing keeps coming loose). My code is janky and doesn't have all the songs yet, but it works! I think I'm ready to submit. Gonna upload all the STL files and all that.
