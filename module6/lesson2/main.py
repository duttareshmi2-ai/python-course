# # Method : Think of Method as a task that belongs to a object . Or you can also say that Method is just an action that something can do . For e.g. Dog-bark , etc . 
# class Dog:
#     def bark(self):
#         print("Woof Woof!")
#     def run(self):
#         self.bark()
#         return ("The dog said woof woof!")
# mydog = Dog()
# print(mydog.run())
# # Constructor : When your object is born or created we use constructor . __init__ is a constructor . 
# # Destructor : It destroys or cleans up . 
# class Character:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name} has entered the game . ")
#     def __del__(self):
#         print(f"{self.name} has left the game . ")
# hero = Character("noobmaster456")
# hero1 = Character("Thor-Ironman")
# print("Both the heroes are playing . ")
# del hero1 
# print("This line prints after hero1 is destroyed . ")
# print("But hero is still alive . ")
# books = ["harry potter" , "Percy Jackson"  , "Lord of the Rings"]
# for index,book in enumerate(books):
#     print(f"Book {index} : {book}")
# Activity : String Upper Case
# Outline:
# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
# #
# Activity 1: String Upper Case

# WHAT YOU WILL BUILD

# You create an IOString class that stores a string, takes input from the user, then prints that string converted to

# uppercase.

# HOW IT WORKS

# Step 1: Define a class named IOString.

# Step 2: Inside the class, define _init_(self) as the constructor, setting self.str1 to an empty string.

# Step 3: Define a method get_String(self) that asks the user to enter a string and stores it in self.str1.

# Step 4: Define a method print_String(self) that converts self.str1 to uppercase using .upper() and prints the

# resullt.

# Step 5: Create an object of the IOString class and store it in str1.

# Step 6: Call str1.get_String() to read the user's input.

# Step 7: Call str1.print_String() to print the uppercase string.

# Activity 2: Employee in and Out

# WHAT YOU WILL BUILD

# You create an Employee class with a constructor and a destructor, then trace exactly when each one runs as an

# object is created and removed.

# HOW IT WORKS

# Step 1: Define a class named Employee.

# Step 2: Inside the class, define_init_(self) as the constructor, printing "Employee created" when it runs.

# Step 3: Define_del_(self) as the destructor, printing "Destructor called" when it runs.

# Step 4: Define a function Create_obj() that prints "Making Object ... ", creates an Employee object, prints

# "function end ... ", then returns that object.

# Step 5: Print "Calling Create_obj() function ... " before calling the function.

# Step 6: Call Create_obj() and store the returned object in obj.

# Step 7: Print "Program End ... "- Python automatically calls the destructor once the program finishes and the

# object is no longer needed.

# Activity 3: Pair of Elements

# WHAT YOU WILL BUILD

# You create a pair_elements class with a method that searches a tuple of numbers for two values adding up to a

# target sum, then prints the positions where they were found.

# HOW IT WORKS

# Step 1: Define a class named pair_elements.

# Step 2: Inside the class, define a method twoSum(self, nums, target).

# Step 3: Inside the method, create an empty dictionary lookup to remember numbers you've already seen and

# their positions.

# Step 4: Loop through nums using enumerate(nums), so you get each position i and value num together.

# Step 5: On each pass, check whether target - num is already a key in lookup - if it is, return a tuple of that stored

# position and the current position i.

# Step 6: If not found yet, store the current number and its position in lookup using lookup[num] = i.

# Step 7: Take the target sum as input from the user, call twoSum() on the tuple (10, 20, 30, 40, 50, 60, 70), and

# # print the two positions using an f-string.