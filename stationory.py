import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

stationary_items = {
    "Pen": 1.5,
    "Notebook": 3.0,
    "Pencil": 0.5,
    "Eraser": 0.25,
    "Marker": 2.0
}

currency = "USD"

def toggle_currency():
    global currency
    currency = "INR" if currency == "USD" else "USD"
    update_prices()

def update_prices():
    for i, (item, price) in enumerate(stationary_items.items()):
        display_price = f"{price*80:.2f} INR" if currency == "INR" else f"{price:.2f} USD"
        price_labels[i].config(text=display_price)

def calculate_total():
    total = 0
    for i, (item, price) in enumerate(stationary_items.items()):
        qty = qty_entries[i].get()
        if not qty.isdigit():
            messagebox.showerror("Invalid Input", f"Quantity for {item} must be a number!")
            return
        qty = int(qty)
        item_price = price*80 if currency == "INR" else price
        total += qty * item_price
    messagebox.showinfo("Order Total", f"Total: {total:.2f} {currency}")

root = tk.Tk()
root.title("Stationary Order Management")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

frame = ttk.Frame(canvas, padding=10)
frame_window = canvas.create_window(300, 200, window=frame)

ttk.Label(frame, text="Stationary Order Management", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

price_labels = []
qty_entries = []

for i, (item, price) in enumerate(stationary_items.items(), start=1):
    ttk.Label(frame, text=item).grid(row=i, column=0, padx=10, pady=5)
    price_label = ttk.Label(frame, text=f"{price:.2f} USD")
    price_label.grid(row=i, column=1, padx=10, pady=5)
    price_labels.append(price_label)

    qty_entry = ttk.Entry(frame, width=5)
    qty_entry.grid(row=i, column=2, padx=10, pady=5)
    qty_entries.append(qty_entry)

ttk.Button(frame, text="Toggle Currency (USD/INR)", command=toggle_currency).grid(row=len(stationary_items)+1, column=0, pady=15)
ttk.Button(frame, text="Calculate Total", command=calculate_total).grid(row=len(stationary_items)+1, column=1, pady=15)

root.mainloop()
