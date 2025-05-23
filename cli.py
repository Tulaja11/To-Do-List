from task import Task
from storage import save_tasks, load_tasks
from scheduler import sort_by_due_date
from utils import input_date

def run_cli():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            due = input_date("Due Date (YYYY-MM-DD) [optional]: ")
            prio = input("Priority (Low/Medium/High): ")
            task = Task(title, due, prio)
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            for i, t in enumerate(sort_by_due_date(tasks), 1):
                status = "✔" if t.completed else "✗"
                print(f"{i}. [{status}] {t.title} - Due: {t.due_date}, Priority: {t.priority}")
        elif choice == "3":
            idx = int(input("Task number to mark complete: ")) - 1
            tasks[idx].completed = True
            save_tasks(tasks)
        elif choice == "4":
            idx = int(input("Task number to delete: ")) - 1
            tasks.pop(idx)
            save_tasks(tasks)
        elif choice == "5":
            break
