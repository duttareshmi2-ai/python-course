import tkinter as tk
#Event - Event is any action that happens when the program is runnning like pressing a key , clicking a mouse button or moving a mouse . Tkinter's mailoop function keeps the window open and continously watches for these events so that the program can react . 
#Bind - Bind is a method that connects a specific kind of event like key press to a function , which is known as event handler . 
root = tk.Tk()
# root.title("Event handler")
# root.geometry("100x100")
# def handle_key_press(event):
#     """Print the character associated to the key press . """
#     print(event.char)
# root.bind("<Key>" , handle_key_press)
# def handle_click(event):
#     print("\nThe button was clicked")
# button = tk.Button(text = "Click Me!"  )
# button.pack()
# button.bind("<Button-1>" , handle_click)
# root.mainloop()
from tkinter import messagebox
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert!" , "Virus is Found!!")
button = tk.Button(root , text="Check for Virus" , command=msg)
button.pack(padx = 40 , pady=40)
root.mainloop()