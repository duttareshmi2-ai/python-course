# Operators III:

# Identity Operators: Identity Operators helps us identify if two variables are pointing to the exact same object in the computer's memory. 
# Two identity operators: 
# 1. Is  : Returns True if both variables point to the same object in memory.
# 2. Is not :  Returns True if both variables point to the different object.

# Example :

# a=[1,2,3]
# b=[1,2,3]

# c=a

# print(a is c) # True - same object
# print(a is b) # False - different objects
# print(a is not c) # False 
# print(a is not b) #True 


# Membership Operators: These operators help us find out if something exists inside a collection or not. They search through list, strings, tuples and other sequences to tell if a value is there or not.
# Two operators :
# 1. In : Returns True if a value is found in the sequence.
# 2. not in : Returns True if a value is not found in the sequence.

# Example:

# a=[1,2,3]
# b=[1,2,3]
# # c=a
# c=[1,2,3,[1,2,3]]
# print (a in c) #True
# print (a not in b) #True
# # print (a in c)
# # print (a not in b)

# Example 2:
# sentence="Hello World"

# print("Hello" in sentence) # True
# print("Pyhton" in sentence) # False
# print("Xyz" not in sentence) #True

# Bitwise Operators: They work directly with the 0's and 1's that computer uses to store numbers.


# Activity 1: Write a program to illustrate the use of 'is' identity operator
# Activity 2: Write a program to apply the right shift and left shift bitwise operator.
# Activity 3: Write a program to show students’ grades by entering marks for five subjects, calculating the average, and checking the grade range using membership operators in and not in. For example, use in to check whether the average is in the range 91 to 100, 81 to 90, and so on, and use not in to validate marks outside the allowed range.
# Activity 1:
print("The 'is' operator in python is used to show that something is equivalent to something just like in real life. ")
print("For e.g.:")
word="hello world"
word2=word
if word is word2:
    print(word2," | this is printed by the is variable telling the computer that if in the variable 'word' 'hello world' is there then print it")
# Activity 2:
num=12 # binary:1100
print("\nOriginal number ", num)
print("\nBinary ",bin(num))
left_shift=num<<2
print("\nLeft shift ", left_shift)
print("\nBinary ",bin(left_shift))
right_shift=num>>2
print("\nRight_shift",right_shift)
print("Binary ",bin(right_shift))
# Activity 3:
english=input("Enter your marks for english: ")
bengali=input("Enter your marks for bengali: ")
maths=input("Enter your marks for maths:")
social_studies=input("Enter your marks for Social studies: ")
science=input("Enter your marks for science: ")
average=english+bengali+maths+social_studies+science/5
print("Your average is ", average)
if 91<= average <=100:
    print("Excellent marks.")
if 81<= average <=90:
    print("Good marks.")
else:
    print("Could have done better.")