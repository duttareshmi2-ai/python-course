def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+': print(add(x, y))
elif op == '-': print(sub(x, y))
elif op == '*': print(mul(x, y))
elif op == '/': print(div(x, y))
else: print("Invalid operation")
