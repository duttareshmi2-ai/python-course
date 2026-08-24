import python_weather
import tkinter as tk
import time
import asyncio
import geocoder
from tkintermapview import TkinterMapView
class Information_Dashboard:
    def __init__(self,root):
        self.root=root
        self.time=time.strftime("%I : %M : %S %p")
        self.root.config(bg="black")
        self.root.geometry("800x400")
        self.widget=TkinterMapView(self.root,width=300,height=200,corner_radius=40)
        self.widget.pack(fill="both",expand=True)
        self.label=tk.Label(self.widget)
        self.label.place(relx=0.5,rely=0.05,anchor="n")
        self.weather()
        self.Map()
    def weather(self):
        async def catch():
            async with python_weather.client.Client() as client:
                master = await client.get("Kolkata")
                return master.country  ,  master.temperature , master.kind
        country,temperature,kind=asyncio.run(catch())
        now=time.strftime("%I : %M : %S %p")
        self.label.config(text=f"Country : {country}  | Temperature : {temperature} | Kind : {kind} | Time : {now}",fg="red",font=("DS-Digital",23,"bold"),bg="black")
        self.root.after(100,self.weather)
    def Map(self):
        ip=geocoder.ip("me")
        lat,lng=ip.latlng
        self.widget.set_position(lat,lng)
        self.widget.set_zoom(12)
        self.widget.set_marker(lat,lng,text="Position")
root=tk.Tk()
Information_Dashboard(root)
root.mainloop()