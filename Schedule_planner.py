import tkinter as tk
from tkinter import ttk, messagebox

def open_planner():
    planner = tk.Toplevel(root)
    planner.title("Reading Planner")
    planner.geometry("300x200")

    ttk.Label(planner, text="Total Pages").pack(pady=5)
    total_entry = ttk.Entry(planner)
    total_entry.pack(pady=5)

    ttk.Label(planner, text="Pages per Day").pack(pady=5)
    per_day_entry = ttk.Entry(planner)
    per_day_entry.pack(pady=5)

    def calculate():
        try:
            total = int(total_entry.get())
            per_day = int(per_day_entry.get())
            days = total // per_day
            remaining = total % per_day
            messagebox.showinfo("Result", f"Complete Days: {days}\nRemaining Pages: {remaining}")
        except:
            messagebox.showerror("Error", "Enter valid numbers")

    ttk.Button(planner, text="Calculate", command=calculate).pack(pady=10)

root = tk.Tk()
root.title("Reading Schedule Planner")
root.geometry("250x150")

ttk.Button(root, text="Open Planner", command=open_planner).pack(expand=True)

root.mainloop()
