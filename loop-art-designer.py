for row in range(1, 11):
	for _ in range(10 - row):
		print(" ", end=" ")
	for _ in range(2 * row - 1):
		print(row, end=" ")
	print()

for row in range(9, 0, -1):
	for _ in range(10 - row):
		print(" ", end=" ")
	for _ in range(2 * row - 1):
		print(row, end=" ")
	print()
