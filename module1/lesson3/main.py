# Data types: Data types are the types that a variable can hold. Types: Integer, float, Boolean, String. We can check the type of a variable by type() method.

# Typecasting: Typecasting is a method to convert a variable data type into a specific data type.

# f=10.18
# i = int(f)
# print(i)


# User Input: Its a input given by a user who is using the program.
# Example:

# print("Enter Your Name: ")
# name = input("enter your name: ")
# print("\nHello", name, "\nwelcome to codingal")

# String Operations: Used to perform various operations on string.
# index of string :It gives you access to a particular character in the string. Index always starts from  0.
# Length of string :The total number of characters present in the string.
# Slicing : Obtaining a substring of string.
# Concatenation : Joining two or more strings in a single one.

# Example for concatenation & join():

# str1="Hello "
# str2="World"

# str3=["Welcome","To the World"]

# print("Concatenation of str1+str2",str1+str2)
# print (" ".join(str3))

# Example of Slicing:

# Str = "string"

# print(Str[3:])

# print(Str[0:1])

# print(Str[-1])

# print(Str[0:3])

# Example for type():

# a=5
# print("This is the type of a", type(a))

# b="Hello"
# print("This is the type of a", type(b))

# a="Hello"

# b=int(a)

# print(type(b))


# Activity 1:
# 1) Store an integer value in `a`.
# 2) Print the datatype of `a` using `type()`.
# 3) Store a decimal (float) value in `b`.
# 4) Print the datatype of `b` using `type()`.
# 5) Store a text (string) value in `c`.
# 6) Print the datatype of `c` using `type()`.
# 7) Store a boolean value (True/False) in `d`.
# 8) Print the datatype of `d` using `type()`.


# Activity 2:
# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
# 2) Print each variable’s value.
# 3) Print the datatype of each variable using `type()`.
# 4) Show a message that type casting will happen next.
# 5) Convert `age` from an integer to a string and store it back in `age`.
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
# 8) Print `weight` and print its datatype again to confirm it changed.

# Activity 3:
# 1) Ask the user to enter a word or sentence and store it in `text`.
# 2) Reverse the string stored in `text` and store the reversed result in `revText`.
#    (Reversing means the last character becomes first, and the first becomes last.)
# 3) Replace `text` with the reversed string (set `text` equal to `revText`).
# 4) Print a message saying you are showing the reversed string.
# 5) Print the reversed string stored in `text`.


# Activity 3:
user_input=input("Enter a word or sentence:")
rev_txt=user_input[::-1]
text=rev_txt

print(text)

# str[3] ?

# str[start:stop:step]