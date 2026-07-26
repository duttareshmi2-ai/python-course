# Simple ATM activity with nested loops
next=True
print("ATM Session")
total=0
customers=0
while next:
    for session in range(1, 2):
        name = input("Enter your name: ")
        print("Hello", name)

        amount = int(input("Enter the amount you want to withdraw: "))
        print("You want to withdraw:", amount)
        total+=amount
        denominations = [500, 200, 100, 50, 20, 10, 5]
        remaining = amount

        print("Denomination report:")
        for denom in denominations:
            count = remaining // denom
            if count > 0:
                print(f"{denom} x {count}")
                remaining %= denom
        customers+=1
        con=input("Type yes if there is any next person to enter the ATM or no:").strip().lower()
        if con!="yes":
            next=False
print(f"Total Customers Served: {customers}")
print(f"Total Money Dispensed: {total}")
print("Bye! Hope to see you again.")