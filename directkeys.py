# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import time
from pynput.keyboard import Key,Controller
import pyautogui


W = "w"
A = "a"
S = "s"
D = "d"

NP_2 = "2"
NP_4 = "4"
NP_6 = "6"
NP_8 = "8"

# Actuals Functions

def PressKey(hexKeyCode,keyboard = Controller()):    
    keyboard.press(hexKeyCode)    


def ReleaseKey(hexKeyCode,keyboard = Controller()):
    keyboard.release(hexKeyCode)
