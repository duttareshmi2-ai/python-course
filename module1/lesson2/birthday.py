# Making a project where different birthday dates are stored in variables (5).
Mine="10th October"

My_mother="10th October"

My_father="25th May"

My_bestfriend="23rd April"

My_sister="2nd April"

# Printing the dates in five different print statements.

print("My birthday is", Mine)

print("My mother's birthday is", My_mother)

print("My father's birthday is", My_father)

print("My bestfriend's birthday is", My_bestfriend)

print("My sister's birthday is ", My_sister)



# Congragulation project
from rich.console import Console
c=Console()
# Creating a program where the user gives input on something he/she has won.
# The output will first show the type of the input.
# Remember: There will be a variable called congragulation which will be set to None variable type unless the user gives input.
congragulation=None
# Input:
i=input("Tell me something on which you have won for e.g. chess or cricket etc in one word or type No: ")
# First printing the type of input:
print("You wrote ",i," and the type is ",type(i))
# If there is No or no in input then say a bye message.
if i.lower()=="no":
    print("Thanks,Bye!")
# Now the main logic:
else:
    congragulation = i
    c.print(f"Congratulations on winning {i} ", style="green")