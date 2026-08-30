# Art Supplies Billing Tool

# Step 1: Function to calculate item cost
def calculate_item_cost(item_name, price, quantity):
    """
    calculate_item_cost(item_name, price, quantity) -> float
    This function calculates the total cost for a given art supply item.
    """
    return price * quantity

# Step 2: Function to calculate full bill
def calculate_bill(items):
    """
    calculate_bill(items) -> float
    This function calculates the total bill for all art supplies.
    items should be a list of tuples: (item_name, price, quantity)
    """
    total = 0
    for item in items:
        name, price, qty = item
        cost = calculate_item_cost(name, price, qty)
        print(f"{name} (₹{price} x {qty}) = ₹{cost}")
        total += cost
    return total

# Step 3: Example purchase
art_items = [
    ("Paint Brush", 50, 2),
    ("Canvas", 200, 1),
    ("Acrylic Colors", 150, 3),
    ("Palette", 75, 1)
]

# Step 4: Print complete bill
print("🎨 Art Supplies Bill")
print("--------------------")
final_total = calculate_bill(art_items)
print("--------------------")
print("Total Bill = ₹", final_total)
