import tkinter as tk

def show_greeting():
    greeting_label.config(text="Hello! Welcome to Tkinter!")

root = tk.Tk()
root.title("Greeting Window")
root.geometry("300x200")
root.configure(bg="lightyellow")

title_label = tk.Label(root, text="Simple Greeting App", bg="lightyellow", font=("Arial", 14))
title_label.pack(pady=15)

info_label = tk.Label(root, text="Press the button below", bg="lightyellow")
info_label.pack(pady=10)

button = tk.Button(root, text="Greet Me", command=show_greeting, bg="blue", fg="white")
button.pack(pady=10)

greeting_label = tk.Label(root, text="", bg="lightyellow", font=("Arial", 12))
greeting_label.pack(pady=15)

root.mainloop()
