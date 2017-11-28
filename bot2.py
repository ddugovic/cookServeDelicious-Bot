# -*- coding: utf-8 -*-
from PIL import Image, ImageGrab, ImageOps
import re
import os
from pytesser import *
from numpy import *
import math, operator
import time
import ctypes
import win32gui
import win32com
import win32com.client
import sys
# import pythoncom, pyHook
import threading
import copy

SendInput = ctypes.windll.user32.SendInput
shell = win32com.client.Dispatch('WScript.Shell')
window = win32gui.FindWindow(0, 'Cook, Serve, Delicious! 2!!')


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
    holdKey(key, 0.05)

def holdKey(key, d):
    #keys need to be inputed as a string
    #press and release key instantly
    print "HOLD ", key
    key_dict = {'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
                'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50,
                'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58,
                'y':0x59, 'z':0x5A, 'up':0x26, 'down':0x28, 'right':0x27, 'left':0x25, 'space':0x20, 'tab':0x09, 'enter':0x0D,
                '1':0x31, '2':0x32, '3':0x33, '4':0x34, '5':0x35, '6':0x36, '7':0x37, '8':0x38}
    newKey = key_dict.get(key)
    PressKey(newKey)
    time.sleep(d)
    ReleaseKey(newKey)

def holdKeyCombo(key, key2, d):
    #keys need to be inputed as a string
    #press and release key instantly
    print "HOLD ", key, key2
    key_dict = {'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
                'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50,
                'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58,
                'y':0x59, 'z':0x5A, 'up':0x26, 'down':0x28, 'right':0x27, 'left':0x25, 'space':0x20, 'tab':0x09, 'enter':0x0D,
                '1':0x31, '2':0x32, '3':0x33, '4':0x34, '5':0x35, '6':0x36, '7':0x37, '8':0x38}
    newKey = key_dict.get(key)
    newKey2 = key_dict.get(key2)
    PressKey(newKey)
    PressKey(newKey2)
    time.sleep(d)
    ReleaseKey(newKey)
    ReleaseKey(newKey2)

def grab():
    #grab2()
    #coordinates for text box where info is given about the order
    box = (300, 550, 1015, 660)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '/box1.png', 'PNG')
    return img

def grab2():
    #coordinates for text box where info is given about the order
    box2 = (1070, 110, 1280, 360)
    img2 = ImageGrab.grab(box2)
    img2.save(os.getcwd() + '/box2.png', 'PNG')
    return img2


#<---------------------Begin cooking recipes--------------------------->
def CornDog(text):
    #sends an alt key then selects the game window
    #I might need to set the the game ID to a variable since idk if it changes or if I can leave it hard coded
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('c')
    time.sleep(0.1)
    hitKey('l')
    time.sleep(0.1)
    hitKey('enter')

