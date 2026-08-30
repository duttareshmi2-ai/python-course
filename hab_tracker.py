# Weekly Habit Tracker

# Step 1: Create tuples to store habit information
habits = ("Exercise", "Read", "Meditate", "Sleep Early")
completion = (True, False, True, True)   # weekly completion record

print("Habits:", habits)
print("Completion Records:", completion)

# Step 2: Find tuple length
print("Number of habits:", len(habits))
print("Number of completion records:", len(completion))

# Step 3: Access values using indexing
print("First habit:", habits[0])
print("Last habit:", habits[-1])

# Step 4: Access values using slicing
print("First two habits:", habits[0:2])
print("Middle habits:", habits[1:3])

# Step 5: Iterate through habits
print("\nIterating through habits:")
for h in habits:
    print("Habit:", h)

# Step 6: Summary of completion
completed_count = completion.count(True)
not_completed_count = completion.count(False)

print("\nSummary:")
print("Completed habits:", completed_count)
print("Not completed habits:", not_completed_count)

# Step 7: Explore immutability
try:
    habits[0] = "Workout"   # attempt to change tuple directly
except TypeError as e:
    print("\nTuples cannot be changed directly!")
    print("Error message:", e)
