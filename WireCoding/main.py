from tkinter import *

import tkinter as tk

def move_line(event):
    # Update the coordinates of the movable end of the line
    canvas.coords(line, image_point_x, image_point_y, event.x, event.y)

# Create the main tkinter window
root = tk.Tk()
root.title("Image with Movable Line")

# Load the image
image = tk.PhotoImage(file="C:/Users/thetr/Downloads/fanum.png")  # Replace with the path to your image

# Create a Canvas widget
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Define the specific point on the image to connect the line
image_point_x, image_point_y = 50, 50

# Draw the line on the canvas with one end connected to the specific point on the image
line = canvas.create_line(image_point_x, image_point_y, 350, 350, fill="blue", width=2)

# Bind the canvas to the left mouse button click event to move the line's movable end
canvas.bind("<B1-Motion>", move_line)

# Run the main event loop
root.mainloop()