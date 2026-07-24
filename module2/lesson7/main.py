# While loop : It repeats the code as long a condition is True. The condition can be changed to false or make the loop broken using the "break" keyword.

# Syntax : 

# while (condition):

#     statement

# Example : 

# total=10

# num=1

# while (num<=total):
#     if num==8:
#         print("Bye")
#         break
#     else:
#         num+=1
#         print(num)


# Activity  :

# A Chore Checklist Countdown that asks about each chore one at a time, uses a while loop to keep checking until the entire list is empty, and prints a final summary of every chore completed today.

# Instructions : 
# 1. Set total number of chores. 
# 2. Keep a count of the completed chores and the current chore number.
# 3. Repeat while there are still chores to check of.
# 4. Find out the current chores name according to its number.
# 5. Only move to the next chore only when the last one is done.
# 6. Print how many chores remain after each check.
# 7. Print the final checklist only.(Original count, Completed Count and remaining chores)

def process():
    number_of_chores=["washing the dishes for mother","cleaning the table and the plate after eating rice","avoid getting scolding from father"]
    number_of_chores_done=0
    while True:
        ques1=input(f"Write 'completed' if {number_of_chores[0]} is done : ")
        if ques1.lower() == "completed":
            number_of_chores_done+=1
            print(f"Moving on to chore number 2.")
            ques2=input(f"Write 'completed' if {number_of_chores[1]} is done : ")
            if ques2.lower() == "completed":
                number_of_chores_done+=1
                print(f"Moving on to chore number 3.")
                ques3=input(f"3rd and final chore {number_of_chores[2]}. Write 'completed' if done : ")
                if ques3.lower() == "completed":
                    number_of_chores_done+=1
                    print("Very Good!")
                    break
    print(f"{len(number_of_chores)} chores in total and {number_of_chores_done} done.")
process()