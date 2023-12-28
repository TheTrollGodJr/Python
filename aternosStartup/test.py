import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Tkinter Window")

# Set the window size
window.geometry("400x200")

# Create a label with some text
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Function to close the application after 5 seconds
def close_application():
    window.destroy()

# Use the after method to wait for 5 seconds and then close the application
window.after(5000, close_application)

# Start the main loop
window.mainloop()
