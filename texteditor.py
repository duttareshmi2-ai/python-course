import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    text.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as f:
        text.insert(tk.END, f.read())

def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

root = tk.Tk()
root.title("Letter Writing Application")
root.geometry("600x400")

text = tk.Text(root, wrap="word")
text.grid(row=0, column=0, columnspan=3, sticky="nsew")

ttk.Button(root, text="Open Letter", command=open_file).grid(row=1, column=0, sticky="ew")
ttk.Button(root, text="Save Letter", command=save_file).grid(row=1, column=1, sticky="ew")
ttk.Button(root, text="Exit", command=root.destroy).grid(row=1, column=2, sticky="ew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
