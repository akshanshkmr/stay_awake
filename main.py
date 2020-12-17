"""
Utility Script to prevent PC from going to sleep
by continouusly moving mouse pointer

[IMP]: to exit the script before specified time, move the mouse pointer into any corner

Author: Akshansh kumar 20201216 
"""

import pyautogui
import time
import sys
from datetime import datetime

def draw_rect(initx,inity,finx,finy,speed):
    for x in range(initx,finx,speed):
        pyautogui.moveTo(x,inity)
    for y in range(inity,finy,speed):
        pyautogui.moveTo(finx,y)
    for x in range(finx,initx,-speed):
        pyautogui.moveTo(x,finy)
    for y in range(finy,inity,-speed):
        pyautogui.moveTo(initx,y)

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    # rectangle vertices
    resolution = pyautogui.size()
    initx = int(resolution.width/3)
    finx =  int(resolution.width*2/3)
    inity = int(resolution.height/3)
    finy =  int(resolution.height*2/3)
    speed = 30

    duration = int(input("How long till we see you again?(in minutes): "))

    t_end=time.time()+duration*60
    print("Script run at {}".format(datetime.now().time()))
    print("Move the mouse pointer, into any corner to exit")
    while time.time()<t_end:
        try:
            draw_rect(initx,inity,finx,finy,speed)
        except:
            print("Script stopped by user at {}".format(datetime.now().time()))
            sys.exit(0)
    print("Script automatically stopped at {}".format(datetime.now().time()))