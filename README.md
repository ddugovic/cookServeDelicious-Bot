cookServeDelicious-Bot
======================

This project is a simple bot that plays Cook, Serve, Delicious! 

It's a simple image recognition bot that uses image histograms and emulated keypresses to play the game.

The bot starts by looking for orders. It does this by going through the numbers 1 through 8 that are on the top right hand
corner of the screen. When it finds one that is illuminated it presses that key. Next it takes another screenshot
to compare with it's dictionary of cooking recipes. Once it finds the correct recipe it calls that function and the order
is completed. Then the loop starts again and it continues doing the same thing.


Requirements to test bot:

- 1920 x 1080 resolution fullscreen windowed mode on high settings
- you need to modify all the hard coded directories I use for the images
- windows OS (I use a few windows only librairies)
- Once you changed all the hard coded image locations simply run bot_threading.py (bot_oop.py is completed yet)


# Video of the bot in action
https://vid.me/iquy

Tested on python 2.7 on windows 7

#TODO
merge bot_oop.py with bot_threading.py
