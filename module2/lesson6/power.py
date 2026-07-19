n=int(input("Enter the base number : "))


np=int(input("Enter the exponent : "))

result=1


for i in range(np):
    result*=n

print("The answer is ", result )