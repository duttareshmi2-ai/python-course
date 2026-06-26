import math
# Python Challenges:

# PEDMAS (Operator Precedence): (Parentheses, Expontiation, Division, Multiplication, Add, Substract.) a=(6+2)*2
# Expressions: They are representation of values.

# Example: 
sum=(1+2)**(5-2) #27
sum1=1+2**3 #9 #27

# Activity 1:
# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

# v=25
# w=67
# x=46
# y=23
# z=(v + w) * x / y
# print("Z is ",z)
# name="Abhroneel"
# age=10
# if name =="Alex" or name=="John" and age>=2:
#     print("Welcome to the world although you were here....")
# else:
#     print("Bye!")


# Activity 2: 
# 1) Ask the user to enter the numerator and store it in `numn`.

# 2) Ask the user to enter the denominator and store it in `numd`.

# 3) Check if `numn` is divisible by `numd`:
#    - Find the remainder when `numn` is divided by `numd`.
#    - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.

# numn=int(input("Enter the numerator: "))
# numd=int(input("Enter the denominator: "))
# if numn%numd==0:
#     print("Perfectly divisible")
# else:
#     print("Not divisible perfectly ")



# Activity 3:
# 1) Store the given values:
#    `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.

# 2) Calculate the total sum using the wrong mean:
#    - Multiply `mean1` by `total_number`
#    - Store it in `sum`
#    - Print the sum.

# 3) Fix the sum to get the correct total:
#    - Remove the wrong number (subtract `wrong_number`)
#    - Add the correct number (add `correct_number`)
#    - Store the corrected total in `num2`
#    - Print the corrected sum.

# 4) Find the correct mean:
#    - Divide `num2` by `total_number`
#    - Store it in `mean2`
#    - Print `mean2`.

# Activity 4:
# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.

# 2) Calculate the average of `a`, `b`, and `c`:
#    - Add them and divide by 3
#    - Store the result in `avg`
#    - Print `avg`

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
#    - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
#    - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
#    - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
#    - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
#    - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
#    - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
#    - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".