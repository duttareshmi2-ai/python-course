import math
from rich.console import Console
c=Console()
# Printing the square root of input given by user using math module in the simplest way "isqrt".
i=input("Enter a number to find the square root of something: ")
try:
    s=math.isqrt(int(i))
    c.print(f"The square root of {i} is {s}", style="green")
except ValueError:
    c.print("Invalid input", style="red")