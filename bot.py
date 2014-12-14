
from PIL import Image, ImageGrab, ImageOps
import os
from numpy import *
import math, operator
import time
import ctypes
import win32gui
import win32com
import win32com.client
import sys
import pythoncom, pyHook
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
    key_dict = {'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48,
                'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50,
                'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58,
                'y':0x59, 'z':0x5A, 'up':0x26, 'down':0x28, 'right':0x27, 'left':0x25, 'enter':0x0D,
                '1':0x31, '2':0x32, '3':0x33, '4':0x34}
    newKey = key_dict.get(key)
    PressKey(newKey)
    #time.sleep(0.01)
    ReleaseKey(newKey)




def grab():
    #coordinates for text box where info is given about the order
    box = (453, 822, 1315, 979)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '\\box0.png', 'PNG')
    return img



#<---------------------Begin cooking recipes--------------------------->
def TheRedDog():
    #sends an alt key then selects the game window
    #I might need to set the the game ID to a variable since idk if it changes or if I can leave it hard coded
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('k')
    time.sleep(0.1)
    hitKey('enter')

def TheYellowDog():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('m')
    time.sleep(0.1)
    hitKey('enter')

def TheClassicCornDog():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('k')
    time.sleep(0.1)
    hitKey('m')
    time.sleep(0.1)
    hitKey('enter')

def TheSweetTwist():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('b')
    time.sleep(0.1)
    hitKey('c')
    time.sleep(0.1)
    hitKey('enter')


def TheButteryCurves():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('b')
    time.sleep(0.1)
    hitKey('enter')

def CinnamonPretzel():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('c')
    time.sleep(0.1)
    hitKey('enter')

def TheDryTwister():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('enter')

def TheSaltyKnot():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')

def TheClassicPretzel():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('s')
    time.sleep(0.1)
    hitKey('b')
    time.sleep(0.1)
    hitKey('enter')

def LargeColaIce():
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

def MediumColaIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeDietIce():
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

def SmallColaIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('enter')

def SmallGrapeIce():
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

def SmallDietIce():
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

def SmallColaNoIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallWaterIce():
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

def SmallTeaIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('right')
    time.sleep(0.1)
    hitKey('i')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumGrapeIce():
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

def MediumDietIce():
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

def MediumColaNoIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def MediumWaterIce():
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

def MediumTeaIce():
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

def LargeGrapeIce():
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

def LargeColaNoIce():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('up')
    time.sleep(0.1)
    hitKey('up')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def LargeWaterIce():
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

def LargeTeaIce():
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

def JumboColaIce():
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

def JumboGrapeIce():
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

def JumboDietIce():
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

def JumboColaNoIce():
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

def JumboWaterIce():
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

def JumboTeaIce():
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

def JumboColaIceFlavorBlast():
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

def JumboGrapeIceFlavorBlast():
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

def JumboDietIceFlavorBlast():
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

def JumboColaNoIceFlavorBlast():
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

def JumboWaterIceFlavorBlast():
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

def JumboTeaIceFlavorBlast():
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

def SmallColaIceFlavorBlast():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('i')
    time.sleep(0.1)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallGrapeIceFlavorBlast():
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

def SmallDietIceFlavorBlast():
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

def SmallColaNoIceFlavorBlast():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('f')
    time.sleep(0.1)
    hitKey('down')
    time.sleep(0.1)
    hitKey('enter')

def SmallWaterIceFlavorBlast():
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

def SmallTeaIceFlavorBlast():
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

def MediumColaIceFlavorBlast():
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

def MediumGrapeIceFlavorBlast():
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

def MediumDietIceFlavorBlast():
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

def LargeColaIceFlavorBlast():
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

def LargeGrapeIceFlavorBlast():
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

def LargeDietIceFlavorBlast():
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


def FastFries():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    #hold down button for 3 seconds to cook fries
    PressKey(0x28)
    time.sleep(3)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('a')
    time.sleep(0.1)
    hitKey('enter')

def LiteFastFries():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(3)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('enter')

def GreyTailFish():
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

def TheBrewsky():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(1.40)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('enter')

def WorkTicketClean():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    hitKey('down')
    time.sleep(0.1)
    hitKey('s')

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


