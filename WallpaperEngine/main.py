import ctypes
import time

count = 0

while True:
  if count == 980:
    count = 0
  else:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:/Users/thetr/Documents/Python/WallpaperEngine/frames/frame{count}.jpg", 0)
    count += 1
    time.sleep(.06)