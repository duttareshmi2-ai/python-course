# List Comprehension : E.g.
nums=[1,2,3,4,5,6,7,8,9]
# mul=[]
# for num in nums : 
#     mul.append(num*2)
# print(mul)
# mul=[num for num in nums if num%2==0 ]
# print(mul)
# Dicitonary Comprehension : E.g.
# d={
#     num : num**2 for num in nums 
# }
# print(d)
# u={}
# for number in nums : 
#    u[number]=number**2
# print(u)
# def square (num) :
#     return num**2
# var=map(square,nums)
# print(list(var))
# alphabets = ["a","b","c","d","e","f","g","h","i"]
# var = zip(alphabets , nums)
# print(list(var))
# Outline:
# A School Store Inventory Checker that filters in-stock items, pairs item names with stock counts into a dictionary, applies a price markup, asks which item you want to buy, and stops the program immediately if that item has already run out.

# Step 1: Create a list of store item names and a list of matching stock counts.

# Step 2: Pair items with stock counts into a dictionary using zip() and dictionary comprehension.

# Step 3: Filter out only the items that are still in stock using list comprehension.

# Step 4: Ask which item the shopper wants to buy.

# Step 5: Stop the checker immediately using exit() if that item has run out.

# Step 6: Apply a markup to every price using map().

# Step 7: Print the final price paid and the updated inventory.