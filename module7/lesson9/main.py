import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfilename 
root = tk.Tk()
root.geometry("600x800")
root.title("Text Editor")
root.rowconfigure(0 , weight=1)
root.columnconfigure(1  , weight=1)
def open_file():
    """OPEN A FILE FOR EDITING"""
    file_path = askopenfilename(filetypes=[("text files" , "*.txt") , ("all files" , "*.*")])
    if not file_path : 
        return 
    textedit.delete(1.0 , tk.END)
    with open(file_path , "r") as input_file  : 
        text = input_file.read()
        textedit.insert(tk.END , text)
        input_file.close()
    root.title(f"Text Editor : {file_path}")
def save_file():
    file_path = asksaveasfilename(filetypes=[("text files" , "*.txt") , ("all files" , "*.*")])
    if not file_path : 
        return 
    with open(file_path , "w") as output_file  : 
        text = textedit.get(1.0 , tk.END)
        output_file.write(text)
    root.title(f"Text Editor : {file_path}")  
textedit = tk.Text(root)
button = tk.Frame(root , relief=tk.RAISED , bd = 2)
btnopen = tk.Button(button , text = "Open" , command=open_file)
btnsave = tk.Button(button , text = "Save as" , command=save_file)
btnopen.grid(row = 0 , column= 0  , sticky = "ew" , padx = 5 , pady = 5)
btnsave.grid(row = 1 , column= 0  , sticky = "ew" , padx = 5 )
button.grid(row=0 , column=0 , sticky="wns")
textedit.grid(row = 0 , column = 1 , sticky = "nsew")
root.mainloop()