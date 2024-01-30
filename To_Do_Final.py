import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, task_id, description, status="Incomplete", due_date=None):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date


class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List App")
        self.geometry("400x300")

        self.task_manager = TaskManager()

        self.label = tk.Label(self, text="To-Do List App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.display_tasks_button = tk.Button(self, text="Display Tasks", command=self.display_tasks)
        self.display_tasks_button.pack()

        self.update_task_button = tk.Button(self, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            task_id = len(self.task_manager.tasks) + 1
            new_task = Task(task_id, description)
            self.task_manager.add_task(new_task)
            messagebox.showinfo("Task Added", f"Task '{description}' added successfully!")

    def display_tasks(self):
        self.task_manager.display_tasks()

    def update_task(self):
        task_id = simpledialog.askinteger("Update Task", "Enter task ID to update:")
        if task_id:
            new_status = simpledialog.askstring("Update Task", "Enter new status (e.g., Complete/Incomplete):")
            if new_status:
                self.task_manager.update_task_status(task_id, new_status)
                messagebox.showinfo("Task Updated", f"Task {task_id} updated successfully!")

class TaskManager:
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

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
