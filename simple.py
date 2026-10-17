import tkinter as tk

def show_greeting():
    name = entry.get()
    if name.strip() == "":
        greeting_label.config(text="Please type your name!")
    else:
        greeting_label.config(text=f"Hello {name}, welcome!")

root = tk.Tk()
root.title("Greeting Window")
root.geometry("300x200")
root.configure(bg="lightgreen")

title_label = tk.Label(root, text="Simple Greeting App", bg="lightgreen", font=("Arial", 14))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your name:", bg="lightgreen")
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Greet Me", command=show_greeting, bg="blue", fg="white")
button.pack(pady=10)

greeting_label = tk.Label(root, text="", bg="lightgreen", font=("Arial", 12))
greeting_label.pack(pady=10)

root.mainloop()
