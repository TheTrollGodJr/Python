import tkinter as tk
from functions import *

monitors = monitor_areas()
print(monitors)
print(len(monitors))

alpha = 255  # Initial alpha value (255 for white)

def makeApp(xChange,yChange,width,height):
    def fade_to_black():
        global alpha
        if alpha > 0:
            alpha -= 1
            root.configure(bg=f'#{"%02x" % alpha}{"%02x" % alpha}{"%02x" % alpha}')
            root.after(10, fade_to_black)
        else:
            root.destroy()

    root = tk.Tk()
    root.title("Fading White to Black")

    root.configure(bg='white')

    # Start the fading effect after a delay
    root.after(2000, fade_to_black)

    if xChange >= 0 and yChange >= 0:
        root.geometry(f"{width}x{height}+{xChange}+{yChange}")
    elif xChange >= 0 and yChange < 0:
        root.geometry(f"{width}x{abs(height)}+{xChange}{yChange}")
    elif xChange < 0 and yChange >= 0:
        root.geometry(f"{width}x{height}{xChange}+{yChange}")
    else:
        root.geometry(f"{width}x{height}{xChange}{yChange}")

    return root
    

for i in range(len(monitors)):
    makeApp(monitors[i][0],monitors[i][1],monitors[i][2],monitors[i][3])
#makeApp(monitors[2][0],monitors[2][1],monitors[2][2],monitors[2][3])

tk.mainloop()