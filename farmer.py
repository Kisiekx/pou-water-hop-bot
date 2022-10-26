import numpy as np
import cv2
import mss
import pyautogui
import keyboard
import time
import sys


# BEST SCORE: 376
version = 2.0


print("Welcome to PFB", version)

input("Hover onto second hop in front of you and press enter")

xHop, yHop = pyautogui.position()

input("Hower onto coin or clock in front of your pou and press enter")

xCoin, yCoin = pyautogui.position()

input("Hover onto Play Again button and press enter")

xPlayAgain, yPlayAgain = pyautogui.position()

input("Hover onto house and press enter")

xLevelUp, yLevelUp = pyautogui.position()

print("Setting up")

animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
             "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]


for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

# Adjust this settings:
waitingtime = 0.15
xCoin = xCoin-25
yCoin = yCoin-30
widtCoin = 50
heightCoin = 60
xHop = xHop-85
yHop = yHop-60
widthHop = 170
heightHop = 120
xLevelUp = xLevelUp-45
yLevelUp = yLevelUp-45
widthLevelUp = 90
lengthLevelUp = 90
# End of adjustable settings

widthPlayAgain = 2
heightPlayAgain = 2


resolutionCoinAndTmer = {
    'left': xCoin,
    'top': yCoin,
    'width': widtCoin,
    'height': heightCoin
}

resolutionHop = {
    'left': xHop,
    'top': yHop,
    'width': widthHop,
    'height': heightHop
}
resolutionPlayAgain = {
    'left': xPlayAgain,
    'top': yPlayAgain,
    'width': widthPlayAgain,
    'height': heightPlayAgain
}
resolutionLevelUp = {
    'left': xLevelUp,
    'top': yLevelUp,
    'width': widthLevelUp,
    'height': heightPlayAgain
}
print("\nOpen your window with Pou on it")
time.sleep(1)
input("Press enter to start farming")
print('Hold "q" to stop farming')
time.sleep(1)

hop = cv2.imread('../assets/hop.png', cv2.IMREAD_UNCHANGED)
play = cv2.imread('../assets/play.png', cv2.IMREAD_UNCHANGED)
coin = cv2.imread('../assets/coin.png', cv2.IMREAD_UNCHANGED)
timer = cv2.imread('../assets/time.png', cv2.IMREAD_UNCHANGED)
cross = cv2.imread('../assets/level.png', cv2.IMREAD_UNCHANGED)
while True:

    sct = mss.mss()
    scr = np.array(sct.grab(resolutionHop))
    scrCoinAndTime = np.array(sct.grab(resolutionCoinAndTmer))
    scrPlayAgain = np.array(sct.grab(resolutionPlayAgain))
    scrCross = np.array(sct.grab(resolutionLevelUp))

    probHop = cv2.matchTemplate(hop, scr, cv2.TM_CCOEFF_NORMED)
    probCoin = cv2.matchTemplate(coin, scrCoinAndTime, cv2.TM_CCOEFF_NORMED)
    probTimer = cv2.matchTemplate(timer, scrCoinAndTime, cv2.TM_CCOEFF_NORMED)
    probCross = cv2.matchTemplate(cross, scrCross, cv2.TM_CCOEFF_NORMED)

    _, valHop, _, locHop = cv2.minMaxLoc(probHop)
    _, valCoin, _, locCoin = cv2.minMaxLoc(probCoin)
    _, valTimer, _, locTimer = cv2.minMaxLoc(probTimer)
    _, valLevelUp, _, locLevelUp = cv2.minMaxLoc(probCross)

    print(valLevelUp)

    if valLevelUp > 0.9:
        pyautogui.click(x=xLevelUp, y=yLevelUp)
        time.sleep(waitingtime)
        if keyboard.is_pressed('q'):
            break
        continue

    b, g, r, c = scrPlayAgain[1, 1]

    if g == 255:
        pyautogui.click(x=xPlayAgain, y=yPlayAgain)

    # Check coin

    if valCoin > 0.9:
        wc = coin.shape[1]
        hc = coin.shape[0]
        cv2.rectangle(scrCoinAndTime, locCoin,
                      (locCoin[0] + wc, locCoin[1] + hc), (255, 0, 0), 2)
        cv2.putText(scrCoinAndTime, "Coin", locCoin,
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, 2, 0)
        pyautogui.click(x=250, y=375)
        cv2.imshow('PFB', scr)
        cv2.imshow('PFB Coin', scrCoinAndTime)
        cv2.resizeWindow('PFB', 300, 150)
        cv2.resizeWindow('PFB Coin', 250, 175)
        cv2.waitKey(1)
        time.sleep(waitingtime)
        if keyboard.is_pressed('q'):
            break
        continue

    # Check timer

    if valTimer > 0.9:
        wc = timer.shape[1]
        hc = timer.shape[0]
        cv2.rectangle(scrCoinAndTime, locTimer,
                      (locTimer[0] + wc, locTimer[1] + hc), (255, 0, 0), 2)
        cv2.putText(scrCoinAndTime, "Clock", locTimer,
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, 2, 0)
        pyautogui.click(x=250, y=375)
        cv2.imshow('PFB', scr)
        cv2.imshow('PFB Coin', scrCoinAndTime)
        cv2.resizeWindow('PFB', 300, 150)
        cv2.resizeWindow('PFB Coin', 250, 175)
        cv2.waitKey(1)
        time.sleep(waitingtime)
        if keyboard.is_pressed('q'):
            break
        continue

    # Check hop

    if valHop > 0.10:
        w = hop.shape[1]
        h = hop.shape[0]
        cv2.rectangle(
            scr, locHop, (locHop[0] + w, locHop[1] + h), (0, 255, 0), 2)
        cv2.putText(scr, "Hop", locHop, cv2.FONT_HERSHEY_PLAIN,
                    1, (0, 0, 0), 1, 2, 0)
        pyautogui.click(x=650, y=375)
        cv2.imshow('PFB', scr)
        cv2.imshow('PFB Coin', scrCoinAndTime)
        cv2.resizeWindow('PFB', 300, 150)
        cv2.resizeWindow('PFB Coin', 250, 175)
        cv2.waitKey(1)
        time.sleep(waitingtime)
        if keyboard.is_pressed('q'):
            break
        continue

    else:
        pyautogui.click(x=250, y=375)
        pyautogui.click(x=650, y=375)
        cv2.imshow('PFB', scr)
        cv2.imshow('PFB Coin', scrCoinAndTime)
        cv2.resizeWindow('PFB', 300, 150)
        cv2.resizeWindow('PFB Coin', 250, 175)
        cv2.waitKey(1)
        time.sleep(waitingtime)
        if keyboard.is_pressed('q'):
            break
        continue

    cv2.imshow('PFB', scr)
    cv2.imshow('PFB Coin', scrCoinAndTime)
    cv2.resizeWindow('PFB', 300, 150)
    cv2.resizeWindow('PFB Coin', 250, 175)
    cv2.waitKey(1)
    time.sleep(waitingtime)

    if keyboard.is_pressed('q'):

        break
