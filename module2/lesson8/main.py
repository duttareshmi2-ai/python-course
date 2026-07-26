# Simple ATM activity with nested loops

print("ATM Session")

for session in range(1, 2):
    name = input("Enter your name: ")
    print("Hello", name)

    amount = int(input("Enter the amount you want to withdraw: "))
    print("You want to withdraw:", amount)

    denominations = [500, 200, 100, 50, 20, 10, 5]
    remaining = amount

    print("Denomination report:")
    for denom in denominations:
        count = remaining // denom
        if count > 0:
            print(f"{denom} x {count}")
            remaining %= denom

    print("Thank you for visiting the ATM.")

