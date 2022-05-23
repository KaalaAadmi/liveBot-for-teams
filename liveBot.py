import mouse
import os
import time
import pyautogui
import math
import datetime

def openAndAvailable():
    # os.system("Microsoft Teams.exe")
    os.startfile(<link to your Teams shortcut>)
    time.sleep(8)

    mouse.on_click(lambda: print("Left Button clicked."))
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')

    # Radius 
    R = 200
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))

    # print(pyautogui.position())

def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end

while True:
    # checkTime()
    start = datetime.time(10, 0, 0)
    end = datetime.time(19, 0, 0)
    current = datetime.datetime.now().time()
    if(time_in_range(start,end,current)):
        openAndAvailable()
        time.sleep(300)
