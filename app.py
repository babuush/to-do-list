import json

# Initialize empty lists to store tasks
tasks = []
completed_tasks = []

# Try to load tasks from a file
try:
    with open("tasks.json", "r") as file:
        tasks_data = json.load(file)
        if isinstance(tasks_data, dict):
            tasks = tasks_data.get("tasks", [])
            completed_tasks = tasks_data.get("completed_tasks", [])
        else:
            print("Invalid data format in the file. Using empty lists.")
except FileNotFoundError:
    tasks = []
    completed_tasks = []

# Main program loop
while True:
    # Display menu
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Remove Uncompleted Task")
    print("5. Remove Completed Task")
    print("6. Quit")

    # Get user input
    choice = input("Enter your choice: ")

    if choice == "1":  # Add a new task
        task_description = input("Enter task description: ")
        task = {"description": task_description, "completed": False}
        tasks.append(task)
        # Save tasks to a file
        with open("tasks.json", "w") as file:
            json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file)

    elif choice == "2":  # View tasks
        # Display the list with identifiers (simple numbering)
        print("Uncompleted Tasks:")
        for i, task in enumerate(tasks, start=1):
            if not task["completed"]:
                print(f"{i}. {task['description']} - Not Completed")
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task['description']} - Completed")

    elif choice == "3":
        # Display tasks to mark as complete
        print("Tasks to Mark as Complete:")
        for i, task in enumerate(tasks, start=1):
            if not task["completed"]:
                print(f"{i}. {task['description']}")
        # Mark a task as complete by selecting its index
        try:
            task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks) and not tasks[task_index]["completed"]:
                completed_task = tasks.pop(task_index)
                completed_task["completed"] = True
                completed_tasks.append(completed_task)
                print("Task marked as complete.")
                # Save tasks to a file after marking as complete
                with open("tasks.json", "w") as file:
                    json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file)
            else:
                print("Invalid task number or task already marked as complete.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "4":
        # Display uncompleted tasks for removal
        print("Uncompleted Tasks to Remove:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['description']} - Not Completed")
        # Remove an uncompleted task by selecting its index
        try:
            task_index = int(input("Enter the number of the uncompleted task to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Removed uncompleted task: {removed_task['description']} - Not Completed")
                # Save tasks to a file after removal
                with open("tasks.json", "w") as file:
                    json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "5":
        # Display completed tasks for removal
        print("Completed Tasks to Remove:")
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task['description']} - Completed")
        # Remove a completed task by selecting its index
        try:
            task_index = int(input("Enter the number of the completed task to remove: ")) - 1
            if 0 <= task_index < len(completed_tasks):
                removed_task = completed_tasks.pop(task_index)
                print(f"Removed completed task: {removed_task['description']} - Completed")
                # Save tasks to a file after removal
                with open("tasks.json", "w") as file:
                    json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "6":
        # Quit the program
        break

    else:
        print("Invalid choice. Please try again.")
