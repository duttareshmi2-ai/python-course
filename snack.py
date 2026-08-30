from array import array

# --- Step 1: Custom "set" using list ---
def make_set(items):
    custom_set = []
    for snack in items:
        if snack not in custom_set:   # avoid duplicates
            custom_set.append(snack)
    return custom_set

# --- Step 2: Add new snack ---
def add_snack(custom_set, snack):
    if snack not in custom_set:
        custom_set.append(snack)

# --- Step 3: Find shared snacks ---
def shared_snacks(set1, set2):
    shared = []
    for snack in set1:
        if snack in set2 and snack not in shared:
            shared.append(snack)
    return shared

# Snack boxes
box1 = make_set(["chips", "cookies", "juice", "apple"])
box2 = make_set(["juice", "sandwich", "chips", "banana"])

print("Box 1:", box1)
print("Box 2:", box2)

# Add new snack
add_snack(box1, "muffin")
print("Box 1 after adding muffin:", box1)

# Find shared snacks
common = shared_snacks(box1, box2)
print("Shared snacks:", common)

# --- Step 4: Array of snack counts ---
snack_counts = array('i', [2, 5, 3, 1])  # counts for some snacks

# --- Step 5: Add values to array ---
snack_counts[0] += 2   # add 2 chips
snack_counts[1] += 1   # add 1 cookie

print("Snack counts:", list(snack_counts))

# --- Step 6: Use count() and reverse() ---
print("How many times '3' appears:", snack_counts.count(3))

snack_counts.reverse()
print("Reversed snack counts:", list(snack_counts))
