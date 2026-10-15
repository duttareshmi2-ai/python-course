import tkinter as tk
from tkinter import messagebox
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Main")
# def top_win():
#     top = tk.Toplevel()
#     top.geometry("180x100")
#     top.title("Toplevel")
#     label = tk.Label(top , text = "This is a top level window . ")
#     label.pack(padx = 10 , pady=10)
#     top.mainloop()
# label_root = tk.Label(root , text = "This is the root window . ")
# button = tk.Button(root , text = "Click here to open another window . " , command=top_win)
# label_root.pack(pady = 10 , padx= 20)
# button.pack(pady = 10 , padx = 10)
# root.mainloop()
root = tk.Tk()
root.geometry("650x400")
root.title("Denomination Counter")
root.configure(bg = "light blue")
label = tk.Label(root , text = "Hey User ! Welcome to the Denomination Counter Application . " , bg = "yellow" , fg = "black")
label.place(relx = 0.5 , y = 340 , anchor=tk.CENTER)
def openmessage_box():
    msgbox = messagebox.showinfo("Alert" , "Do you want to calculate the denomination count?")
    if msgbox == "ok" : 
        top_win()
btn = tk.Button(root , text = "Let's Get started" , command = openmessage_box , bg = "red" , fg = "orange")
btn.place(x = 260 , y = 360)
def top_win():
    top = tk.Toplevel()
    top.geometry("600x350+50+50")
    top.title("Denomination")
    top.configure(bg = "light grey")
    label = tk.Label(top , text = "Enter total amount" , bg = "white" , fg = "black")
    entry = tk.Entry(top)
    labelw = tk.Label(top , text = "Here are number of notes for each denomination " , bg = "cyan" , fg = "orange")
    l1 = tk.Label(top , text = "2000" , bg = "light grey")
    l2 = tk.Label(top , text = "500" , bg = "light grey")
    l3 = tk.Label(top , text = "100" , bg = "light grey")
    e1 = tk.Entry(top)
    e2 = tk.Entry(top)
    e3 = tk.Entry(top)
    def cal():
        try : 
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            e1.delete(0 , tk.END)
            e2.delete(0 , tk.END)
            e3.delete(0 , tk.END)
            e1.insert(tk.END , str(note2000))
            e2.insert(tk.END , str(note500))
            e3.insert(tk.END , str(note100))
        except ValueError : 
            messagebox.showerror("Error" , "Please Enter a valid number")
    btnsubmit = tk.Button(top , text = "Calculate" , command = cal , bg = "yellow" , fg = "red")
    label.place(x = 230 , y = 50)
    entry.place(x = 200 , y = 80)
    btnsubmit.place(x = 240 , y = 120)
    labelw.place(x = 140 , y = 170)
    l1.place(x = 180 , y = 200)
    l2.place(x = 180 , y = 230)
    l3.place(x = 180 , y = 260)
    e1.place(x = 270 , y = 200)
    e2.place(x = 270 , y = 230)
    e3.place(x = 270 , y = 260)
    top.mainloop()
root.mainloop()