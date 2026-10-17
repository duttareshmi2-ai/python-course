import tkinter as tk
from tkinter import ttk, messagebox

def process_task():
    task = entry.get()
    if len(task) == 0:
        messagebox.showwarning("Warning", "You must type a task!")
    else:
        messagebox.showinfo("Last Character", f"Last character: {task[-1]}")

root = tk.Tk()
root.title("After-School Routine")
root.geometry("300x150")

ttk.Label(root, text="Enter a Task:").pack(pady=10)
entry = ttk.Entry(root, width=25)
entry.pack(pady=5)

ttk.Button(root, text="Submit", command=process_task).pack(pady=10)

root.mainloop()
