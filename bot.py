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
    #keys need to be inputed as a string
    #press and release key instantly
    print "HIT ", key
    key_dict = {'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
                'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50,
                'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58,
                'y':0x59, 'z':0x5A, 'up':0x26, 'down':0x28, 'right':0x27, 'left':0x25, 'enter':0x0D,
                '1':0x31, '2':0x32, '3':0x33, '4':0x34, '5':0x35, '6':0x36, '7':0x37, '8':0x38}
    newKey = key_dict.get(key)
    PressKey(newKey)
    #time.sleep(0.01)
    ReleaseKey(newKey)

def grab():
    #coordinates for text box where info is given about the order
    box = (285, 565, 1015, 690)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '/box0.png', 'PNG')
    return img


#<---------------------Begin cooking recipes--------------------------->
def TheRedDog(text):
    #sends an alt key then selects the game window
    #I might need to set the the game ID to a variable since idk if it changes or if I can leave it hard coded
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('k')
    time.sleep(0.1)
    hitKey('enter')

def TheYellowDog(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('m')
    time.sleep(0.1)
    hitKey('enter')

def TheClassicCornDog(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('k')
    time.sleep(0.1)
    hitKey('m')
    time.sleep(0.1)
    hitKey('enter')

def TheSweetTwist(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('b')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('enter')

def TheButteryCurves(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('b')
    time.sleep(0.1)
    hitKey('enter')

def CinnamonPretzel(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('c')
    time.sleep(0.1)
    hitKey('enter')

def TheDryTwister(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('enter')

def TheSaltyKnot(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')

def TheClassicPretzel(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('b')
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

def LargeColaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumColaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeDietIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallColaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('enter')

def SmallGrapeIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallDietIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallColaNoIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallWaterIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallTeaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumGrapeIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumDietIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumColaNoIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumWaterIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumTeaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeGrapeIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeColaNoIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeWaterIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeTeaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboColaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboGrapeIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboDietIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboColaNoIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboWaterIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboTeaIce(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboColaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboGrapeIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboDietIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboColaNoIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('enter')

def JumboWaterIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def JumboTeaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallColaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallGrapeIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallDietIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallColaNoIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallWaterIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallTeaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumColaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumGrapeIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumDietIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeColaIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeGrapeIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeDietIceFlavorBlast(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('right')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')


def GoldenFriedChicken(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(3.6)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
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
    cooking_timer.append(8.5)
    compare_imagesCooking()

    #use variable to find the #key that was previously selected
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

def TheBrewsky(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(1.40)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('enter')

def WorkTicketClean(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)

def WorkTicketTrash(text):
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
    hitKey('s')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.3)
    hitKey('right')
    time.sleep(0.3)

def WorkTicketRodents(text):
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('s')
    time.sleep(0.1)

def WorkTicketDishes(text):
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
    cooking_timer.append(7.0)
    compare_imagesCooking()
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

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
    cooking_timer.append(17.70)
    compare_imagesCooking()
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

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
    cooking_timer.append(17.70)
    #start main loop again so I can start serving customers
    compare_imagesCooking()
    #But ommit "number" variable so it doesen't click on the food that is cooking
    #once timer ends cancel whatever is happening and return to this function which will then resume the original loop
    #cooking_number gets deleted then compare image loop is repeated
    hitKey(str(cooking_numbers[0]))
    del cooking_timer[:]

def ThumbsUp(text):
    hitKey('t')
    time.sleep(0.1)


#----------------------End cooking recipes---------------------------->
cooking_list = ['The Gerstmann',
                'The Red Dog',
                'The Yellow Dog',
                'The Classic Corn Dog',
                'Trio of Delicious',
                'Minty Deluxe',
                'The Yin and Yang',
                'Vanilla',
                'Chocolate',
                'Mint',
                'The Sweet Twist',
                'The Buttery Curves',
                'Cinnamon Pretzel',
                'The Dry Twister',
                'The Salty Knot',
                'The Classic Pretzel',
                'Golden Fried Chicken',
                'Sopapillas',
                'Mix Fries',
                'Fries',
                'Hash Patties',
                'Grey Tail Fish',
                'The Brewsky',
                'The Rich Brewsky',
                'Work Ticket (Clean)',
                'Work Ticket (Dishes)',
                'Work Ticket (Rodents)',
                'Work Ticket (Trash)',
                'Coffee',
                'Marzu',
                'Serpent',
                'Wine',
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
                'Classic Steak',
                'Citrus Steak',
                'Jumbo Cola No Ice w/Flavor Blast',
                'Small Cola No Ice w/Flavor Blast',
                'Jumbo Cola No Ice',
                'Small Cola No Ice',
                'Medium Cola No Ice',
                'Large Cola No Ice',
                'Jumbo Cola Ice w/Flavor Blast',
                'Jumbo Grape Ice w/Flavor Blast',
                'Jumbo Diet Ice w/Flavor Blast',
                'Jumbo Water Ice w/Flavor Blast',
                'Jumbo Tea Ice w/Flavor Blast',
                'Medium Cola Ice w/Flavor Blast',
                'Medium Grape Ice w/Flavor Blast',
                'Medium Diet Ice w/Flavor Blast',
                'Large Cola Ice w/Flavor Blast',
                'Large Grape Ice w/Flavor Blast',
                'Large Diet Ice w/Flavor Blast',
                'Small Cola Ice w/Flavor Blast',
                'Small Grape Ice w/Flavor Blast',
                'Small Diet Ice w/Flavor Blast',
                'Small Water Ice w/Flavor Blast',
                'Small Tea Ice w/Flavor Blast',
                'Large Cola Ice',
                'Medium Cola Ice',
                'Large Diet Ice',
                'Small Cola Ice',
                'Small Grape Ice',
                'Small Diet Ice',
                'Small Water Ice',
                'Small Tea Ice',
                'Medium Grape Ice',
                'Medium Diet Ice',
                'Medium Water Ice',
                'Medium Tea Ice',
                'Large Grape Ice',
                'Large Water Ice',
                'Large Tea Ice',
                'Jumbo Cola Ice',
                'Jumbo Grape Ice',
                'Jumbo Diet Ice',
                'Jumbo Water Ice',
                'Jumbo Tea Ice',
                'Check Out My Picture']

#also good for logging, it will print out whatever order its doing
#I took out the "()" from the functions otherwise when the dict was initialized all the functions would get called
cooking_dict = {'The Gerstmann':TheRedDog,
                'The Red Dog':TheRedDog,
                'The Yellow Dog':TheYellowDog,
                'The Classic Corn Dog':TheClassicCornDog,
                'Trio of Delicious':IceCreamTrio,
                'Minty Deluxe':IceCreamMintyDeluxe,
                'The Yin and Yang':IceCreamYinAndYang,
                'Vanilla':IceCream,
                'Chocolate':IceCream,
                'Mint':IceCream,
                'The Sweet Twist':TheSweetTwist,
                'The Buttery Curves':TheButteryCurves,
                'Cinnamon Pretzel':CinnamonPretzel,
                'The Dry Twister':TheDryTwister,
                'The Salty Knot':TheSaltyKnot,
                'The Classic Pretzel':TheClassicPretzel,
                'Golden Fried Chicken':GoldenFriedChicken,
                'Sopapillas':Fries,
                'Mix Fries':MixFries,
                'Fries':Fries,
                'Hash Patties':Fries,
                'Grey Tail Fish':GreyTailFish,
                'The Brewsky':TheBrewsky,
                'The Rich Brewsky':TheBrewsky,
                'Work Ticket (Clean)':WorkTicketClean,
                'Work Ticket (Dishes)':WorkTicketDishes,
                'Work Ticket (Rodents)':WorkTicketRodents,
                'Work Ticket (Trash)':WorkTicketTrash,
                'Coffee':Coffee,
                'Marzu':Wine,
                'Serpent':Wine,
                'Wine':Wine,
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
                'Classic Steak':ClassicSteak,
                'Citrus Steak':CitrusSteak,
                'Jumbo Cola No Ice w/Flavor Blast':JumboColaNoIceFlavorBlast,
                'Small Cola No Ice w/Flavor Blast':SmallColaNoIceFlavorBlast,
                'Jumbo Cola No Ice':JumboColaNoIce,
                'Small Cola No Ice':SmallColaNoIce,
                'Medium Cola No Ice':MediumColaNoIce,
                'Large Cola No Ice':LargeColaNoIce,
                'Jumbo Cola Ice w/Flavor Blast':JumboColaIceFlavorBlast,
                'Jumbo Grape Ice w/Flavor Blast':JumboGrapeIceFlavorBlast,
                'Jumbo Diet Ice w/Flavor Blast':JumboDietIceFlavorBlast,
                'Jumbo Water Ice w/Flavor Blast':JumboWaterIceFlavorBlast,
                'Jumbo Tea Ice w/Flavor Blast':JumboTeaIceFlavorBlast,
                'Medium Cola Ice w/Flavor Blast':MediumColaIceFlavorBlast,
                'Medium Grape Ice w/Flavor Blast':MediumGrapeIceFlavorBlast,
                'Medium Diet Ice w/Flavor Blast':MediumDietIceFlavorBlast,
                'Large Cola Ice w/Flavor Blast':LargeColaIceFlavorBlast,
                'Large Grape Ice w/Flavor Blast':LargeGrapeIceFlavorBlast,
                'Large Diet Ice w/Flavor Blast':LargeDietIceFlavorBlast,
                'Small Cola Ice w/Flavor Blast':SmallColaIceFlavorBlast,
                'Small Grape Ice w/Flavor Blast':SmallGrapeIceFlavorBlast,
                'Small Diet Ice w/Flavor Blast':SmallDietIceFlavorBlast,
                'Small Water Ice w/Flavor Blast':SmallWaterIceFlavorBlast,
                'Small Tea Ice w/Flavor Blast':SmallTeaIceFlavorBlast,
                'Large Cola Ice':LargeColaIce,
                'Medium Cola Ice':MediumColaIce,
                'Large Diet Ice':LargeDietIce,
                'Small Cola Ice':SmallColaIce,
                'Small Grape Ice':SmallGrapeIce,
                'Small Diet Ice':SmallDietIce,
                'Small Water Ice':SmallWaterIce,
                'Small Tea Ice':SmallTeaIce,
                'Medium Grape Ice':MediumGrapeIce,
                'Medium Diet Ice':MediumDietIce,
                'Medium Water Ice':MediumWaterIce,
                'Medium Tea Ice':MediumTeaIce,
                'Large Grape Ice':LargeGrapeIce,
                'Large Water Ice':LargeWaterIce,
                'Large Tea Ice':LargeTeaIce,
                'Jumbo Cola Ice':JumboColaIce,
                'Jumbo Grape Ice':JumboGrapeIce,
                'Jumbo Diet Ice':JumboDietIce,
                'Jumbo Water Ice':JumboWaterIce,
                'Jumbo Tea Ice':JumboTeaIce,
                'Check Out My Picture':ThumbsUp}

numkeys = {'1':[20,  95, 70, 145], '2':[20, 155, 70, 205], '3':[20, 210, 70, 260], '4':[20, 270, 70, 320],
           '5':[20, 330, 70, 380], '6':[20, 385, 70, 435], '7':[20, 445, 70, 495], '8':[20, 505, 70, 555]}

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
                im = Image.open('box0.png')
                text = image_to_string(im,"eng")
                print text
                #possible match from cooking_list
                for recipe in cooking_list:
                    if recipe.upper().replace(" ICE","") in text.replace(" ICE",""):
                        print recipe
                for recipe in cooking_list:
                    if recipe.upper().replace(" ICE","") in text.replace(" ICE",""):
                        print recipe
                        #print image_to_string(h2)
                        #used for cooking recipes
                        cooking_numbers_new.append(number)
                        #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                        cooking_dict[recipe](text.replace(" ",""))
                        del cooking_numbers_new[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time


def compare_images():
    time.sleep(0.05)
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
            im = Image.open('box0.png')
            text = image_to_string(im,"eng").replace("(no ice)","no ice").replace(" wi"," w/").replace(" wl"," w/").upper().replace("FIAVOR","FLAVOR")
            print text
            #possible match from cooking_list
            for recipe in cooking_list:
                if recipe.upper().replace(" ICE","") in text.replace(" ICE",""):
                    print recipe
            for recipe in cooking_list:
                if recipe.upper().replace(" ICE","") in text.replace(" ICE",""):
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
