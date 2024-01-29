class Task:
    def __init__(self, task_id, description, status="Incomplete", due_date=None):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(f"Task {task.task_id}: {task.description} ({task.status})")

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status
                print(f"Task {task_id} updated. New status: {new_status}")
                return
        print(f"Task with ID {task_id} not found.")

# Example usage:

todo_list = ToDoList()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Update Task Status")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        description = input("Enter task description: ")
        task_id = len(todo_list.tasks) + 1
        new_task = Task(task_id, description)
        todo_list.add_task(new_task)
    elif choice == "2":
        todo_list.display_tasks()
    elif choice == "3":
        task_id = int(input("Enter task ID to update: "))
        new_status = input("Enter new status (e.g., Complete/Incomplete): ")
        todo_list.update_task_status(task_id, new_status)
    elif choice == "4":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
