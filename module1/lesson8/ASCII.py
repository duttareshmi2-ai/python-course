take=input("Enter anything: ")
if take.islower:
    print("Input is in lowercase fully.")
elif take.isupper:
    print("Input is in uppercase fully.")
else:
    print("Input is mixed up of uppercase and lowercase.")
if len(take)==1:
    out=ord(take)
    print("Unicode", out)
else:
    print("Enter only one special caracter.")