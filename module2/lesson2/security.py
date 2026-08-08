
password="rewq@123"


from gtts import gTTS
import playsound
import tkinter as tk
import pywhatkit
import winsound 
import time
root=tk.Tk()
def check_if_password_is_correct(passd,number):
    if not passd or not number:
         label.config(text="PLEASE ENTER BOTH FORMS",fg="red")
    else:
        if str(passd)==password:
          label.config(text="Access granted",fg="green",font=("Times New Roman",72))
          textiftrue="Access Granted"
          g=gTTS(text=textiftrue,lang="en")
          g.save("iftrue.mp3")
          playsound.playsound("iftrue.mp3")
          pywhatkit.sendwhatmsg_instantly(f"{str(number)}","You have inherited 5 million dollars")
        else:
         label.config(text="Alert! Access Denied!",fg="red",font=("Times New Roman",72))
         textiffalse="Access Denied!"
         g=gTTS(text=textiffalse,lang="en")
         g.save("iffalse.mp3")
         playsound.playsound("iffalse.mp3")
         for i in range(10):
              i+=1
              winsound.Beep(1000,1000)
              time.sleep(1)
def GUI():
     epass=entry.get()
     nnum=numen.get()
     check_if_password_is_correct(epass,nnum)
root.geometry("1000x500")
root.config(bg="black")
root.title("Security")
entry=tk.Entry(root,fg="black",bg="white")
entry.insert(0,"Please Enter the password")
entry.pack(pady=10,padx=10)
numen=tk.Entry(root,fg="black",bg="white")
numen.insert(0,"Please Enter the phone number")
numen.pack(pady=10,padx=10)
button=tk.Button(root,text="Press me to execute",fg="black",bg="white",command=GUI)
button.pack(pady=10,padx=10)
label=tk.Label(root)
label.pack()
root.mainloop()