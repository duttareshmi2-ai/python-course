# What is Nesting? Nesting means placing one if in another if. Example:
choice=int(input("Enter 1 for bike and 2 for car. "))
if choice == 1:
    bike_type=int(input("Enter 1 for scooter and 2 for mountain bike. "))
    if bike_type== 1 :
        print("You picked scooter.")
    else:
        print("You picked moutain bike.")
elif choice == 2:
    car_type=int(input("Enter 1 for Hyundai and 2 for Maruti Suzuki. "))
    if car_type== 1 :
        print("You picked Hyundai.")
    else:
        print("You picked Maruti Suzuki.")
else:
    print("Invalid input.")