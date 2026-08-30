# Homework Completion Tracker

# Step 1: List of homework tasks
tasks = ["Math", "Science", "English", "History"]

# Step 2: While loop to check tasks
i = 0
while i < len(tasks):   # repeat until all tasks are complete
    print("Checking homework:", tasks[i])
    i += 1              # update loop variable to stop the loop

print("All homework tasks are complete!")

# -------------------------------
# Infinite Loop Example (for study)
# -------------------------------
# WARNING: This will never stop unless you break it manually
tasks2 = ["Math", "Science"]
j = 0
while j < len(tasks2):
    print("Checking homework:", tasks2[j])
    # forgot j += 1 → loop never ends!
