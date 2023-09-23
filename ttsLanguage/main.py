import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Fullscreen Window")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to fullscreen
root.geometry("1920x1200")#f"{screen_width}x{screen_height}")

# Create a button widget
button = tk.Button(root, text="Click Me!")

# Place the button in the center of the window
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Function to be called when the button is clicked
def button_click():
    print("Button Clicked!")

# Bind the button click event to the function
button.config(command=button_click)

# Start the tkinter main loop
root.mainloop()