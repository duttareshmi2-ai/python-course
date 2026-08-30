# Bill & Seating Helper

# Step 1: Positional arguments to calculate a restaurant bill
def calculate_bill(food_cost, drink_cost, tip):
    total = food_cost + drink_cost + tip
    return total

# Example usage
bill_total = calculate_bill(500, 200, 50)   # positional arguments
print("Restaurant Bill Total:", bill_total)


# Step 2: Recursive function with docstring
def seating_arrangements(n):
    """
    seating_arrangements(n) -> int
    This function calculates the number of seating arrangements
    possible for n people using recursion (factorial).
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * seating_arrangements(n - 1)

# Step 3: Access the docstring
print("\nAccessing docstring of seating_arrangements:")
print(seating_arrangements.__doc__)

# Step 4: Use recursion to calculate seating arrangements
people = 4
arrangements = seating_arrangements(people)
print(f"\nNumber of seating arrangements for {people} people:", arrangements)
