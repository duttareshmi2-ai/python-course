# Keywords : Are the special reserved word that python already understands and uses for specefic purpose.
# It can be not be used as a variable.
# Return : A keyword that ends a function's execution immediately and sends a value back whenever that function is called. Any statement or any code written after a return statement written never runs because the function has already finished it's job.
# def main():
#     """hello"""
#     return None
# print(main.__doc__)
# Break: It immeadiately stops a loop entirely and it skips everything that is left to go.
# while True:
#     inp=input("Please type exit if you want to break the loop : ")
#     if inp.lower()=="exit":
#         print("Break")
#         break
#     else:
#         print("Not Breaking")
# pass : It skips or it tells python to do nothing.
# change=0
# if change==0:
#     pass
# else:
#     print(f"Here is the change {change}")
# continue : It tells python to skip the remaining code and jump back to the loop's condition.
# for i in range(10):
#     i+=1
#     if i == 6:
#         continue
#     else:
#         print(i)
#Snack Vending Machine
# Outline:
# You build a snack vending machine that accepts coins one at a time, rejects invalid ones, stops once enough money is inserted, and calculates any change owed using a function
print("Snack Vending Machine"+" (Type 'exit' to stop).")
while True:
    choice=input("What do you want to choose? Lays : Rs10 Pepsi : Rs15 Ice-Cream: Rs20 .   ")
    if choice.lower()=="lays":
        lays=input("Please Enter 10 Rupees : ")
        if not int(lays)==10:
            print("Please pay the required amount from next time.")
        if int(lays)>10:
            change=int(lays)-10
            print(f"Your change is {change} Rupees.")
    if choice.lower()=="pepsi":
        lays=input("Please Enter 15 Rupees : ")
        if not int(lays)==15:
            print("Please pay the required amount from next time.")
        if int(lays)>15:
            change=int(lays)-15
            print(f"Your change is {change} Rupees .")
    if choice.lower()=="ice-cream":
        lays=input("Please Enter 20 Rupees : ")
        if not int(lays)==20:
            print("Please pay the required amount from next time.")
        if int(lays)>20:
            change=int(lays)-20
            print(f"Your change is {change} Rupees .")
    if choice.lower()=="exit":
        print("Exiting. See you again!")
        break