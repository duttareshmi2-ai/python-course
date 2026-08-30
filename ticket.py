# Parking Ticket Helper

# Step 1: Function to calculate change
def give_change(total, paid):
    change = paid - total
    if change > 0:
        return change
    else:
        pass   # no change needed
    return 0

# Step 2: Coin payment program
valid_coins = [1, 2, 5, 10]   # accepted coin values
ticket_price = 12
paid = 0

print("Parking Ticket Price:", ticket_price)
print("Insert coins (accepted: 1, 2, 5, 10). Type 0 to stop.")

while True:
    coin = int(input("Enter coin: "))
    
    if coin == 0:   # stop coin collection
        print("Coin collection stopped.")
        break
    
    if coin not in valid_coins:   # skip invalid coins
        print("Invalid coin, try again.")
        continue
    
    paid += coin
    print("Total paid so far:", paid)
    
    if paid >= ticket_price:
        print("Ticket paid successfully!")
        change = give_change(ticket_price, paid)
        if change > 0:
            print("Return change:", change)
        else:
            pass   # no change needed
        break
