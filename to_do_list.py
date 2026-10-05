tasks = []
while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")
    elif choice == "2":
        for task in tasks:
            print(task)
    elif choice == "3":
        task_to_remove = input("Enter the task to remove: ")
        tasks.remove(task_to_remove)
        print("Task removed!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
