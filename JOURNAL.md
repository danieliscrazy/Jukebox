---
title: "Jukebox"
author: "@dld"
description: "Physical Minecraft Jukebox that plays discs!"
created_at: "2025-05-22"
---

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
