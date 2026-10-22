import tkinter as tk

root = tk.Tk()
root.title("ATM PIN Setup Interface")

frame = tk.Frame(root, bd=5, relief="sunken")
frame.pack(padx=10, pady=10)

pin_var = tk.StringVar()

entry = tk.Entry(frame, textvariable=pin_var, show="*", width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=3, pady=10)

def add_digit(d):
    pin_var.set(pin_var.get() + str(d))

def clear_pin():
    pin_var.set("")

def submit_pin():
    tk.Label(root, text=f"PIN set to: {pin_var.get()}", font=("Arial", 14)).pack()

# Keypad buttons
for i in range(1, 10):
    tk.Button(frame, text=str(i), width=5, height=2, command=lambda d=i: add_digit(d)).grid(row=(i-1)//3+1, column=(i-1)%3, padx=5, pady=5)

tk.Button(frame, text="Clear", width=5, height=2, command=clear_pin).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame, text="0", width=5, height=2, command=lambda: add_digit(0)).grid(row=4, column=1, padx=5, pady=5)
tk.Button(frame, text="Submit", width=5, height=2, command=submit_pin).grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
