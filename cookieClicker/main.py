import pyautogui
import keyboard
import cv2
import numpy as np
import asyncio
import sys

'''
spawn golden cookie:
var newShimmer=new Game.shimmer("golden");
'''

def keyToggle():
    global toggle
    if toggle: toggle = False
    else: toggle = True
    
def exitToggle():
    global endToggle
    if endToggle: endToggle = False
    else: endToggle = True

def getPixels(image):
    grayscale_image = image.convert("L")
    pixels = grayscale_image.load()

    width, height = grayscale_image.size
    pixels = []

    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 255:
                pixels.append((x, y))

    if len(pixels) != 0:
        x, y = 0, 0
        for item in pixels:
            x += item[0]
            y += item[1]
        return (int(x/len(pixels)), int(y/len(pixels)))
    else:
        return (0,)

async def checkGolden():
    while True:
        img = pyautogui.screenshot()
        t = 5
        mask = cv2.inRange(img, np.array([96-t, 169-t, 196-t]), np.array([96+t, 169+t, 196+t]))
        coords = getPixels(mask)
        
        if len(coords) > 1:
            mouseX, mouseY = pyautogui.position()
            pyautogui.moveTo(coords[0], coords[1])
            pyautogui.click()
            pyautogui.moveTo(mouseX, mouseY)
        asyncio.sleep(10)

async def main():
    toggle = False
    endToggle = False
    keyboard.add_hotkey("shift + q", keyToggle)
    keyboard.add_hotkey("shift + p", exitToggle)
    print("Running")
    while True:
        if toggle:
            pyautogui.click()
        if endToggle:
            break
        asyncio.sleep(.01)
    sys.exit(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    shutdown = asyncio.Event()

    loop.create_task(checkGolden)
    loop.create_task(main)