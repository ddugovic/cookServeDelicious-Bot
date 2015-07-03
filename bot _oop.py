
from PIL import Image, ImageGrab, ImageOps
import os
from numpy import *
import math
import operator
import time
import ctypes
import win32gui
import win32com
import win32com.client
import sys
import threading
import copy

SendInput = ctypes.windll.user32.SendInput
shell = win32com.client.Dispatch('WScript.Shell')
window = win32gui.FindWindow(0, 'Cook, Serve, Delicious!')


# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actual Functions

def PressKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



def hitKey(key):
    # keys need to be inputed as a string
    # press and release key instantly
    key_dict = {'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
                'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50,
                'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58,
                'y':0x59, 'z':0x5A, 'up':0x26, 'down':0x28, 'right':0x27, 'left':0x25, 'enter':0x0D,
                '1':0x31, '2':0x32, '3':0x33, '4':0x34}
    newKey = key_dict.get(key)
    time.sleep(0.1)
    PressKey(newKey)
    time.sleep(0.1)
    ReleaseKey(newKey)




def grab():
    # coordinates for text box where info is given about the order
    box = (453, 822, 1315, 979)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '\\box0.png', 'PNG')
    return img

# <---------------------Begin cooking recipes---------------------->
class CookingRecipes(object):
    """Used for most recipes. Uses default value of None
    for recipes that don't require extra parameters

    Supports:
    Simple recipes
    Recipes that require cooking time

    Sleep Timer Test:
    a = [1,2,3,4,5,6]
    b = a
    for i in range(1, len(a)+4, 2):
    b.insert(i, 'sleep')
    print b


    Eval not evaluating expressions properly
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    def __init__(self, keys, cooking_time=None, no_pos=None, sleep_time=5):
        self.sleep_time = sleep_time
        self.sendkeys = shell.SendKeys('%')
        self.setforeground = win32gui.SetForegroundWindow(window)
        # 1 less sleep timer than total of commands
        # Set to a string to is doesn't run when its instanciated
        # sleep_timers = ['time.sleep(sleep_time)' for i in len(keys)-1]
        self.keys = ['hitKey(key)' for key in keys]
        keys_sleep = self.keys
        # the +4 to the length is needed to insert enough sleep timers
        # +4 will need to be changed since the len of commands isn't always the same
        for i in range(1, len(self.keys)+4, 2):
            keys_sleep.insert(i, 'time.sleep(sleep_time)')
        print keys_sleep
        for i in keys_sleep:
            print "Evaluating..."
            eval(i)
            print i
        # self.keys = [hitKey(key) for key in keys]
        self.cooking_time = cooking_time
        self.no_pos = no_pos
        if self.cooking_time is not None:
            time.sleep(self.cooking_time)
            index = cooking_numbers.index(no_pos)
            hitKey(str(cooking_numbers[index]))
            cooking_numbers.pop(index)
            time.sleep(0.1)



class CustomRecipes0(object):
    """Used mostly for recipes that require holding down keys"""
    def __init__(self, press_key, sleep_time, release_key, keys):
        self.sendkeys = shell.SendKeys('%')
        self.setforeground = win32gui.SetForegroundWindow(window)
        self.pressKey = PressKey(press_key)
        self.sleep = time.sleep(sleep_time)
        self.releaseKey = ReleaseKey(release_key)
        self.keys = [hitKey(key) for key in keys]

class CookingThreading(object):
    """Food is the Target and no_pos the args"""
    def __init__(self, no_pos, food):
        self.no_pos = no_pos
        self.food = food
        t = threading.Thread(target=self.food, args=(no_pos,))
        t.start()



TheRedDog = "CookingRecipes(['k', 'enter'])"
TheYellowDog = "CookingRecipes(['m', 'enter'])"
TheClassicCornDog = "CookingRecipes(['k', 'm', 'enter'])"
TheSweetTwist = "CookingRecipes(['b', 'c', 'enter'])"
TheButteryCurves = "CookingRecipes(['b', 'enter'])"
CinnamonPretzel = "CookingRecipes(['c', 'enter'])"
TheDryTwister = "CookingRecipes(['enter'])"
TheSaltyKnot = "CookingRecipes(['s', 'enter'])"
TheClassicPretzel = "CookingRecipes(['s', 'b', 'enter'])"
LargeColaIce = "CookingRecipes(['up', 'up', 'i', 'down', 'enter'])"
MediumColaIce = "CookingRecipes(['up', 'i', 'down', 'enter'])"
LargeDietIce = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'up', 'i', 'down', 'enter'])"
SmallColaIce = "CookingRecipes(['down', 'i', 'enter'])"
SmallGrapeIce = "CookingRecipes(['right', 'right', 'i', 'down', 'enter'])"
SmallDietIce = "CookingRecipes(['right', 'right', 'right', 'right', 'i', 'down', 'enter'])"
SmallColaNoIce = "CookingRecipes(['down', 'enter'])"
SmallWaterIce = "CookingRecipes(['right', 'right', 'right', 'i', 'down', 'enter'])"
SmallTeaIce = "CookingRecipes(['right', 'i', 'down', 'enter'])"
MediumGrapeIce = "CookingRecipes[(['right', 'right', 'up', 'i', 'down'])]"
MediumDietIce = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'i', 'down', 'enter'])"
MediumColaNoIce = "CookingRecipes(['up', 'down', 'enter'])"
MediumWaterIce = "CookingRecipes(['right', 'right', 'right', 'up', 'i', 'down', 'enter'])"
MediumTeaIce = "CookingRecipes(['right', 'up', 'i', 'down', 'enter'])"
LargeGrapeIce = "CookingRecipes(['right', 'right', 'up', 'up', 'i', 'down', 'enter'])"
LargeColaNoIce = "CookingRecipes(['up', 'up', 'down', 'enter'])"
LargeWaterIce = "CookingRecipes(['right', 'right', 'right', 'up', 'up', 'i', 'down', 'enter'])"
LargeTeaIce = "CookingRecipes(['right', 'up', 'up', 'i', 'down', 'enter'])"
JumboColaIce = "CookingRecipes(['up', 'up', 'up', 'i', 'down', 'enter'])"
JumboGrapeIce = "CookingRecipes(['right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter'])"
JumboDietIce = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter'])"
JumboColaNoIce = "CookingRecipes(['up', 'up', 'up', 'down', 'enter'])"
JumboWaterIce = "CookingRecipes(['right', 'right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter'])"
JumboTeaIce = "CookingRecipes(['right', 'up', 'up', 'up', 'i', 'down', 'enter'])"
JumboColaIceFlavorBlast = "CookingRecipes(['up', 'up', 'up', 'i', 'f', 'down', 'enter'])"
JumboGrapeIceFlavorBlast = "CookingRecipes(['right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter'])"
JumboDietIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter'])"
JumboColaNoIceFlavorBlast = "CookingRecipes(['up', 'up', 'up', 'f', 'down', 'enter'])"
JumboWaterIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter'])"
JumboTeaIceFlavorBlast = "CookingRecipes(['right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter'])"
SmallColaIceFlavorBlast = "CookingRecipes(['i', 'f', 'down', 'enter'])"
SmallGrapeIceFlavorBlast = "CookingRecipes(['right', 'right', 'i', 'f', 'down', 'enter'])"
SmallDietIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'right', 'i', 'f', 'down', 'enter'])"
SmallColaNoIceFlavorBlast = "CookingRecipes(['f', 'down', 'enter'])"
SmallWaterIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'i', 'f', 'down', 'enter'])"
SmallTeaIceFlavorBlast = "CookingRecipes(['right', 'i', 'f', 'down', 'enter'])"
MediumColaIceFlavorBlast = "CookingRecipes(['up', 'i', 'f', 'down', 'enter'])"
MediumGrapeIceFlavorBlast = "CookingRecipes(['right', 'right', 'up', 'i', 'f', 'down', 'enter'])"
MediumDietIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'i', 'f', 'down', 'enter'])"
LargeColaIceFlavorBlast = "CookingRecipes(['up', 'up', 'i', 'f', 'down', 'enter'])"
LargeGrapeIceFlavorBlast = "CookingRecipes(['right', 'right', 'up', 'up', 'i', 'f', 'down', 'enter'])"
LargeDietIceFlavorBlast = "CookingRecipes(['right', 'right', 'right', 'right', 'up', 'up', 'i', 'f', 'down', 'enter'])"
FastFries = "CustomRecipes0(0x28, 3, 0x28, ['p', 'a', 'enter'])"
LiteFastFries = "CustomRecipes0(0x28, 3, 0x28, ['p', 'enter'])"

# threading function that calls the actual cooking function
GreyTailFish = lambda no_pos: CookingThreading(no_pos, GreyTailFishCook)
GreyTailFishCook = lambda no_pos: CookingRecipes(['left', 'right', 'down', 's', 'enter'], 8.5, no_pos)

TheBrewsky = "CustomRecipes0(0x28, 1.40, 0x28, ['enter'])"
WorkTicketClean = "CookingRecipes(['down', 's'])"
WorkTicketTrash = "CookingRecipes(['up', 'right', 'up', 'right', 'up', 'right', 'up', 'right', 'up', 'right', 's'])"
'''
def WorkTicketTrash():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)
    hitKey('s')
'''
def WorkTicketRodents():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('s')

def WorkTicketDishes():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)

def ClassicSteak():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('j')
    time.sleep(0.1)
    hitKey('enter')
    cooking_timer.append(17.70)
    compare_imagesCooking()
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

def CitrusSteak():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('j')
    time.sleep(0.1)
    hitKey('j')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('enter')
    # instead of doing a sleep which prevents me from running any code
    # I can just use a timer
    # I replace sleep with a variable with the identical time
    # I call my compare_imagesCook() function after I initialize the variable
    # and I use it as a timer to keep track of the food once the timer runs out I exit the function/loop
    # and continue in this function where I left off
    cooking_timer.append(17.70)
    # start main loop again so I can start serving customers
    compare_imagesCooking()
    # But ommit "number" variable so it doesn't click on the food that is cooking
    # once timer ends cancel whatever is happening and return to this function which will then resume the original loop
    # cooking_number gets deleted then compare image loop is repeated
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

# ----------------------End cooking recipes---------------------------->
# associated recipe names with the image location for said recipe
# also good for logging, it will print out whatever order its doing
recipe_dict = {'The Red Dog':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the red dog.png',
               'The Yellow Dog':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the yellow dog.png',
               'The Classic Corn dog':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the classic corn dog.png',
               'The Sweet Twist':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the sweet twist.png',
               'The Buttery Curves':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the buttery curves.png',
               'Cinnamon Pretzel':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\cinnamon pretzel.png',
               'The Dry Twister':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the dry twister.png',
               'The Salty Knot':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the salty knot.png',
               'The Classic Pretzel':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the classic pretzel.png',
               'Large Cola Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large cola ice.png',
               'Medium Cola Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium cola ice.png',
               'Large Diet Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large diet ice.png',
               'Small Cola Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small cola ice.png',
               'Small Grape Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small grape ice.png',
               'Small Diet Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small diet ice.png',
               'Small Cola No Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small cola no ice.png',
               'Small Water Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small water ice.png',
               'Small Tea Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small tea ice.png',
               'Medium Grape Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium grape ice.png',
               'Medium Diet Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium diet ice.png',
               'Medium Cola No Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium cola no ice.png',
               'Medium Water Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium water ice.png',
               'Medium Tea Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium tea ice.png',
               'Large Grape Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large grape ice.png',
               'Large Cola No Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large cola no ice.png',
               'Large Water Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large water ice.png',
               'Large Tea Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large tea ice.png',
               'Jumbo Cola Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\jumbo cola ice.png',
               'Fast Fries':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\fast fries.png',
               'Lite Fast Fries':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\lite fast fries.png',
               'Grey Fish Tail':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\grey fish tail.png',
               'The Brewsky':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the brewsky.png',
               'Work Ticket (Clean)':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (clean).png',
               'Work Ticket (Trash)':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (trash).png',
               'Work Ticket (Rodents)':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (rodents).png',
               'Work Ticket (Dishes)':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (dishes).png',
               'Classic Steak':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\classic steak.png',
               'Citrus Steak':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\citrus streak.png',
               'Jumbo Grape Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo grape ice.png',
               'Jumbo Diet Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo diet ice.png',
               'Jumbo Cola No Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola no ice.png',
               'Jumbo Water Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo water ice.png',
               'Jumbo Tea Ice':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo tea ice.png',
               'Jumbo Cola Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola ice flavor blast.png',
               'Jumbo Grape Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo grape ice flavor blast.png',
               'Jumbo Diet Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo diet ice flavor blast.png',
               'Jumbo Cola No Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola no ice flavor blast.png',
               'Jumbo Water Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo water ice flavor blast.png',
               'Jumbo Tea Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo tea ice flavor blast.png',
               'Small Cola Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small cola ice flavor blast.png',
               'Small Grape Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small grape ice flavor blast.png',
               'Small Diet Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small diet ice flavor blast.png',
               'Small Cola No Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small cola no ice flavor blast.png',
               'Small Water Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small water ice flavor blast.png',
               'Small Tea Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small tea ice flavor blast.png',
               'Medium Cola Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium cola ice flavor blast.png',
               'Medium Grape Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium grape ice flavor blast.png',
               'Medium Diet Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium diet ice flavor blast.png',
               'Large Cola Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large cola ice flavor blast.png',
               'Large Grape Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large grape ice flavor blast.png',
               'Large Diet Ice Flavor Blast':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large diet ice flavor blast.png'}
# I took out the "()" from the functions otherwise when the dict was initialized all the functions would get called
cooking_dict = {'The Red Dog':TheRedDog, 'The Yellow Dog':TheYellowDog, 'The Classic Corn dog':TheClassicCornDog, 'The Sweet Twist':TheSweetTwist,
                'The Buttery Curves':TheButteryCurves, 'Cinnamon Pretzel':CinnamonPretzel, 'The Dry Twister':TheDryTwister, 'The Salty Knot':TheSaltyKnot,
                'The Classic Pretzel':TheClassicPretzel, 'Large Cola Ice':LargeColaIce, 'Medium Cola Ice':MediumColaIce, 'Large Diet Ice':LargeDietIce,
                'Small Cola Ice':SmallColaIce, 'Small Grape Ice':SmallGrapeIce, 'Small Diet Ice':SmallDietIce, 'Small Cola No Ice':SmallColaNoIce,
                'Small Water Ice':SmallWaterIce, 'Small Tea Ice':SmallTeaIce, 'Medium Grape Ice':MediumGrapeIce, 'Medium Diet Ice':MediumDietIce,
                'Medium Cola No Ice':MediumColaNoIce, 'Medium Water Ice':MediumWaterIce, 'Medium Tea Ice':MediumTeaIce, 'Large Grape Ice':LargeGrapeIce,
                'Large Cola No Ice':LargeColaNoIce, 'Large Water Ice':LargeWaterIce, 'Large Tea Ice':LargeTeaIce, 'Fast Fries':FastFries, 'Lite Fast Fries':LiteFastFries,
                'Grey Fish Tail':GreyTailFish, 'The Brewsky':TheBrewsky, 'Work Ticket (Clean)':WorkTicketClean, 'Work Ticket (Trash)':WorkTicketTrash,
                'Work Ticket (Rodents)':WorkTicketRodents, 'Work Ticket (Dishes)':WorkTicketDishes, 'Classic Steak':ClassicSteak, 'Citrus Steak':CitrusSteak,
                'Jumbo Cola Ice':JumboColaIce, 'Jumbo Grape Ice':JumboGrapeIce, 'Jumbo Diet Ice':JumboDietIce, 'Jumbo Cola No Ice':JumboColaNoIce,
                'Jumbo Water Ice':JumboWaterIce, 'Jumbo Tea Ice':JumboTeaIce, 'Jumbo Cola Ice Flavor Blast':JumboColaIceFlavorBlast, 'Jumbo Grape Ice Flavor Blast':JumboGrapeIceFlavorBlast,
                'Jumbo Diet Ice Flavor Blast':JumboDietIceFlavorBlast, 'Jumbo Cola No Ice Flavor Blast':JumboColaNoIceFlavorBlast, 'Jumbo Water Ice Flavor Blast':JumboWaterIceFlavorBlast,
                'Jumbo Tea Ice Flavor Blast':JumboTeaIceFlavorBlast, 'Small Cola Ice Flavor Blast':SmallColaIceFlavorBlast, 'Small Grape Ice Flavor Blast':SmallGrapeIceFlavorBlast,
                'Small Diet Ice Flavor Blast':SmallDietIceFlavorBlast, 'Small Cola No Ice Flavor Blast':SmallColaNoIceFlavorBlast, 'Small Water Ice Flavor Blast':SmallWaterIceFlavorBlast,
                'Small Tea Ice Flavor Blast':SmallTeaIceFlavorBlast, 'Medium Cola Ice Flavor Blast':MediumColaIceFlavorBlast, 'Medium Grape Ice Flavor Blast':MediumGrapeIceFlavorBlast,
                'Medium Diet Ice Flavor Blast':MediumDietIceFlavorBlast, 'Large Cola Ice Flavor Blast':LargeColaIceFlavorBlast, 'Large Grape Ice Flavor Blast':LargeGrapeIceFlavorBlast,
                'Large Diet Ice Flavor Blast':LargeDietIceFlavorBlast}

# recipes that require cooking time
# these recipes are associated with lambda functions ONLY
cooking_recipes = ['Classic Steak', 'Citrus Steak', 'Grey Fish Tail']

numkeys = {'1':[65, 133, 114, 198], '2':[65, 221, 119, 284], '3':[66, 303, 115, 364], '4':[65, 391, 121, 450],
           '5':[64, 472, 115, 536], '6':[64, 556, 118, 619], '7':[66, 645, 117, 706], '8':[64, 728, 120, 791]}
numImages = {'1':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num1.png',
             '2':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num2.png',
             '3':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num3.png',
             '4':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num4.png',
             '5':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num5.png',
             '6':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num6.png',
             '7':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num7.png',
             '8':'C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num8.png'}

# Need global counter for cooking_numbers. Since I will be cooking
# multiple things at the same time each one will be associated with a different number
# the list will house multiple numbers each number represents a # 1 through 8 in game
# my global counter number will also be 1-8 but will be used as an index of positions
# i-e cooking_numbers[0] or cooking_numbers[3]
cooking_numbers = []

cooking_timer = []
def grab_numkeys(number):
        img = ImageGrab.grab(numkeys.get(number))
        img.save(os.getcwd() + '\\num.png', 'PNG')
        return img

def compare_imagesCooking():
    """Almost identical to compare_images() function. But used solely for food that requires cooking.
       As the food cooks this function is called to start serving other customers.
       It will ommit pressing the number of the customer it is already serving. i.e the food that is cooking.
       2nd is it returns to the cooking function after its timer has ended"""
    #will identical dict then remove the "number" variable from them
    numkeys_new = numkeys.copy()
    numImages_new = numImages.copy()
    cooking_numbers_new = list(cooking_numbers)
    #remove all numbers from new list so basically pop all numbers, can use a loop for this. List will have multiple
    # numbers since I will cook multiple thigns at once
    numkeys_new.pop(cooking_numbers[0], None)
    numImages_new.pop(cooking_numbers[0], None)
    time.sleep(0.05)
    start = time.time()
    while time.time() < start + cooking_timer[0]:
        print "Start temporary cooking loop..."
        for number in numkeys_new:
            grab_numkeys(number)
            #image taken from training set
            n1 = Image.open(numImages_new.get(number)).histogram()
            #image to verify
            n2 = Image.open('C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\num.png').histogram()
            rms0 = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, n1, n2))/len(n1))
            print number, rms0
            if rms0 < 5:
                hitKey(number)#click on selected number then screengrab recipe
                time.sleep(0.1)
                grab()#grabs image for recipe
                #possible match from recipe_dict
                for recipe in recipe_dict:
                    h1 = Image.open(recipe_dict.get(recipe)).histogram()
                    #image to verify
                    h2 = Image.open("C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\box0.png").histogram()
                    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
                    print rms

                    #I could probable set this to 0
                    if rms < 5:
                        print recipe
                        # used for cooking recipes
                        cooking_numbers_new.append(number)
                        #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                        eval(cooking_dict[recipe])
                        del cooking_numbers_new[:]  # used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time




def compare_images():
    time.sleep(0.05)
    numkeys_new = numkeys.copy()
    # numImages_new = numImages.copy()
    # removes cooking numbers that are currently being cooked
    numkeys_new = [x for x in numkeys_new if x not in cooking_numbers]
    for number in numkeys_new:
        grab_numkeys(number)
        # image taken from training set
        n1 = Image.open(numImages.get(number)).histogram()
        # image to verify
        n2 = Image.open('C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\num.png').histogram()
        rms0 = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, n1, n2))/len(n1))
        # print number, rms0
        if rms0 < 5:
            hitKey(number)# click on selected number then screengrab recipe
            time.sleep(0.1)
            grab()# grabs image for recipe
            # possible match from recipe_dict
            for recipe in recipe_dict:
                h1 = Image.open(recipe_dict.get(recipe)).histogram()
                # image to verify - is the screenshot it keeps taking
                h2 = Image.open("C:\Users\yoi\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\box0.png").histogram()
                rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
                # print rms

                # I could probably set this to 0
                if rms < 5:
                    print recipe
                    if recipe in cooking_recipes:   # I only want to append a cooking_number the recipes that require cooking time
                        cooking_numbers.append(number)
                        no_pos = number
                        print "Current %s" % no_pos
                        # search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                        # lambda function gets passed here
                        cooking_dict[recipe](no_pos)
                        # all cooking numbers are tracked within the list.

                    else:
                        # object in string gets passed here
                        eval(cooking_dict[recipe])









time.sleep(1)

while 1:
    compare_images()





#grab()
