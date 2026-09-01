# Student Grade Book
# Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

# What you need to use
# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Dictionary created with at least 5 student name-score pairs  →   5 marks
# 2.  A loop correctly calculates and prints the class average      →  10 marks
# 3.  Highest and lowest scores and students identified             →  10 marks
# 4.  .get() used to look up student — friendly message if missing  →  10 marks
# 5.  Program runs without any errors                               →   5 marks
# ========================================================================
# Total  →  40 marks
#  ========================================================================
grade_book = {
    "Alice"  : 90 , 
    "Bob" : 95 , 
    "Rick" : 80
}
print(grade_book)
minimum = max(grade_book)
print(f"{minimum} has the lowest marks . ")
maximum = min(grade_book)
print(f"{maximum} has the highest marks . ")

for key , values in grade_book.items() : 
    average = values  /  3
print(f" The average is {average} . ")
user = input("Please Enter the name of a student to find the marks : ")
result = grade_book.get(user , "Sorry  , Not in the grade book . ")
print(result)