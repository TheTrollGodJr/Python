import tkinter as tk
from os import startfile

def save_answer():
    answer = answer_text.get("1.0", "end-1c")
    with open(f"C:/Users/thetr/Documents/Python/wakeUp/writing/history.txt", "a", encoding="utf-8") as file:
        file.write(question + "    " + answer + "\n\n")
    with open("C:/Users/thetr/Documents/Python/wakeUp/writing/counter.txt", "w") as file:
        file.write(f"{count + 1}")
    app.quit()

with open("C:/Users/thetr/Documents/Python/wakeUp/writing/counter.txt", "r") as file:
    count = int(file.readline())

with open("C:/Users/thetr/Documents/Python/wakeUp/writing/prompts.txt", "r") as file:
    try:
        question = file.readlines()[count]
    except:
        startfile("C:/Users/thetr/Documents/Python/wakeUp/writing/error.py")
        exit(1)

# Create the main application window
app = tk.Tk()
app.title("Questionnaire")

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

# Create a label to display the question
question_label = tk.Label(app, text=f"{question}", font=("Helvetica", 12), bg="#1E1E1E", fg="white", wraplength=500, justify="center")
question_label.pack()

# Create a taller text box for answering the question with padding
answer_text = tk.Text(app, height=20, width=60, bg="#333", fg="white", padx=10, pady=10)
answer_text.pack()

# Create a submit button
submit_button = tk.Button(app, text="Submit", command=save_answer, bg="#333", fg="white")
submit_button.pack()

# Set the default window size
app.geometry("600x500")

# Start the tkinter main loop
app.mainloop()
