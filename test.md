# Doom Minibadge

## Project Description.
This is my Doom Minibadge! I have probably spent over 50 hours making this badge, debugging, and more on this badge, be aware this is held together with duct tape, zip ties, and hopes and dreams.
__NOTES:__
+ This badge is not done yet. I am still working on making it work, I will tell you where I got it wrong, and you can try to fix it, I am working on a solution as we speak.
+ There are LOTS of small parts, I only give you the required amount of parts, __YOU CANNOT LOSE THESE, I CANNOT REPLACE THEM__. Only take this if you are VERY good at soldering.
+ You will need bodge wire! (yayyyy... .  . .) I recommend 32 AWG, minimum is 36 AWG, Max is 26 AWG, I recommend 32, though, as it works so well for the display bodging.
+ Programming is super fun, I will have the files in this workspace, but you will need a Pi Pico, set as a debugger, with Pico tester installed. I can help you flash it, so contact me over Discord.
+ Your badge just might not work! This has been such a hard project, I haven't been able to double check every badge, you might just get one with a dead chip, tough luck. I have VERY few of these, so no replacements.
+ This is supposed to be fun, if you're not having fun soldering this, you shouldn't.

## Material list
1. Board
2. Display (0.42") ![Display](./images/display.jpg)
3. U2 (the real name is very long, I'm not pasting it here, but it's the chip-looking thing with 8 pins) ![U2](./images/u2.jpg)
4. Crystal ![Crystal](./images/crystal.jpg)
5. Main Cap ![Main Cap](./images/m_cap.jpg)
6. #6 Touch Pad Resistors ![TP Res](./images/res.jpg)
7. #4 Display Caps ![Disp Caps](./images/d_cap.jpg)
8. Headers (there are only 2, 2, and 3 required; you do not need all the header spaces)
9. 32 AWG Wire (lots of it, I recommend 3 different colours, I used red, yellow, and blue)
10. __FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX FLUX__

# Instructions
First, You're gonna want to solder top-side comps.

### Top
+ You will need the Touch Pad Resistors (TPR). Each TPR goes on the unmarked small pads on the board, they are all near their respective TP.
+ The main Cap is the only thing left on this side, that one is right next to the top right 3v3 pin. Do not short this one, we'll also be bodging some wires from here, later.
Now, let's flip to the back of the board for some easier parts to handle

### Bottom
+ You're going to want to solder U2 first, but be careful, the piece is bigger than the footprint, I recommend (committing a electrical sin) to bend the legs backwards, they should be facing inwards, and U2 should be above the ground a little bit, that's fine, as we are putting on the headers later. The little indent on U2 should be oriented to the white arrow on the board (see image below) ![U2 Orient](./images/u2_orient.jpg)
+ The crystal is a little bit harder, but not by much. It is found right below the FPC connector (see image below) and is non-polar. I recommend tilting it to a 45 degree angle, having one side facing towards you as you solder, or you could use rework or something. ![Crystal stuff](./images/crystal_add.jpg)
+ I'd like to point out really quick that there are a lot of "missing parts" on the board, solder points with nothing on them, this is not intentional, but at this point, everything on the board is done (with the exception of headers), everything off it requires the remaining parts
+ Solder the headers on, you can do the entire row, but if you're doing just 2,2,3 headers, the headers should look like this image... ![Headers](./images/headers.jpg)

## Bodge wires
One quick message to all you out there, the display bodging is not for the faint of heart, neither is connecting to the FPC pins, nor any of the rest of this. I recommend magnification for this section, I used +3.00 glasses and it worked well, anything else will do, too, but make sure the board is stationary. You will need a very fine tip for this stuff... and probably an afternoon.
### Display
This one is by far the hardest, so buckle up.
To start, apply solder to pins 1-4 on the display, none of the others quite yet. You need to solder the display caps onto these pins bridging 1-2, 3-4 (see below)<br>
![Disp Caps](./images/d_cap_add.jpg)<br>

Now, solder the pin 5 on the opposite side of the display, then 7, then 9, all the way to 15. For these, you need a Bodge wires on every one of them. No exceptions.
