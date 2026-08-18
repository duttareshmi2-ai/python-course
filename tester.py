import tkinter as tk
import pygame as pg
import playsound
from PIL import Image,ImageTk,ImageDraw
pg.mixer.init()
root=tk.Tk()
tick=pg.mixer.Sound("tick.wav")
def count_down(total):
    if total >=0:
        h,rem=divmod(total,3600)
        m,s=divmod(rem,60)
        label.config(text=f"{h:02d}:{m:02d}:{s:02d}",fg="red",font=("DS-Digital",32,"bold"),bg="black")
        tick.play()
        root.after(1000,count_down,total-1)
    else:
        label.config(text="Timer Ended",fg="green",font=("Minecraft",32,"bold"),bg="black")
        playsound.playsound("tester.mp3")
def start_timer():
    h=0
    m=0
    s=10
    total=h*3600+m*60+s
    count_down(total)
root.geometry("1536x730")
root.config(bg="black")
img=Image.new("RGB",(1500,150),"black")
draw=ImageDraw.Draw(img)
draw.rounded_rectangle((20,20,1480,140),radius=40,fill="orange",outline="yellow",width=4)
bg=ImageTk.PhotoImage(img)
bg_master=tk.Label(root,image=bg,bg="black")
bg_master.place(relx=0.5,rely=0.5,anchor="center")
label=tk.Label(bg_master)
label.place(relx=0.5,rely=0.5,anchor="center")
start_timer()
root.mainloop()