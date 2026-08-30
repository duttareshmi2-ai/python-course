# Step 1: Create dictionary of student records
records = {
    "Rohan": ["Math", "Science", "English", "Math"],   # duplicate "Math"
    "Priya": ["History", "Geography", "Math"],
    "Kiran": ["Biology", "Chemistry", "Biology"],      # duplicate "Biology"
}

print("Initial Records:", records)

# Step 2: Access values safely
print("Rohan's subjects:", records.get("Rohan", "Not Found"))
print("Unknown student:", records.get("Unknown", "Not Found"))

# Step 3: Add and update records
records["Meera"] = ["Art", "Music"]   # add new student
records["Rohan"].append("Computer")   # update existing student
print("After adding/updating:", records)

# Step 4: Remove duplicates manually (no set used)
def remove_duplicates(subjects):
    cleaned = []
    for sub in subjects:
        if sub not in cleaned:
            cleaned.append(sub)
    return cleaned

for student in records:
    records[student] = remove_duplicates(records[student])

# Remove unwanted entry (example: delete "Meera")
del records["Meera"]

print("Cleaned Records:", records)

# Step 5: Check dictionary length
print("Number of students:", len(records))

# Step 6: Iterate through final records
print("\nFinal Student Records:")
for student, subjects in records.items():
    print(f"{student}: {subjects}")
