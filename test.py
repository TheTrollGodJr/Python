import tkinter as tk

def on_enter_key(event):
    return 'break'

root = tk.Tk()
root.title("Single Line Entry")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# Bind the Enter key to the on_enter_key function
entry.bind('<Return>', on_enter_key)
root.geometry("200x100")

root.mainloop()