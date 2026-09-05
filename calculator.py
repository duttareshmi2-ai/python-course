def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b == 0:
		raise ValueError("Cannot divide by zero")
	return a / b


def calculator():
	operations = {
		"+": add,
		"-": subtract,
		"*": multiply,
		"/": divide,
	}

	print("Calculator")
	print("Operations: +, -, *, /")

	try:
		first = float(input("Enter first number: "))
		operator = input("Enter operation: ").strip()
		second = float(input("Enter second number: "))

		if operator not in operations:
			print("Invalid operation")
			return

		result = operations[operator](first, second)
		print("Result:", result)
	except ValueError as error:
		print("Error:", error)


if __name__ == "__main__":
	calculator()
