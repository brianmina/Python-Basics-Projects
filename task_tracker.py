

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


add_task("Do the laundry")
add_task("Read a book")
add_task("Do yoga")
add_task("Go to the gym")
add_task("Study programming")

view_tasks()
incomplete_tasks()