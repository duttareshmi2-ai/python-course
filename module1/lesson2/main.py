import keyword
# Identifers: An identifier is a name used to identify a variable, function, class, modules,etc. It is a combination of alphabets,numbers & underscore.

# Rules:

# 1. It can be a combination of lowercase, uppercase or a digit or an underscore. Example: myName, main_1.

# 2. An Identiier cannot start with a digit. Example: 1class is invalid but class1 is valid.

# 3. Keywords cannot be used as identifiers.

# 4. We cannot use special characters like @,#,$,etc.

# Keywords: A keyword is a word that has some specific meaning reserved by the programming language. Example: int, float, True, False, etc.

# Variables: A variable is user-defined. It is a quantity that may change within the context of the problem or program. Example: a="Hello", a=246.


# Activity 1: Write a program with print commands 

# Normal print statement which print "Hello world".
# print("Hello world")

# This is a print statement which prints a number.
# print(28)

# # This is a print statement which will print multiple arguments.
# print("The product of 23*12:", 23*12)

# Activity 2: Write a program to store different values.
# This prints Hello world.

a="Hello world"
print(a)

# This will print a number.

b=43
print(b)

# Activity 3:  Write a program which will print all the keywords.
print(keyword.kwlist)