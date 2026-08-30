# ids = {
#     "Rohan" : "12" , 
#     "Abhirup" : "10" , 
#     "Rish" : "11"
# }
# Rohan=ids["Rohan"]
# print(Rohan)
# Abhirup = ids["Abhirup"]
# print(Abhirup)
# ids["Rish"] = "14"
# print(ids)
ids = {
    1,2,3,4,5,6,7,8,9,0,1,2,34
}
print(ids)
ids.add("890")
print(ids)
ids1={
    1,2,3,4,5,6,7,8,9,0,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
}
i= ids & ids1
print(i)
import array as arr
a=arr.array("i",[1,2,3,4,12,3,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,2,2,2,2,1,1,1,1])
print(a)
b=[1,2,3,4,5,6,7,8,90,1,2,3,4,6,"string"]
print(b)
a.insert(3,5)
print(a)
length=a.count(4)
print(length)
a.reverse()
print(a)
# Class Fruit Basket Organizer
# Outline:
# A Class Fruit Basket Organizer that stores two fruit baskets as sets, finds the fruits shared between both baskets, and tracks fruit counts using an array that gets updated, counted, and reversed.
from array import array

# Two baskets as sets
basket1 = {"apple", "banana", "orange", "grape"}
basket2 = {"banana", "kiwi", "apple", "melon"}

# Find shared fruits
shared = basket1 & basket2
print("Shared fruits:", shared)

# Fruit counts array (10 slots, all zero)
fruit_counts = array('i', [0] * 10)

# Update counts
fruit_counts[0] += 5   # Add 5 at index 0
fruit_counts[1] += 3   # Add 3 at index 1

# Display counts
print("Fruit counts:", list(fruit_counts))

# Total count
print("Total count:", sum(fruit_counts))

# Reverse counts
fruit_counts = array('i', reversed(fruit_counts))
print("Reversed counts:", list(fruit_counts))
