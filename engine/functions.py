import io
import sys
#from movement import *
'''
def startConsole():
    class ReadOnlyConsole(io.TextIOBase):
        def write(self, string):
            print(string, end="")
    startKeyboard()
    # Redirect standard input to the read-only console
    sys.stdin = ReadOnlyConsole()

'''

import threading
import time
import keyboard  # Make sure to install the 'keyboard' package with: pip install keyboard

coords = [0,0,0] # x, y, z
rotation = [360,360] # horizontal, vertical -- facing towards posive x by default -- posive x move right, positive y moves up -- goes to 360 before resetting to 1 -- 360 = 0
distance = [0,0] # rise / run
keys = []

def move(keyInput):
    global coords
    for inputs in keyInput:
        if inputs == "w":
            if rotation[0] == 360 or rotation[0] == 90 or rotation[0] == 180 or rotation[0] == 270:
                if rotation[0] == 360:
                    coords[0] += .5
                elif rotation[0] == 90:
                    coords[2] += .5
                elif rotation[0] == 180:
                    coords[0] -= .5
                elif rotation[0] == 270:
                    coords[2] -= .5
            else:
                if rotation[0] >= 1 and rotation <= 90:
                    if rotation[0] <= 45:
                        # y=(45/m)x
                        # x=(m/90)
                        # m=rotation[0]
                        coords[0] += rotation[0]/90 # add x value
                        coords[2] += .5#(45/rotation[0]) * (rotation[0]/90) # add z value
                    else:
                        #y=-(m/90)+1
                        coords[0] += .5
                        coords[2] += (-1 * (rotation[0]/90)) + 1
                elif rotation[0] >= 91 and rotation[0] <= 180:
                    if rotation[0] <= 135:
                        pass
                    else:
                        coords[0] += (((rotation - 180) * -1)/90)
                        coords[2] += -0.5
                elif rotation[0] >= 181 and rotation[0] <= 270:
                    pass

        elif inputs == "s":
            coords[0] -= 0
            coords[2] -= 0

        if inputs == "right":
            rotation[0] += .2
        elif inputs == "left":
            rotation[0] -= .2

        if inputs == "up":
            rotation[1] += .2
        elif inputs == "down":
            rotation -= .2

        if inputs == "esc":
            sys.exit(1)


class RenderingEngine:
    global keys

    def __init__(self):
        self.is_running = True
        self.lock = threading.Lock()

    def render_loop(self):
        while self.is_running:
            with self.lock:
                # Your rendering logic goes here
                move(keys)
                self.render_frame()
            time.sleep(0.1)  # Adjust the sleep time as needed

    def render_frame(self):
        # Your ASCII rendering logic goes here
        #print("ASCII Art: Frame")
        #print(f"X:{coords[0]}, Y:{coords[1]}, Z:{coords[2]}")
        print(keys)
        pass

    def input_listener(self):
        while self.is_running:
            event = keyboard.read_event(suppress=True)
            #with self.lock():
            if event.event_type == keyboard.KEY_DOWN:
                if event.name not in keys:
                    keys.append(event.name)
            elif event.event_type == keyboard.KEY_UP:
                keys.remove(event.name)
            sys.exit(1)
        #self.is_running = False
        #print("running = false")

    def start(self):
        render_thread = threading.Thread(target=self.render_loop)
        input_thread = threading.Thread(target=self.input_listener)

        render_thread.start()
        input_thread.start()

        render_thread.join()
        input_thread.join()

if __name__ == "__main__":
    engine = RenderingEngine()
    engine.start()