#----------------------End cooking recipes---------------------------->
#associated recipe names with the image location for said recipe
#also good for logging, it will print out whatever order its doing
recipe_dict = {'The Red Dog':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the red dog.png',
               'The Yellow Dog':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the yellow dog.png',
               'The Classic Corn dog':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the classic corn dog.png',
               'The Sweet Twist':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the sweet twist.png',
               'The Buttery Curves':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the buttery curves.png',
               'Cinnamon Pretzel':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\cinnamon pretzel.png',
               'The Dry Twister':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the dry twister.png',
               'The Salty Knot':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the salty knot.png',
               'The Classic Pretzel':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the classic pretzel.png',
               'Large Cola Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large cola ice.png',
               'Medium Cola Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium cola ice.png',
               'Large Diet Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large diet ice.png',
               'Small Cola Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small cola ice.png',
               'Small Grape Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small grape ice.png',
               'Small Diet Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small diet ice.png',
               'Small Cola No Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small cola no ice.png',
               'Small Water Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small water ice.png',
               'Small Tea Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\small tea ice.png',
               'Medium Grape Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium grape ice.png',
               'Medium Diet Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium diet ice.png',
               'Medium Cola No Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium cola no ice.png',
               'Medium Water Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium water ice.png',
               'Medium Tea Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\medium tea ice.png',
               'Large Grape Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large grape ice.png',
               'Large Cola No Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large cola no ice.png',
               'Large Water Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large water ice.png',
               'Large Tea Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\large tea ice.png',
               'Jumbo Cola Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\jumbo cola ice.png',
               'Fast Fries':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\fast fries.png',
               'Lite Fast Fries':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\lite fast fries.png',
               'Grey Fish Tail':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\grey fish tail.png',
               'The Brewsky':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\the brewsky.png',
               'Work Ticket (Clean)':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (clean).png',
               'Work Ticket (Trash)':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (trash).png',
               'Work Ticket (Rodents)':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (rodents).png',
               'Work Ticket (Dishes)':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\work ticket (dishes).png',
               'Classic Steak':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\\classic steak.png',
               'Citrus Steak':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\citrus streak.png',
               'Jumbo Grape Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo grape ice.png',
               'Jumbo Diet Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo diet ice.png',
               'Jumbo Cola No Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola no ice.png',
               'Jumbo Water Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo water ice.png',
               'Jumbo Tea Ice':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo tea ice.png',
               'Jumbo Cola Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola ice flavor blast.png',
               'Jumbo Grape Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo grape ice flavor blast.png',
               'Jumbo Diet Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo diet ice flavor blast.png',
               'Jumbo Cola No Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo cola no ice flavor blast.png',
               'Jumbo Water Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo water ice flavor blast.png',
               'Jumbo Tea Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\jumbo tea ice flavor blast.png',
               'Small Cola Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small cola ice flavor blast.png',
               'Small Grape Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small grape ice flavor blast.png',
               'Small Diet Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small diet ice flavor blast.png',
               'Small Cola No Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small cola no ice flavor blast.png',
               'Small Water Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small water ice flavor blast.png',
               'Small Tea Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\small tea ice flavor blast.png',
               'Medium Cola Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium cola ice flavor blast.png',
               'Medium Grape Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium grape ice flavor blast.png',
               'Medium Diet Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\medium diet ice flavor blast.png',
               'Large Cola Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large cola ice flavor blast.png',
               'Large Grape Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large grape ice flavor blast.png',
               'Large Diet Ice Flavor Blast':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\recipes\large diet ice flavor blast.png'}
#I took out the "()" from the functions otherwise when the dict was initialized all the functions would get called
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

numkeys = {'1':[65, 133, 114, 198], '2':[65, 221, 119, 284], '3':[66, 303, 115, 364], '4':[65, 391, 121, 450],
           '5':[64, 472, 115, 536], '6':[64, 556, 118, 619], '7':[66, 645, 117, 706], '8':[64, 728, 120, 791]}
numImages = {'1':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num1.png',
             '2':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num2.png',
             '3':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num3.png',
             '4':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num4.png',
             '5':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num5.png',
             '6':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num6.png',
             '7':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num7.png',
             '8':'C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\numkeys\\num8.png'}

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
            n2 = Image.open('C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\num.png').histogram()
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
                    h2 = Image.open("C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\box0.png").histogram()
                    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
                    print rms

                    #I could probable set this to 0
                    if rms < 5:
                        print recipe
                        #used for cooking recipes
                        cooking_numbers_new.append(number)
                        #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                        cooking_dict[recipe]()
                        del cooking_numbers_new[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time




def compare_images():
    #get for loop to stop searching after it finds the correct image to improve performance
    time.sleep(0.05)
    for number in numkeys:
        grab_numkeys(number)
        #image taken from training set
        n1 = Image.open(numImages.get(number)).histogram()
        #image to verify
        n2 = Image.open('C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\num.png').histogram()
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
                h2 = Image.open("C:\Users\Ron\Documents\MEGA\Codding_projects\Game cheating\Cook, time, delicious\\box0.png").histogram()
                rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
                print rms

                #I could probably set this to 0
                if rms < 5:
                    print recipe
                    #used for cooking recipes
                    cooking_numbers.append(number)
                    #search cooking_dict for the recipe then call that function which will execute the steps to the recipe and serve the customer
                    cooking_dict[recipe]()
                    del cooking_numbers[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time
                    #Maybe the break can optimize the search by ending the dictionary loop after it finds the right answer
                    #break







time.sleep(1)

for i in xrange(10000):
    compare_images()





#grab()