import cv2
import time
from screeninfo import get_monitors
import threading
import pyautogui
import random
from playsound import playsound
import pygetwindow as gw


def moveWindow(windowCoords=list, monitorDimensions=tuple):
    playsound("Trolls/movingPopup/errorSound.mp3")
    while runThread:
        mouse = pyautogui.position()

        # if the mouse is in the window
        if mouse[0] >= windowCoords[0] and mouse[0] <= windowCoords[0]+411 and mouse[1] >= windowCoords[1] and mouse[1] <= windowCoords[1]+160:
            #print(random.randint(1,99))
            num = random.randint(1,4)

            # move window up
            if num == 1:
                newY = mouse[1]-200
                if newY <= 0:
                    newY = monitorDimensions[1]-180
                windowCoords[1] = newY
                cv2.moveWindow("Fatal Error!", windowCoords[0], newY)
            elif num == 2:
                newY = mouse[1]+100
                if newY >= monitorDimensions[1]-75:
                    newY = 20
                windowCoords[1] = newY
                cv2.moveWindow("Fatal Error!", windowCoords[0], newY)
            elif num == 3:
                newX = mouse[0]+200
                if newX >= monitorDimensions[0]:
                    newX = 20
                windowCoords[0] = newX
                cv2.moveWindow("Fatal Error!", newX, windowCoords[1])
            elif num == 4:
                newX = mouse[0]-600
                if newX <= 0:
                    newX = monitorDimensions[0]-430
                windowCoords[0] = newX
                cv2.moveWindow("Fatal Error!", newX, windowCoords[1])

        time.sleep(.01)

if __name__ == "__main__":
    monitorDimensions = (get_monitors()[0].width, get_monitors()[0].height)
    img = cv2.imread("Trolls/movingPopup/error.jpg")

    cv2.imshow("Fatal Error!", img)
    cv2.moveWindow("Fatal Error!", int(monitorDimensions[0]/2)-200, int(monitorDimensions[1]/2)-130)

    runThread = True
    t1 = threading.Thread(target=moveWindow, args=([int(monitorDimensions[0]/2)-200, int(monitorDimensions[1]/2)-130], monitorDimensions,))
    t1.start()

    while True:
        key = cv2.waitKey(1) & 0xFF
        if cv2.getWindowProperty("Fatal Error!", cv2.WND_PROP_VISIBLE) == 0:
            runThread = False
            time.sleep(.1)
            break
        
        if key == 27:
            runThread = False
            time.sleep(.1)
            break

    t1.join()
    
    cv2.destroyAllWindows()


    


