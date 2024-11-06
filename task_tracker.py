

tasks = []


def add_task(task):
    tasks.append({"task": task, "complete": False})


def complete_tast(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["complete"] = True
            print(f"Task '{task_name} marked as completed.")
            return
    print(f"Task '{task_name}' not found.")


add_task("Do the laundry")
add_task("Read a book")
add_task("Do yoga")
add_task("Go to the gym")
add_task("Study programming")


print(tasks)