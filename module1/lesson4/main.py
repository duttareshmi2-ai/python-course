import math
# Operators-1:
# Operators: They are symbols used to perform mathematical, logical or assignment operations on operands.
# Operands are values or functions on which operators act or perform operations. Example: 3+4, here 3 & 4 are operands and "+" is a operator.

# Three types of operators:
# 1. Arithmetic Operators: They perform mathematical calculations such as addition, subtraction, multiplication, division, etc. "+": Add, "-": Subtract, "*": Multiplication, "/": Division, "%": Modulus, "**": Exponentiation, "//": Floor Division.
# 2. Comparison Operators: They compare two operands and return either True or False. "==": Equal, "!=": not equal, ">": Greater than, "<": Less than, ">=": Greater than equal to, "<=": Less than equal to.
# 3. Assignment Operators: They assign values to variables or update the current value of variables, often combining arithmetic or bitwise operations. "=": simple assignment, "+=": add & assign, "-=": subtract and assign, "/=": divide and assign,"*=": multiple and assign, "%=": modulus and assign,"//=" floor division and assign, "**=": exponetiate and assign.
# 4. Logical Operators: They are used for logical operations such as and, or & not.


# Example for Arithmetic:
calc=2.67+3.8989
print(round(calc,4))
print(2-3)
print(3*2)
print(math.ceil(5/2)) #2.5 
print(10%5)
print(2**3)
print(5//2)

# Example for comparison:

print(3<5)
print(3>5)
print(3==5)
print(3!=5)
print(3>=5)

# Example for assignment:

a=3
a+=1
print(a)


# Activity 1:
# # 1) Store the values for each tree in separate variables: tree1, tree2, tree3, tree4, tree5

# 2) Add all 5 tree values and store the result in `sum`

# 3) Print the total (`sum`) of all 5 trees

# 4) Divide `sum` by 5 to find the average and store it in `average`

# 5) Print the average (`average`) of all 5 trees


# Activity 2:
# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.

# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.

# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.