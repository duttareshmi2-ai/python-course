tasks_left = 3

while tasks_left > 0:
    print(f"Homework tasks remaining: {tasks_left}")
    input("Complete a homework task, then press Enter: ")

    tasks_left -= 1  # Update loop variable

print("All homework tasks are complete!")