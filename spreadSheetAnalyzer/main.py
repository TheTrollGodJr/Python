import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import pyperclip  # This module is used to copy text to the clipboard

def submit_function():
    # Replace this function with your own logic
    print("Submit button pressed!")
    print("Selected File:", selected_file.get())
    print("Text entered:")
    print(text_entry.get("1.0", tk.END))  # Get the text from the text box
    enable_copy_button()

def select_file():
    file_path = filedialog.askopenfilename()
    selected_file.set(file_path)
    enable_copy_button()

def enable_copy_button():
    copy_button.config(state=tk.NORMAL)  # Enable the "Copy" button

def disable_copy_button():
    copy_button.config(state=tk.DISABLED)  # Disable the "Copy" button

def copy_to_clipboard():
    # Replace this string with the text you want to copy
    text_to_copy = "Example text to be copied to the clipboard"
    pyperclip.copy(text_to_copy)
    tkinter.messagebox.showinfo("Copied!", "Text has been copied to the clipboard.")
    disable_copy_button()

# Create the main window
root = tk.Tk()
root.title("Modern Dark Theme Example")
root.geometry("600x250")
root.configure(bg='#2C3E50')  # Dark background color

# Variable to store selected file path
selected_file = tk.StringVar()

# Label above the text box
text_label = tk.Label(root, text="Enter Prompt:", fg="white", bg='#2C3E50', font=('Helvetica', 12))
text_label.pack(pady=(10, 0))

# Smaller text box for entering text
text_entry = tk.Text(root, bg='#34495E', fg="white", height=5, width=30, wrap=tk.WORD)
text_entry.pack(expand=True, fill='both', padx=80, pady=(15, 15))

# Frame to hold buttons
button_frame = tk.Frame(root, bg='#2C3E50')
button_frame.pack()

# Button to select a file
select_button = tk.Button(button_frame, text="Select File", command=select_file, bg='#34495E', fg="white")
select_button.pack(side=tk.LEFT, padx=5, pady=(0,10))

# Submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_function, bg='#3498DB', fg="white")
submit_button.pack(side=tk.LEFT, padx=5, pady=(0,10))

# Copy button (initially grayed out)
copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard, bg='#95A5A6', fg="white", state=tk.DISABLED)
copy_button.pack(side=tk.LEFT, padx=5, pady=(0,10))

# Run the Tkinter event loop
root.mainloop()
