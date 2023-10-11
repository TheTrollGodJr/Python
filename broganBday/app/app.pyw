import tkinter as tk
from conv import *
import os
from os import startfile

dir = os.path.dirname(os.path.abspath(__file__))

def on_enter_key(event):
    return 'break'

app = tk.Tk()
app.title("Answer Submission")

# Configure dark mode colors
app.configure(bg="#1E1E1E")
app.option_add("*TButton*highlightBackground", "#1E1E1E")
app.option_add("*TButton*highlightColor", "#1E1E1E")
app.option_add("*TButton*background", "#333")
app.option_add("*TButton*foreground", "white")
app.option_add("*TButton.padding", [10, 5])
app.option_add("*TLabel*background", "#1E1E1E")
app.option_add("*TLabel*foreground", "white")
app.option_add("*TText*background", "#333")
app.option_add("*TText.foreground", "white")

def revert():
    question_label.config(text="Enter the final message")

def checkAnswer():
    answer = answer_text.get()#"1.0", "end-1c")
    answer_text.config(textvariable="")
    print(answer)
    if (tokenA == change(answer)) or (tokenB == change(answer)):
        startfile(os.path.join(dir, "alert.pyw"))
        question_label.config(text="Correct")
        app.after(3000, revert)
    else:
        print("wrong")
        question_label.config(text="Incorrect")
        app.after(3000, revert)

# Create a label to display the question
question_label = tk.Label(app, text=f"Enter the final message", font=("Helvetica", 12), bg="#1E1E1E", fg="white", wraplength=500, justify="center", pady=5)
question_label.pack()

# Create a taller text box for answering the question with padding
answer_text = tk.Entry(app, width=60, bg="#333", fg="white")
answer_text.pack(pady=10)

# Create a submit button
submit_button = tk.Button(app, text="Submit", command=checkAnswer, bg="#333", fg="white")
submit_button.pack()

answer_text.bind('<Return>', on_enter_key)
# Set the default window size
app.geometry("500x125")

# Start the tkinter main loop
app.mainloop()