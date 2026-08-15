# Exception : Exception  is a way in Python of saying 'Something unexcepted happened and  I don't know how to continue'.
# try:
#     num=int(input("Enter a number : "))
# except Exception as e :
#     print(f"Error : {e}")
# try:
#     string="hello,exception"
#     idx=int(input("Enter Index : "))
#     print(string[idx])
# except ValueError : 
#     print("Error : please enter a whole number.")
# except IndexError:
#     print("Index does not exist.")
# else:
#     print("Succesful")
# finally:
#     print("This will print always.")
# while True:
#     try:
#         age=int(input("Please Enter Your Age : "))
#         break
#     except ValueError : 
#         print("Please Enter a vaild age.")
# print(age)
#1.Value Error
# Outline:
# Write a program to understand how the value error exception works?
# print("An ERROR Exception occurs when the program encounters a problem which the program dosen't know how to continue after it and therefore throws an Error. An Error can be of many types for e.g. ValueError,TypeError etc.")
# try:
#     n=int(input("Enter a Number or it will give an ValueError : "))
# except ValueError:
#     print("This is an ValueError.")
#2.Multiple exceptions
# Outline:
# Write a program to check how the exceptions and finally statement works
try:

    num1,num2=eval(input("Enter two numbers, separate them by a comma: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("A number cannot be divided by 0.")
except SyntaxError:
    print("Syntax Error")
else:
    print("icing on the cake.")
finally:
    print("This will always return to you")