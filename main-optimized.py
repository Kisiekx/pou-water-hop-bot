import numpy as np
import cv2
from time import sleep
import mss
import pyautogui
import keyboard

#settings for croping screenshoot
resolution = {
    'left': 520,
    'top': 400,
    'width': 250,
    'height': 200
}

hop = cv2.imread('../assets/hop.png', cv2.IMREAD_UNCHANGED)
grayhop = cv2.cvtColor(hop, cv2.COLOR_BGR2GRAY)

#loop
while True:


    #picture of thing that I am looking for


    #screenshooting place where the thing should be
    sct = mss.mss()
    scr = np.array(sct.grab(resolution))
    grayscr = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)

    #looking for the thing
    probality = cv2.matchTemplate(grayhop, grayscr, cv2.TM_CCOEFF_NORMED)

    #clicking left part of the screen if there is the thing and left where there isn't
    _, max_val, _, _ = cv2.minMaxLoc(probality)

    if max_val>0.20:

        pyautogui.click(x=700, y=400)

    else:
        pyautogui.click(x=200, y=400)
        pyautogui.click(x=700, y=400)

    #break
    if keyboard.is_pressed('q'):
        break

    sleep(0.15)

    cv2.imshow('view', scr)
