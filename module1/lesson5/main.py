# from rich.console import Console
# c=Console()
# Conditional Statements:

# Indentation: It tells python that a group of statements belong to a particular block of code. It helps in managing and maintaining the code.

# If Statement/Condition: It only executes the code when the condition is True.
# If Else Statement/Condition: It gets executed only when the if condition is False.

# Example for If Statements:

# num=3
# if num>0:
#     print(num,"Its positive number")

# num=-1
# if num>0:
#   print(num,"Its a positive number ")


# # Example for If Else Statement:

# i=4

# if (i<15):
#    print("i is smaller than 15")
# else:
#    print("i is greater than 15")


# Activity 1:
# write a program to check whether the given number is positive?

#Activity 2:
#Write to check if a person is buying oranges at 100 rs and later selling it at 120 rs. Find that he has profit or loss?

#Activity 3:
# Write a program to check whether the given number is greater than 15 or smaller than 15.

#Activity 4:
# Write a program to check whether the given number is even or odd?

# Activity 1:
# Checking if the user input's number is positive or not.
# u=input("Enter a number which is positive or not: ")
# try:
#     if int(u)>0:
#       c.print(f"{u} is a positive number!", style="green")
#     else:
#       c.print(f"{u} is not a positive number!", style="red")
# except ValueError:
#    c.print("Invalid input", style="red")

# Activity 2:
# bought=100
# sold=120
# if sold-bought >0:
#    print("Profit")
# else:
#    print("Loss")
# Activity 3:
# u=input("Enter a number to compare your number with 15: ")
# if int(u)>15:
#     print("Your number is greater than 15.")
# else:
#     print("Your number is smaller than 15.")
# Activity 4:
# u=input("Enter a number to check whether it is even or odd:")
# if int(u)%2==0:
#     print("Even")
# else:
#     print("Odd")