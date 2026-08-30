# Grocery Billing Queue

# Step 1: List of grocery items
queue = ["Milk", "Bread", "Eggs", "Rice", "Juice"]

# Step 2: While loop to process items
i = 0
while i < len(queue):   # repeat until all items are processed
    print("Billing item:", queue[i])
    i += 1              # update loop variable to stop the loop

print("All items billed!")

# -------------------------------
# Infinite Loop Example (for study)
# -------------------------------
# WARNING: This will never stop unless you break it manually
queue2 = ["Milk", "Bread", "Eggs"]
j = 0
while j < len(queue2):
    print("Billing item:", queue2[j])
    # forgot j += 1 → loop never ends!
