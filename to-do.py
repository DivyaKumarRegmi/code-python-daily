#tasks['learn python','GO to market']    status=[False,False]
tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Complete")
    print("4. View Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ").strip()
        if task:
            tasks.append([task, False])
        else:
            print("Task cannot be empty.")

    elif choice == 2:
        taskN = int(input("Enter task number to delete: "))
        if 0 < taskN <= len(tasks):
            tasks.pop(taskN - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    elif choice == 3:
        taskN = int(input("Enter task number to mark as complete: "))
        if 0 < taskN <= len(tasks):
            if tasks[taskN - 1][1] == True:
                print("Task is already marked.")
            else:
                tasks[taskN - 1][1] = True
                print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == 4:
        if not tasks:
            print("No tasks available.")
        for i, task in enumerate(tasks):
            status = '\u2713' if task[1] else '\u2717'
            print(f"{i + 1}. {task[0]} {status}")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

    input("Enter any key to continue...")