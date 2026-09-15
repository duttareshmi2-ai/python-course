# # Inheritance : Inheritance means one class can borrow features , properties or actions from another class . 
# class Animal : 
#     def eat(self):
#         print("I am eating.")
# class Deer(Animal):
#     pass
# object1 = Deer()
# object1.eat()
# class Animal :
#     def whoami(self):
#         print(f"I am {self.__class__.__name__}")
# class Lion(Animal): 
#     def roar(self):
#         print ("Roar!!")
# obj = Lion()
# obj.whoami()
# obj.roar()
class Animal :
    def __init__(self , name): 
        self.name = name
class Tiger(Animal):
    def __init__(self , name , color)  : 
        super().__init__(name)
        self.color = color
obj = Tiger("Simba" , "yellow")
print(obj.name , obj.color)
# Overriding a method  :  
# Checking with is subclass
