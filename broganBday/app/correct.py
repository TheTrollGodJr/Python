import tkinter as tk
app = tk.Tk()
app.title("")

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

def exitApp():
    app.destroy()

# Create a label to display the question
labelA = tk.Label(app, text=f"You will be contacted shortly.", font=("Helvetica", 12), bg="#1E1E1E", fg="white", wraplength=500, justify="center")#, pady=5)
labelA.pack()

labelB = tk.Label(app, text=f"unless im asleep", font=("Helvetica", 7), bg="#1E1E1E", fg="white", wraplength=500, justify="center")
labelB.pack()

# Create a submit button
submit_button = tk.Button(app, text="Submit", command=exitApp, bg="#333", fg="white")
submit_button.pack(pady=5)

app.geometry("300x75")

# Start the tkinter main loop
app.mainloop()