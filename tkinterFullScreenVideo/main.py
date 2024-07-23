import tkinter as tk
import cv2
from PIL import Image, ImageTk

def close(event=None):
    # Close the window
    root.destroy()

root = tk.Tk()

# Set the background color to black
root.configure(bg="black")

# Hide the title bar
root.overrideredirect(True)

# Configure to fill the entire screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Load video
video_path = "D:/Downloads/videoplayback (3).webm"  # Replace this with your video file path
video_capture = cv2.VideoCapture(video_path)

# Create a canvas to display video
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
canvas.pack()

def display_video():
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color from BGR to RGB
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img  # Keep a reference to the image to prevent garbage collection
    root.after(10, display_video)  # Repeat after 10 milliseconds

# Start displaying video
display_video()

# Bind the Escape key to close the window
root.bind("<Escape>", close)

root.mainloop()


#D:/Videos/shotcut/alberto.mp4
