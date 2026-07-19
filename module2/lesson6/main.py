import time


# Loops: A loop statement allows us to run a statement or group of statements multiple times.
# Types of loops: 
# 1. For loop: The for loop is used to repeat over a sequence. 
# Syntax :
# for i in sequence(range,list,string):
#       statements.

# Example:

# n="hellow"
# temp=""
# for i in n:
#     temp+=i
# print(temp) #hellow

# for num in range(10): #range(start,end,step)
#     print(num)


# 2. While loop: Execute a statement or a group of statements while a given condition is True.
# 3. Nested Loop: We can operate multiple loops inside another while or for loop.


# Activity 1: 
# 1) Ask the user to enter a number and store it in `n`.

# 2) Set `sum` to 0.
#    (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.

# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)

n=int(input("Enter any number: "))

sum=0


for i in range(1,n,1):

    sum+=i

    print(f"\r{sum}", end="", flush=True)

    time.sleep(0.5)


# Activity 2:
# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.
#    (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:
#    - Add the character `i` in front of `string2`
#    - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).

string=input("Enter a word or sentence: ")

string2=""

for i in string:
    string2=i+string2

print(string)

print(string2)


# Activity 3:
# # 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.

# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).



n=int(input("Enter a number greater than 1 : "))


print("All the numbers from  ", n , "to 1")


for i in range(n,0,-1):
    print(i)