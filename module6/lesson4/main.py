# # Private Attribute : It is something hidden only which it's own class can access it and would prevent be touched from the outside . A private attribute is a variable or method with a double _ . 
# # Encapsulation : Encapsulation means that protecting the data and only allow safe and control changes . 
# # Setter : It is a method which is built specifically for this job (ONE INTENTIONAL METHOD FOR UPDATING A PRIVATE VARIABLE'S VALUE) . 
# # Special funtions are methods which or whose name starts and ends with a double _ . For e.g __init__ , __str__, __add__ ,etc  . 
# class Robot : 
#     def __init__(self , name) : 
#         self.name = name
#         self.__battery = 100
#     # def setbattery(self , value):
#     #     if 0 <= value <= 100 : 
#     #         self.__battery=value
#     #         print(f"Battery level updated . ")
#     #     else : 
#     #         print("Battery level must be between 0 and 100 to power up . ")
#     # def showbattery(self):
#     #     print(f"Battery level : {self.__battery}")
#     def __str__(self):
#         return f"Hi. I am {self.name} . "
# r = Robot("siri")
# # r.setbattery(150)
# # r.setbattery(12)
# # r.showbattery()
# print(r)
# Activity 1 : Outline:
# Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
# Activity 2 : Outline:
# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
# Activity 3 : Outline:
# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.
# # 
# Activity 1: Keep It Private!

# WHAT YOU WILL BUILD

# You create a class with a private variable and a private method, then see exactly what happens when you try to

# reach each one from inside versus outside the class.

# HOW IT WORKS

# Step 1: Define a class named myClass.

# Step 2: Inside the class, create a private class variable _privateVar set to 27.

# Step 3: Define a private method _privMeth(self) that prints a short message.

# Step 4: Define a public method hello(self) that prints _privateVar's value using myClass ._ privateVar.

# Step 5: Create an object foo of the myClass class.

# Step 6: Call foo.hello() - since hello() is a method inside the class, it reaches the private variable with no trouble.

# Step 7: Try reaching foo ._ privMeth from outside the class - Python raises an AttributeError, proving a private

# method really can't be reached this way from outside.

# Activity 2: Computer Price

# WHAT YOU WILL BUILD

# You create a Computer class with a private selling price, then compare what happens when you try to change it

# directly versus using a proper setter method.

# HOW IT WORKS

# Step 1: Define a class named Computer.

# Step 2: Inside_init_(self), set a private instance variable self ._ maxprice to 900.

# Step 3: Define a method sell(self) that prints the current selling price using an f-string.

# Step 4: Define a setter method setMaxPrice(self, price) that updates self ._ maxprice to the new price.

# Step 5: Create an object c and call c.sell() - it prints 900.

# Step 6: Try setting c ._ maxprice = 1000 directly, then call c.sell() again - it still prints 900, since this only created

# a new, separate attribute instead of touching the real private value.

# Step 7: Call c.setMaxPrice(1000), then call c.sell() one more time - it now prints 1000, since the setter actually

# reached the real private variable.


# Activity 3: Point Function

# WHAT YOU WILL BUILD

# You create a Point class that stores an x and y coordinate, then define a special function so printing a Point

# object automatically shows its coordinates.

# HOW IT WORKS

# Step 1: Define a class named Point

# Step 2: Define_init_(self, x, y) and store both values onto self.x and self.y.

# Step 3: Define the special function_str_(self), returning an f-string formatted as "(x, y)".

# Step 4: Create an object p1 by calling Point(2, 3).

# Step 5: Call print(p1) - Python automatically calls _str_ behind the scenes and prints its returned text,

# showing (2, 3).