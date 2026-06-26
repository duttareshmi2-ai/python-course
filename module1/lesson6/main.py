# Operators II:


# If elif else:  The elif allows us to examine us to have multiple statements for True and executes a block code as soon as one of the condition becomes True.
# But elif cannot be written without else statement. 

# Example 1:

# a=3
# if(a>=2): #5>6: False  -1 0 1
#     print("Yo")
# elif(a<=4): #5<5 :False
#     print("Go")
# else:
#     print("YoHo")

# Logical Operators returns Boolean.
# AND : This will return True if both x and y are True.
# OR  : This will return True if either x or y are True.
# NOT : Reverse a result, so if something is True, NOT returns False.

# Example 1:

# a=1
# b=-10

# if (a>0 and b>0): #False
#     print("Greater than 0")
# if (a>0 or b>0): #True
#     print("neither is greater than 0")
# if not (a>b): # False
#     print(True)
# else:
#     print(False)


#Activity 1:
# 1) Store values in `a`, `b`, and `c`.

# 2) Check an AND condition using `a and b and c`:
#    - This becomes True only if all three values are treated as True.
#    - If the condition is True, print the “all true” message.
#    - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.

# 4) Check an OR condition: `a > 0 or b > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.

# Activity 2:
# 1) Store values in `a`, `b`, and `c`.

# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).

# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).

# 4) Store two strings in `a` and `b`.

# 5) If `a` is not equal to `b`, print a message saying they are different.

# 6) Store new numeric values in `a` and `b`.

# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
#    - If exactly one of these comparisons is True, the condition becomes True.
#    - If the condition is True, print "Hello".

# 8) Take an integer input from the user and store it in `a`.

# 9) Check if `a` is not divisible by 2 (remainder is not 0).
#    - If true, print that `a` is not an even number (it is odd).

# Activity 3:
# 1) Ask the user to enter their height in centimeters and store it in `height`.

# 2) Ask the user to enter their weight in kilograms and store it in `weight`.

# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Else if BMI is 24.9 or less → print "healthy"
#    - Else if BMI is 29.9 or less → print "over weight"
#    - Else if BMI is 34.9 or less → print "severely over weight"
#    - Else if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"
# Activity 3:
# height=int(input("Enter your height in centimeters:"))
# weight=int(input("Enter your weight:"))
# height_in_meters=height/100
# BMI=weight/(height_in_meters)**2
# print("Your BMI is ", round(BMI,2) )
# if (BMI < 18.4 or BMI ==18.4):
#     print("Underweight")
# elif (BMI < 24.9 or BMI==24.9):
#     print("Healthy")
# elif (BMI < 29.9 or BMI==29.9):
#     print("Over weight")
# elif (BMI < 34.9 or BMI==34.9):
#     print(" Severely over weight")
# elif (BMI < 39.9 or BMI==39.9):
#     print("Obese")
# else:
#     print("Severely obese")
# Activity 2:
