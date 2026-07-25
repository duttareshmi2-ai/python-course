def process():
    number_of_chores=["practising maths","practising english comprehensions","doing python"]
    number_of_chores_done=0
    while True:
        ques1=input(f"Write 'completed' if {number_of_chores[0]} is done : ")
        if ques1.lower() == "completed":
            number_of_chores_done+=1
            print(f"Moving on to homework number 2.")
            ques2=input(f"Write 'completed' if {number_of_chores[1]} is done : ")
            if ques2.lower() == "completed":
                number_of_chores_done+=1
                print(f"Moving on to homework number 3.")
                ques3=input(f"3rd and final chore {number_of_chores[2]}. Write 'completed' if done : ")
                if ques3.lower() == "completed":
                    number_of_chores_done+=1
                    print("Very Good!")
                    break
    print(f"{len(number_of_chores)} homework in total and {number_of_chores_done} done.")
process()