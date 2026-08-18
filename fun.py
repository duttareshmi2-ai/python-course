import tkinter as tk
import sounddevice as sd
import queue, threading, json
import vosk
import pyttsx3

# ------------------- Setup -------------------
root = tk.Tk()
root.geometry("800x400")
root.config(bg="black")

# Counter state
total = 0
running = True

# Speech engine (local TTS, no MP3 files)
engine = pyttsx3.init()

# Vosk model (download + unzip first!)
model = vosk.Model(r"C:\Users\dutta\OneDrive\Desktop\python course\vosk-model-small-en-us-0.15")
rec = vosk.KaldiRecognizer(model, 16000)

# Queue for audio streaming
q = queue.Queue()

# ------------------- Audio -------------------
def audio_callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_for_blast():
    global running
    while running:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").lower()
            print("Heard:", text)  # Debug
            if "blast" in text:
                running = False
                for widget in root.winfo_children():
                    widget.destroy()
                global blast_label
                blast_label = tk.Label(root, text="", fg="red",
                                       font=("Minecraft", 64, "bold"), bg="black")
                blast_label.place(relx=0.5, rely=0.5, anchor="center")
                typing_animation("Blast!")
                break

# ------------------- Counter -------------------
def count_adder():
    global total, running
    if not running:
        return
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    label.config(text=f"{h:02d}:{m:02d}:{s:02d}",
                 fg="red", font=("DS-Digital", 32, "bold"), bg="black")
    # Speak seconds directly
    engine.say(str(s))
    engine.runAndWait()
    total += 1
    root.after(1000, count_adder)

# ------------------- Animation -------------------
def typing_animation(text, index=0):
    if index < len(text):
        blast_label.config(text=text[:index+1])
        root.after(200, typing_animation, text, index+1)

# ------------------- UI -------------------
label = tk.Label(root, text="00:00:00", fg="red",
                 font=("DS-Digital", 32, "bold"), bg="black")
label.place(relx=0.5, rely=0.5, anchor="center")

blast_label = tk.Label(root, text="", fg="red",
                       font=("Minecraft", 32, "bold"), bg="black")
blast_label.place(relx=0.5, rely=0.2, anchor="center")

# ------------------- Start -------------------
sd.InputStream(samplerate=16000, channels=1, callback=audio_callback).start()
threading.Thread(target=listen_for_blast, daemon=True).start()
count_adder()

root.mainloop()
