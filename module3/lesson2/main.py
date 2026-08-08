# Built in functions: print,int, and etc.
# Not Built in functions can be created using define (def) variable.
# def add(a,b):
#     return a+b
# output=add(2,3)
# print(output)
#A Lemonade Stand Calculator that greets every customer, calculates the total cost and change due using functions with arguments and return statements, and prints a personalized thank you message alongside the final receipt.
def greet(name):
    return f"Welcome to the Lemonade Store {name}"
def calculate(lemonade_size,cost):
    lemonade_size+=1
    cost+=cost
def change(cost):
    