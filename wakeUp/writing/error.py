import tkinter as tk

def close_app():
    app.destroy()  # Close the tkinter window

# Create the main application window
app = tk.Tk()
app.title("Error")

# Create a label to display a line of text
text_label = tk.Label(app, text="There are no more questions.\nPlease add more.", font=("Helvetica", 12))
text_label.pack()

# Create an "OK" button
ok_button = tk.Button(app, text="OK", command=close_app)
ok_button.pack()

app.geometry("300x75")
# Start the tkinter main loop
app.mainloop()