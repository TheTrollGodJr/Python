import keyboard
#from functions import *

def keyboardPressed(e):
    print(e.name)
    #print(f'Key {e.name} {"pressed" if e.event_type == keyboard.KEY_DOWN else "released"}')
    #if e.name == "w":
        #if e.event_type == keyboard.KEY_DOWN:
        #    print("Forward")
        #else:
        #    print("Stop")

def startKeyboard():
    keyboard.hook(keyboardPressed)
    keyboard.wait("esc")
    exit(1)

if __name__ == "__main__":
    startKeyboard()