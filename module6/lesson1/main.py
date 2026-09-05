# Class: Mould/Blueprint for the object.
# Object:Actual object.
# Attribute:Properties of the object.
# __init__: Setup worker who set's the details.
# self: Refers to "This specific car"

# class Dog:
#     def __init__(self,dogname):
#         self.dogname = dogname
#     def bark(self):
#         return f"Dog {self.dogname} is saying woof woof!"
# dog1 = Dog("Richard").bark()
# print(dog1)

# class Car:
#     wheels=4
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand

#     def __getattribute__(self, name):
#         print(f"Someone is trying to access: {name}")
#         return object.__getattribute__(self,name)
# car1=Car("Red","Toyota")
# print(car1.color)

# car1=Car("Gray","VW") # Here "Gray" and "VW" are type of instance Attributes.
# print(car1.color) # Instance Attributes are unique to one object.
# print(car1.wheels) # Here we are accessing the class attribute, which is accessible to all the objects.
# car2=Car("Blue","Hyundai")
# print(car2.color)
# print(car2.wheels)


# class Demo:
#     def __init__(self):
#         self.x=10
#     def __getattr__(self,name):
#         print(f"__getattr__ called for: {name}")
#         return "default value"

# d=Demo()
# print(d.x)
# print(d.y)
# Activity 1 : Student Class
# Outline:
# Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output.
class Student : 
    def __init__(self,grade):
        self.grade=grade
    def student(self):
        return f"This student is of class {self.grade} . "
print(Student(5).student())
print("---------------------------------")
# Activity 2 : Class Vehicle
# Outline:
# Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def check(self):
        return f"The mileage of this car is {self.mileage} . The maximum speed limit is {self.max_speed} . "
print(Vehicle(90,120).check())
print("---------------------------------")
# Activity 3  : Class Parrot
# Outline:
# Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well