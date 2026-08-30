prices = {
	"apple": 1.50,
	"bread": 2.00,
	"milk": 3.00,
	"rice": 5.00,
}

while True:
	bill = []
	total = 0

	print("\nEnter grocery items. Type 'exit' to print the bill.")

	while True:
		item = input("Item: ").lower()

		if item == "exit":
			break

		if item not in prices:
			print("Item not available.")
			continue

		quantity = int(input("Quantity: "))
		cost = prices[item] * quantity
		bill.append((item, quantity, cost))
		total += cost

	print("\n----- GROCERY BILL -----")
	for item, quantity, cost in bill:
		print(f"{item.title()} x {quantity} = ${cost}")
	print(f"Total: ${total}")
	print("------------------------")

	again = input("Start a new bill? (yes/no): ").lower()
	if again != "yes":
		break
