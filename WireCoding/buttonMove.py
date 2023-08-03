from tkinter import *

root = Tk()
root.attributes('-fullscreen', True)
root.title("Wire Coding")

def move_button():
    # Move the button to the current cursor position
    button.place(x=root.winfo_pointerx() - root.winfo_rootx() - button.winfo_width() // 2,
                 y=root.winfo_pointery() - root.winfo_rooty() - button.winfo_height() // 2)
    # Call the move_button function after 20 milliseconds
    if button_pressed:
        root.after(20, move_button)

def start_moving(event):
    global button_pressed
    button_pressed = True
    move_button()

def stop_moving(event):
    global button_pressed
    button_pressed = False

# Create a button widget
button = Button(root, text="Move Me")
button.place(x=50, y=50)  # Initial position of the button

button_pressed = False

# Bind the button to the left mouse button press event to start moving
button.bind("<ButtonPress-1>", start_moving)

# Bind the button to the left mouse button release event to stop moving
button.bind("<ButtonRelease-1>", stop_moving)

# Run the main event loop
root.mainloop()
'''
def moveButton(e):
    x = e.x
    y = e.y

#root.bind('<Motion>', callable)

button = Button(text= "Move", command= moveButton('<Motion>'))
button.pack()
button.place(bordermode=OUTSIDE, height=150, width=150)
'''
root.mainloop()