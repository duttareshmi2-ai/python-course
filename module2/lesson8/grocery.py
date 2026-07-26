print("Welcome to the grocery store!")
print("\nYou can buy the following items at different costs:\n")
print("\n1.Basamati Rice (10kg) | Rs 300\n")
print("\n2.Dhupkati/candles (10 per packet) | Rs 40\n")
print("\n3.Roti/Maida (5kg) | Rs 200")
print("\n4.'Solution to acidity'- ENO (1 packet lime flavour ) | Rs 5\n")
customer_num=0
price=0
while  customer_num<=6:
    customer_num+=1
    customer=int(input("Please enter your choice: "))
    if customer==1:
        print("Rs 300 please.")
        price+=300
    elif customer==2:
        print("Rs 40 please.")
        price+=40
    elif customer==3:
        print("Rs 200 please.")
        price+=200
    elif customer==4:
        print("Rs 5 please.")
        price+=5
    else:
        print("Sorry, not in the list")
    print("Total money earnerd : " + price)