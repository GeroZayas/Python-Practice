# create an empty list to store to-do items
tasks = []

# main loop of the app
while True:
    # print a menu of options
    print("What would you like to do?")
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View all tasks")
    print("4. Quit")

    # get the user's choice
    choice = input("Enter your choice: ")

    # add a new task
    if choice == "1":
        task = input("Enter the new task: ")
        tasks.append(task)
        print("Task added.")

    # mark a task as complete
    elif choice == "2":
        task_index = int(input("Enter the index of the task to mark as complete: "))
        # check if the index is valid
        if task_index >= 0 and task_index < len(tasks):
            tasks[task_index] = "[COMPLETED] " + tasks[task_index]
            print("Task marked as complete.")
        else:
            print("Invalid index.")

    # view all tasks
    elif choice == "3":
        print("Here are all your tasks:")
        for i, task in enumerate(tasks):
            print("----------------------------")
            print(str(i) + ". " + task)
            print("----------------------------")

    # quit the app
    elif choice == "4":
        print("Goodbye!")
        break

    # invalid choice
    else:
        print("Invalid choice.")
