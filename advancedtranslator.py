from PIL import Image,ImageTk
import tkinter as tk

root=tk.Tk()
root.geometry("1920x1080")
bg_image=Image.open("bg.png")
bg_photo=ImageTk.PhotoImage(bg_image)
image=tk.Label(root,image=bg_photo)
image.place(x=0,y=0,relwidth=1,relheight=1)
root.mainloop()