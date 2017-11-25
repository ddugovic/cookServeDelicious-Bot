
from PIL import Image, ImageGrab, ImageOps
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
    box = (434, 854, 1296, 1011)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '/box0.png', 'PNG')
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


def GoldenFriedChicken():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(4)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('enter')

def Fries():
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

def LiteFries():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(3)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('enter')

def MixFries():
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
    hitKey('s')
    time.sleep(0.1)
    hitKey('enter')

def SeaFries():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    PressKey(0x28)
    time.sleep(3)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('e')
    time.sleep(0.1)
    hitKey('enter')

def SweetFries():
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    #hold down button for 3 seconds to cook fries
    PressKey(0x28)
    time.sleep(3)
    ReleaseKey(0x28)
    time.sleep(0.1)
    hitKey('p')
    time.sleep(0.1)
    hitKey('s')
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
    #WorkTicketDishes()
    #WorkTicketTrash()
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
    #hitKey('up')
    #time.sleep(0.3)
    #hitKey('right')
    #time.sleep(0.3)
    #hitKey('up')
    #time.sleep(0.3)
    #hitKey('right')
    #time.sleep(0.3)
    #hitKey('up')
    #time.sleep(0.3)
    #hitKey('right')
    #time.sleep(0.3)
    hitKey('s')

def WorkTicketRodents():
    #WorkTicketDishes()
    #WorkTicketTrash()
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

def ThumbsUp():
    hitKey('t')


#----------------------End cooking recipes---------------------------->
cooking_list = ['The Red Dog',
                'The Yellow Dog',
                'The Classic Corn Dog',
                'The Sweet Twist',
                'The Buttery Curves',
                'Cinnamon Pretzel',
                'The Dry Twister',
                'The Salty Knot',
                'The Classic Pretzel',
                'Golden Fried Chicken',
                'Delicious Lite Sopapillas',
                'Delicious Sopapillas',
                'Lite Fries',
                'Mix Fries',
                'Sea Fries',
                'Sweetest Potato Fries',
                'Fries',
                'Grey Tail Fish',
                'The Brewsky',
                'The Rich Brewsky',
                'Work Ticket (Clean)',
                'Work Ticket (Dishes)',
                'Work Ticket (Rodents)',
                'Work Ticket (Trash)',
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
cooking_dict = {'The Red Dog':TheRedDog,
                'The Yellow Dog':TheYellowDog,
                'The Classic Corn Dog':TheClassicCornDog,
                'The Sweet Twist':TheSweetTwist,
                'The Buttery Curves':TheButteryCurves,
                'Cinnamon Pretzel':CinnamonPretzel,
                'The Dry Twister':TheDryTwister,
                'The Salty Knot':TheSaltyKnot,
                'The Classic Pretzel':TheClassicPretzel,
                'Golden Fried Chicken':GoldenFriedChicken,
                'Delicious Lite Sopapillas':LiteFries,
                'Delicious Sopapillas':SweetFries,
                'Lite Fries':LiteFries,
                'Mix Fries':MixFries,
                'Sea Fries':SeaFries,
                'Sweetest Potato Fries':SweetFries,
                'Fries':Fries,
                'Grey Tail Fish':GreyTailFish,
                'The Brewsky':TheBrewsky,
                'The Rich Brewsky':TheBrewsky,
                'Work Ticket (Clean)':WorkTicketClean,
                'Work Ticket (Dishes)':WorkTicketDishes,
                'Work Ticket (Rodents)':WorkTicketRodents,
                'Work Ticket (Trash)':WorkTicketTrash,
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

numkeys = {'1':[35, 135, 105, 215], '2':[35, 221, 105, 284], '3':[35, 303, 105, 364], '4':[35, 391, 105, 450],
           '5':[35, 472, 105, 536], '6':[35, 556, 105, 619], '7':[35, 645, 105, 706], '8':[35, 728, 105, 791]}
numImages = {'1':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num1.png',
             '2':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num2.png',
             '3':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num3.png',
             '4':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num4.png',
             '5':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num5.png',
             '6':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num6.png',
             '7':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num7.png',
             '8':'C:/Users/Gaming/Desktop/cookServeDelicious-Bot/numkeys/num8.png'}

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
            n1 = numImages.get(number) #threshold
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
                text = image_to_string(im)
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
                        cooking_dict[recipe]()
                        del cooking_numbers_new[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time




def compare_images():
    #get for loop to stop searching after it finds the correct image to improve performance
    time.sleep(0.05)
    for number in numkeys:
        grab_numkeys(number)
        #image taken from training set
        n1 = numImages.get(number) #threshold
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
            text = image_to_string(im).replace("(no ice)","no ice").replace(" wi"," w/").replace(" wl"," w/").upper().replace("FIAVOR","FLAVOR")
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
                    cooking_dict[recipe]()
                    del cooking_numbers[:] #used to clear list. otherwise it will get filed with numbers when I only want 1 in there at a time
                    #Maybe the break can optimize the search by ending the dictionary loop after it finds the right answer
                    break

time.sleep(1)

while 1:
    compare_images()
