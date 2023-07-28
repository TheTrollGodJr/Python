import numpy as np
import cv2
import pyautogui

# Specify resolution
resolution = (1920, 1080)
 
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# Specify name of Output file
filename = "Recording.avi"
 
# Specify frames rate. We can choose
# any value and experiment with it
fps = 60.0
 
# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

while True:
 
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
 
    # Convert the screenshot to a numpy array
    frame = np.array(img)
 
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # Write it to the output file
    out.write(frame)
     
    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
     
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()
 
# Destroy all windows
cv2.destroyAllWindows()