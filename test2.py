#1 Project × 40 Marks

# Function Calculator
# Build a calculator that uses a separate function for each operation. The user picks an operation and enters two numbers. Your program handles invalid input and division by zero without crashing.

# What you need to use
# ------------------------------------------------------------------------
# 1.  def and return     →  define 4 functions: add, subtract, multiply, divide
# 2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
# 3.  float(input())     →  to read numbers from the user
# 4.  return values      →  each function must return the correct result
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  4 functions defined — add, subtract, multiply, divide        →  10 marks
# 2.  Each function returns the correct result for any two numbers →  10 marks
# 3.  ZeroDivisionError caught and prints a clear message          →  10 marks
# 4.  ValueError caught for non-number input                       →   5 marks
# 5.  Program runs without any errors                              →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

print("---Calculator---")
def add(a,b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Please Enter a number."
def subtract(c,d):
    try:
        return float(c) - float(d)
    except ValueError:
        return "Please Enter a number."
def multiply(e,f):
    try:
        return float(e) * float(f)
    except ValueError:
        return "Please Enter a number."
def divide(g,h):
    try:
        return float(g) / float(h)
    except ValueError:
        return "Please Enter a number."
    except ZeroDivisionError:
        return "Cannot Divide By Zero"
def main():
    choice=input("Please Enter your choice : add or subtract or multiply or divide : ")
    if choice.lower()=="add":
        a=input("Enter the first number : ")
        b=input("Enter the second number : ")
        print("The answer is ", add(a,b))
    elif choice.lower()=="subtract":
        a=input("Enter the first number : ")
        b=input("Enter the second number : ")
        print("The answer is ", subtract(a,b))
    elif choice.lower()=="multiply":
        a=input("Enter the first number : ")
        b=input("Enter the second number : ")
        print("The answer is ", multiply(a,b))
    elif choice.lower()=="divide":
        a=input("Enter the first nuumber : ")
        b=input("Enter the second number : ")
        print("The answer is ", divide(a,b))
    else:
        print("Please enter from the given choices.")
main()