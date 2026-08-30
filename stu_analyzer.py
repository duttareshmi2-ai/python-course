# Student Marks List Analyzer

# Step 1: Create a list of marks
marks = [85, 90, 78, 92, 88, 76, 95]

print("Marks List:", marks)

# Step 2: Find length of the list
print("Number of marks:", len(marks))

# Step 3: Access items with indexing
print("First mark:", marks[0])
print("Third mark:", marks[2])
print("Last mark:", marks[-1])

# Step 4: Access items with slicing
print("First three marks:", marks[0:3])
print("Marks from index 2 to 5:", marks[2:6])

# Step 5: Iterate through marks
print("\nIterating through marks:")
for m in marks:
    print("Mark:", m)

# Step 6: Calculate summary
total = sum(marks)
average = total / len(marks)
smallest = min(marks)
largest = max(marks)

print("\nSummary of Marks:")
print("Total:", total)
print("Average:", average)
print("Smallest:", smallest)
print("Largest:", largest)