def DryDog(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('enter')

def Dog(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    if "WIENER" in text:
        hitKey('w')
        time.sleep(0.1)
    if "REGULAR" in text:
        hitKey('r')
        time.sleep(0.1)
        hitKey('space')
        time.sleep(0.1)
    elif "PREMIUM" in text:
        hitKey('p')
        time.sleep(0.1)
        hitKey('space')
        time.sleep(0.1)
    elif "PRETZEL" in text:
        hitKey('z')
        time.sleep(0.1)
        hitKey('space')
        time.sleep(0.1)
    if "KETCHUP" in text:
        hitKey('k')
        time.sleep(0.1)
    if "MUSTARD" in text:
        hitKey('m')
        time.sleep(0.1)
    if "ONIONS" in text:
        hitKey('o')
        time.sleep(0.1)
    if "RELISH" in text:
        hitKey('r')
        time.sleep(0.1)
    hitKey('enter')

def Pretzel(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    if "GERMAN" in text:
        hitKey('g')
    else:
        hitKey('c')
    time.sleep(0.1)
    hitKey('enter')

def IceCream(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    if "VANILLA" in text:
        if "TWO" in text:
            hitKey('v')
            time.sleep(0.1)
        elif "THREE" in text:
            hitKey('v')
            time.sleep(0.1)
            hitKey('v')
            time.sleep(0.1)
        hitKey('v')
        time.sleep(0.1)
    if "MINT" in text:
        if "TWO" in text:
            hitKey('m')
            time.sleep(0.1)
        elif "THREE" in text:
            hitKey('m')
            time.sleep(0.1)
            hitKey('m')
            time.sleep(0.1)
        hitKey('m')
        time.sleep(0.1)
    elif "CHOCOLATE" in text:
        if "TWO" in text:
            hitKey('c')
            time.sleep(0.1)
        elif "THREE" in text:
            hitKey('c')
            time.sleep(0.1)
            hitKey('c')
            time.sleep(0.1)
        hitKey('c')
        time.sleep(0.1)
    if "CHERRY" in text.replace("(HERRG", "CHERRY"):
        hitKey('h')
        time.sleep(0.1)
    if "SPRINKLES" in text:
        hitKey('p')
        time.sleep(0.1)
    if "WHIP" in text:
        hitKey('w')
        time.sleep(0.1)
    if "NUTTY" in text:
        hitKey('n')
        time.sleep(0.1)
    hitKey('enter')

def IceCreamMintyDeluxe(text):
    Snack('mmhwn')

def IceCreamTrio(text):
    Snack('vcm')

def IceCreamYinAndYang(text):
    Snack('vchp')

def Nuggets(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    for x in xrange(0, 4):
        hitKey('n')
        time.sleep(0.1)
    holdKey('d', 3.6)
    time.sleep(0.1)
    hitKey('enter')

def Fries(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    #hold down button for 3 seconds to cook fries
    PressKey(0x28)
    if "HASH" in text:
        time.sleep(2)
        if not "LITE" in text:
            text = "SUGAR"
    elif "SOPAPILLAS" in text:
        time.sleep(2.8)
        if "LITE" in text:
            text = "LITE"
    else:
        if "SWEETEST" in text:
            text += "LITE"
        time.sleep(2.8)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    if "SEA" in text:
        hitKey('e')
        time.sleep(0.1)
    elif not "LITE" in text:
        hitKey('a')
        time.sleep(0.1)
    if "SUGAR" in text:
        hitKey('s')
        time.sleep(0.1)
    hitKey('enter')

def MixFries(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    #hold down button for 3 seconds to cook fries
    PressKey(0x28)
    time.sleep(2.8)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('a')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')

def GreyTailFish(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('left')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    #cooking_timer.append(8.5)
    #compare_imagesCooking()

    #use variable to find the #key that was previously selected
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def TheBrewsky(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(1.40)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('enter')

def WorkTicketIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('o')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketRestroom(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('f')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketTrash(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('t')
    time.sleep(0.3)
    for x in xrange(0, 5):
        hitKey('m')
        time.sleep(0.3)
    hitKey('s')
    time.sleep(0.3)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketPests(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('t')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketRatTraps(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('l')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketRoachTraps(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('t')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def WorkTicketDishes(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('d')
    time.sleep(0.1)
    hitKey('w')
    time.sleep(0.1)
    hitKey('r')
    time.sleep(0.1)
    hitKey('u')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def Coffee(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    if "CREAMER" in text:
        hitKey('c')
        time.sleep(0.1)
    if "SUGARS" in text:
        m = re.search('([2-5])SUGARS', text.replace("ZSUGARS", "2SUGARS")+"4SUGARS")
        sugars = int(m.group(1))
        for x in xrange(0, sugars):
            hitKey('s')
            time.sleep(0.1)
    elif "SUGAR" in text:
        hitKey('s')
        time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def Wine(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    if "MARZU" in text:
        hitKey('w')
        time.sleep(0.1)
    if "SERPENT" in text:
        hitKey('w')
        time.sleep(0.1)
        hitKey('w')
        time.sleep(0.1)
    for x in xrange(0, 25):
        hitKey('up')
        time.sleep(0.05)
    hitKey('enter')
    time.sleep(0.1)

def Nachos(text):
    if "QUESO" in text.replace("UESO", "QUESO"):
        hitKey('q')
        time.sleep(0.1)
    if "CREAM" in text:
        hitKey('s')
        time.sleep(0.1)
    if "JALAPENO" in text.replace("ALAPENO", "JALAPENO"):
        hitKey('j')
        time.sleep(0.1)
    if "BEANS" in text.replace("EANS", "BEANS"):
        hitKey('b')
        time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def Snack(keys):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    for key in list(keys):
        hitKey(key)
        time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def Kabob(keys):
    Snack(keys)
    #cooking_timer.append(7.0)
    #compare_imagesCooking()
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def Kabobber(text):
    Kabob('tgrtmkmk')

def KabobChicken(text):
    Kabob('tktkgkrk')

def KabobClassic(text):
    Kabob('mtgrtgrk')

def KabobMeaty(text):
    Kabob('mkmtgkmk')

def KabobPepper(text):
    Kabob('grgrgrtm')

def KabobRed(text):
    Kabob('trtrtrgm')

def SushiEbiSpecial(text):
    Snack('eeeeertu')

def SushiMixedDelicious(text):
    Snack('eerrrttu')

def SushiOceanPlate(text):
    Snack('eeerrtuu')

def SushiRoeSpecial(text):
    Snack('eeerrrrt')

def SushiStandardSampler(text):
    Snack('eerrttuu')

def SushiSeaSpirit(text):
    Snack('errtttuu')

def SushiToroSpecial(text):
    Snack('ertttttu')

def SushiTunaPlatter(text):
    Snack('ertuuuuu')

def Salad(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    if "RANCH" in text:
        hitKey('r')
        time.sleep(0.1)
    if "THOUSAND" in text:
        hitKey('t')
        time.sleep(0.1)
    if "CHEESE" in text.replace("(BEE", "CHEESE"):
        hitKey('c')
        time.sleep(0.1)
    if "EVERYTHING" in text.replace("EVERGFHING", "EVERYTHING"):
        text = "BACON ONIONS MUSHROOMS GREENS"
    if "BACON" in text:
        hitKey('b')
        time.sleep(0.1)
    if "ONIONS" in text:
        hitKey('o')
        time.sleep(0.1)
    if "MUSHROOMS" in text.replace("MUSHROO∩¼é", "MUSHROOMS"):
        hitKey('m')
        time.sleep(0.1)
    if "GREENS" in text:
        hitKey('g')
        time.sleep(0.1)
    hitKey('enter')
    time.sleep(0.1)

def SaladTheManhattan(text):
    Snack('rcbomg')

def Sandwich(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    for x in xrange(0, 2):
        hitKey('m')
        time.sleep(0.1)
    if "BACON" in text:
        hitKey('b')
        time.sleep(0.1)
    if "BISCUIT" in text:
        hitKey('b')
        time.sleep(0.1)
    if "CHEESE" in text:
        hitKey('c')
        time.sleep(0.1)
    if "CROISSANT" in text:
        hitKey('c')
        time.sleep(0.1)
    if "EGG" in text:
        hitKey('e')
        time.sleep(0.1)
    if "LETTUCE" in text:
        hitKey('l')
        time.sleep(0.1)
    if "TOMATOES" in text:
        hitKey('t')
        time.sleep(0.1)
    if "SWISSCHEESE" in text:
        hitKey('s')
        time.sleep(0.1)
    hitKey('space')
    time.sleep(0.1)
    hitKey('r')
    time.sleep(0.1)
    hitKey('enter')
    cooking_timer.append(15.70)
    #compare_imagesCooking()
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def Patty(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    for x in xrange(0, 2):
        hitKey('m')
        time.sleep(0.1)
    if "BACON" in text:
        hitKey('b')
        time.sleep(0.1)
    if "CHEESE" in text:
        hitKey('c')
        time.sleep(0.1)
    if "EGG" in text:
        hitKey('f')
        time.sleep(0.1)
    if "LETTUCE" in text:
        hitKey('l')
        time.sleep(0.1)
    if "ONIONS" in text:
        hitKey('o')
        time.sleep(0.1)
    if "PICKLES" in text:
        hitKey('p')
        time.sleep(0.1)
    if "TOMATOES" in text:
        hitKey('t')
        time.sleep(0.1)
    if "SWISSCHEESE" in text:
        hitKey('s')
        time.sleep(0.1)
    hitKey('space')
    time.sleep(0.1)
    hitKey('r')
    time.sleep(0.1)
    hitKey('enter')
    #cooking_timer.append(15.70)
    #compare_imagesCooking()
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def ClassicSteak(text):
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
    #cooking_timer.append(17.70)
    #compare_imagesCooking()
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def CitrusSteak(text):
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
    #instead of doing a sleep which prevents me from running any code
    #I can just use a timer
    #I replace sleep with a variable with the identical time
    #I call my compare_imagesCook() function after I initialize the variable
    #and I use it as a timer to keep track of the food once the timer runs out I exit the function/loop
    #and continue in this function where I left off
    #cooking_timer.append(17.70)
    #start main loop again so I can start serving customers
    #compare_imagesCooking()
    #But ommit "number" variable so it doesen't click on the food that is cooking
    #once timer ends cancel whatever is happening and return to this function which will then resume the original loop
    #cooking_number gets deleted then compare image loop is repeated
    #hitKey(str(cooking_numbers[0]))
    #del cooking_timer[:]

def ThumbsUp(text):
    hitKey('t')
    time.sleep(0.1)


#----------------------End cooking recipes---------------------------->
cooking_list = ['Corndog',
                'The Gerstmann',
                'Dry Dog',
                'Dawg',
                'Dog',
                'Wiener',
                'Trio of Delicious',
                'Minty Deluxe',
                'The Yin and Yang',
                'Vanilla',
                'Chocolate',
                'Mint',
                'Nuggets',
                'Sopapillas',
                'Mix Fries',
                'Fries',
                'Hash Patties',
                'Grey Tail Fish',
                'The Brewsky',
                'The Rich Brewsky',
                'Work Ticket (Dishes)',
                'Ice',
                'Restroom',
                'Pests',
                'Rat Traps',
                'Roach Traps',
                'Trash',
                'Coffee',
                'Marzu',
                'Serpent',
                'Wine',
                'Nachos',
                'Chicken Kabob',
                'Kabobber',
                'Meaty Kabob',
                'Pepper Kabob',
                'Red Kabob',
                'Kabob',
                'Cheesy Leaves',
                'Pepper Ranch',
                'The Dry Greens',
                'The Dry Deluxe',
                'Kids Delight',
                'The Manhattan',
                'The Mix',
                'Tomato Ranch',
                'Cheesy Peppers',
                'Salad',
                'Thousand',
                'Ebi Special',
                'Mixed Delicious',
                'Ocean Plate',
                'Roe Special',
                'Sea Spirit',
                'Standard Sampler',
                'Toro Special',
                'Tuna Platter',
                'Patty',
                'Egg',
                'Ham',
                'Sausage',
                'Pretzel',
                'Classic Steak',
                'Citrus Steak',
                'Check Out My Picture']

#also good for logging, it will print out whatever order its doing
#I took out the "()" from the functions otherwise when the dict was initialized all the functions would get called
cooking_dict = {'Corndog':CornDog,
                'The Gerstmann':Dog,
                'Dry Dog':DryDog,
                'Dawg':Dog,
                'Dog':Dog,
                'Wiener':Dog,
                'Trio of Delicious':IceCreamTrio,
                'Minty Deluxe':IceCreamMintyDeluxe,
                'The Yin and Yang':IceCreamYinAndYang,
                'Vanilla':IceCream,
                'Chocolate':IceCream,
                'Mint':IceCream,
                'Nuggets':Nuggets,
                'Sopapillas':Fries,
                'Mix Fries':MixFries,
                'Fries':Fries,
                'Hash Patties':Fries,
                'Grey Tail Fish':GreyTailFish,
                'The Brewsky':TheBrewsky,
                'The Rich Brewsky':TheBrewsky,
                'Work Ticket (Dishes)':WorkTicketDishes,
                'Ice':WorkTicketIce,
                'Restroom':WorkTicketRestroom,
                'Pests':WorkTicketPests,
                'Rat Traps':WorkTicketRatTraps,
                'Roach Traps':WorkTicketRoachTraps,
                'Trash':WorkTicketTrash,
                'Coffee':Coffee,
                'Marzu':Wine,
                'Serpent':Wine,
                'Wine':Wine,
                'Nachos':Nachos,
                'Chicken Kabob':KabobChicken,
                'Kabobber':Kabobber,
                'Meaty Kabob':KabobMeaty,
                'Pepper Kabob':KabobPepper,
                'Red Kabob':KabobRed,
                'Kabob':KabobClassic,
                'Cheesy Leaves':Salad,
                'Pepper Ranch':Salad,
                'The Dry Greens':Salad,
                'The Dry Deluxe':Salad,
                'Kids Delight':Salad,
                'The Manhattan':SaladTheManhattan,
                'The Mix':Salad,
                'Tomato Ranch':Salad,
                'Cheesy Peppers':Salad,
                'Salad':Salad,
                'Thousand':Salad,
                'Ebi Special':SushiEbiSpecial,
                'Mixed Delicious':SushiMixedDelicious,
                'Ocean Plate':SushiOceanPlate,
                'Roe Special':SushiRoeSpecial,
                'Sea Spirit':SushiSeaSpirit,
                'Standard Sampler':SushiStandardSampler,
                'Toro Special':SushiToroSpecial,
                'Tuna Platter':SushiTunaPlatter,
                'Patty':Patty,
                'Egg':Sandwich,
                'Ham':Sandwich,
                'Sausage':Sandwich,
                'Pretzel':Pretzel,
                'Classic Steak':ClassicSteak,
                'Citrus Steak':CitrusSteak,
                'Check Out My Picture':ThumbsUp}

numkeys = {'1':[0,  70, 30, 105], '2':[0, 115, 30, 150], '3':[0, 160, 30, 195], '4':[0, 200, 30, 235],
           '5':[0, 250, 30, 290], '6':[0, 255, 30, 295], '7':[0, 300, 30, 340], '8':[0, 345, 30, 385]}

stations = {'S1':[220, 15, 250, 30], 'S2':[301, 15, 331, 30], 'S3':[382, 15, 412, 30], 'S4':[463, 15, 493, 30]}

#Need global counter for cooking_numbers. Since I will be cooking
#multiple things at the same time each one will be associated with a different number
#the list will house multiple numbers each number represents a # 1 through 8 in game
#my global counter number will also be 1-8 but will be used as an index of positions
#i-e cooking_numbers[0] or cooking_numbers[3]
cooking_numbers = []

cooking_timer = []
def grab_numkeys(number):
        img = ImageGrab.grab(numkeys.get(number))
        img.save(os.getcwd() + '/num.png', 'PNG')
        return img

def grab_stations(station):
        img = ImageGrab.grab(stations.get(station))
        img.save(os.getcwd() + '/station.png', 'PNG')
        return img

def compare_imagesCooking():
    """Almost identical to compare_images() function. But used solely for food that requires cooking.
       As the food cooks this function is called to start serving other customers.
       It will ommit pressing the number of the customer it is already serving. i.e the food that is cooking.
       2nd is it returns to the cooking function after its timer has ended"""
    #will identical dict then remove the "number" variable from them
    numkeys_new = numkeys.copy()
    cooking_numbers_new = list(cooking_numbers)
    #remove all numbers from new list so basically pop all numbers, can use a loop for this. List will have multiple
    # numbers since I will cook multiple thigns at once
    numkeys_new.pop(cooking_numbers[0], None)
    time.sleep(0.05)
    start = time.time()
    while time.time() < start + cooking_timer[0]:
        print "Start temporary cooking loop..."
        for number in numkeys_new:
            grab_numkeys(number)
            #image to verify
            n2 = Image.open('C:/Users/Gaming/Desktop/cookServeDelicious-Bot/num.png').histogram()
            b = 0
            for x in xrange(0, len(n2)):
                b += x * n2[x];
            avg = b / sum(n2)
            c = 0
            for x in xrange(0, len(n2)):
                c += (x - avg) * (x - avg) * n2[x]
            stdev = math.sqrt(c / sum(n2))
            #print number, stdev
            if stdev > 210:
                hitKey(number)#click on selected number then screengrab recipe
                time.sleep(0.1)
                grab()#grabs image for recipe
                im = Image.open('box1.png')
                text = image_to_string(im,"eng").upper().replace("DISH ES","DISHES").replace("DAG","DOG")
                print text
                #possible match from cooking_list
                for recipe in cooking_list:
                    if recipe.upper() in text:
                        print recipe
                for recipe in cooking_list:
                    if recipe.upper() in text:
                        print recipe
                        #print image_to_string(h2)
                        #used for cooking recipes
                        cooking_numbers_new.append(number)
                        #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                        cooking_dict[recipe](text.replace(" ",""))
                        del cooking_numbers_new[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time


def compare_images():
    time.sleep(0.05)
    grab()#grabs image for recipe
    im = Image.open('box1.png')
    text = image_to_string(im,"eng").upper().replace("DISH ES","DISHES").replace("DAG","DOG")
    for station in stations:
        grab_stations(station)
        #im2 = Image.open('box2.png')
        #text2 = image_to_string(im2,"eng").upper().replace("DISH ES","DISHES").replace("DAG","DOG")
        #image to verify
        n2 = Image.open('C:/Users/Gaming/Desktop/cookServeDelicious-Bot/station.png').histogram()
        b = 0
        for x in xrange(0, len(n2)):
            b += x * n2[x];
        avg = b / sum(n2)
        c = 0
        for x in xrange(0, len(n2)):
            c += (x - avg) * (x - avg) * n2[x]
        stdev = math.sqrt(c / sum(n2))
        #print station, stdev
        if stdev < 210:
            holdKeyCombo('tab', station[1], 0.05)
            time.sleep(0.05)
            if station == 'S3' or station == 'S4':
                hitKey('space')
                time.sleep(0.05)
            if station == 'S2' or station == 'S4':
                hitKey('b')
                time.sleep(0.05)
            hitKey('a')
            hitKey('space')
            time.sleep(0.05)
            #possible match from cooking_list
            for recipe in cooking_list:
                if recipe.upper() in text:
                   print recipe
            for recipe in cooking_list:
                if recipe.upper() in text:
                    print recipe
                    #used for cooking recipes
                    cooking_numbers.append(station)
                    #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                    cooking_dict[recipe](text.replace(" ",""))
                    cooking_dict[recipe](text.replace(" ",""))
                    cooking_dict[recipe](text.replace(" ",""))
                    cooking_dict[recipe](text.replace(" ",""))
                    del cooking_numbers[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time
                    #Maybe the break can optimize the search by ending the dictionary loop after it finds the right answer
                    break
    for number in numkeys:
        grab_numkeys(number)
        #image to verify
        n2 = Image.open('C:/Users/Gaming/Desktop/cookServeDelicious-Bot/num.png').histogram()
        b = 0
        for x in xrange(0, len(n2)):
            b += x * n2[x];
        avg = b / sum(n2)
        c = 0
        for x in xrange(0, len(n2)):
            c += (x - avg) * (x - avg) * n2[x]
        stdev = math.sqrt(c / sum(n2))
        #print number, stdev
        if stdev > 210:
            hitKey(number)#click on selected number then screengrab recipe
            time.sleep(0.1)
            grab()#grabs image for recipe
            im = Image.open('box1.png')
            text = image_to_string(im,"eng").upper().replace("DISH ES","DISHES").replace("DAG","DOG")
            print text
            #possible match from cooking_list
            for recipe in cooking_list:
                if recipe.upper() in text:
                    print recipe
            for recipe in cooking_list:
                if recipe.upper() in text:
                    print recipe
                    #used for cooking recipes
                    cooking_numbers.append(number)
                    #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                    cooking_dict[recipe](text.replace(" ",""))
                    del cooking_numbers[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time
                    #Maybe the break can optimize the search by ending the dictionary loop after it finds the right answer
                    break
    return

time.sleep(1)

while 1:
    compare_images()
