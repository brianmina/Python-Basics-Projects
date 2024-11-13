

tasks = []


def add_task(task):
    tasks.append({"task": task, "completed": False})


def complete_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["completed"] = True
            print(f"Task '{task_name} marked as completed.")
            print(f"Updated task: {task}") # debugging
            return
    print(f"Task '{task_name}' not found.")

#TODO: create 2 functions(view_tasks() and incomplete_tasks())

def view_tasks():
    print("\nYour task:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Imcomplete"
        print(f"- {task['task']}: {status}")
    print()


def incomplete_tasks():
    print("\nIncomplete tasks:")
    for task in tasks:
        if not task["completed"]:
            print(f"-{task['task']}")
    print()


def delete_task(task_name):
    # This function will allow the user to remove a specific task by name.
    # Set a flag to check if the task was found
    task_found = False
    for index, task in enumerate(tasks):
        if task['task'] == task_name:
            del tasks[index]
            print(f"Task '{task_name}' has been deleted.")
            task_found = True
            break
        
    if not task_found:
        print(f"Task '{task_name}' not found.")


# def mark_as_complete(task_name):
#     #This task allows you to mark a task as complete if it exists in the task list
#     for task in tasks:
#         if task['task'] == task_name:
#             task['Completed'] = True
#             print(f"Task '{task_name}' has been marked as complete.")
#             break
#     else:
#         print(f"Task '{task_name}' not found in the task list")

def menu():
    print("Welcome to the Task Tracker!")
    while True:
        print("\nPlease choose an option:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Mark a task as complete")
        print("4. View all task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == "2":
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to mark as complete: ")
            complete_task(task_name)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting the Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

menu()

#TODO: create a interactive menu 