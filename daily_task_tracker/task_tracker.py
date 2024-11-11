

tasks = []


def add_task(task):
    tasks.append({"task": task, "completed": False})


def complete_tast(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["complete"] = True
            print(f"Task '{task_name} marked as completed.")
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
    for index, task in enumerate(tasks):
        if task['task'] == task_name:
            del tasks[index]
            print(f"Task '{task_name}' has been deleted.")
            break
        else:
            print(" hello")
            print(f"Task '{task_name}' not found.")


def mark_as_complete(task_name):
    #This task allows you to mark a task as complete if it exists in the task list
    for task in tasks:
        if task['task'] == task_name:
            task['task'] = "complete"
            print(f"Task '{task_name}' has been marked as complete.")
            break
    else:
        print(f"Task '{task_name}' not found in the task list")




add_task("Do the laundry")
add_task("Read a book")
add_task("Do yoga")
add_task("Go to the gym")
add_task("Study programming")

view_tasks()
incomplete_tasks()

delete_task("Go to the gym")
mark_as_complete("Study programming")

#TODO: create a interactive menu 