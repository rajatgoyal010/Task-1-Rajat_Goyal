import tkinter as tk
from tkinter import messagebox
from task_manager import Task
from storage import save_tasks, load_tasks


class TodoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List")
        self.root.geometry("700x500")

        self.tasks = load_tasks()

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        self.priority = tk.StringVar(value="Medium")
        tk.OptionMenu(root, self.priority,
                      "High", "Medium", "Low").pack()

        self.category = tk.Entry(root)
        self.category.insert(0, "General")
        self.category.pack()

        self.date = tk.Entry(root)
        self.date.insert(0, "YYYY-MM-DD")
        self.date.pack()

        tk.Button(root, text="Add Task",
                  command=self.add_task).pack()

        self.listbox = tk.Listbox(root,
                                  width=80,
                                  height=15)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Complete",
                  command=self.complete_task).pack()

        tk.Button(root, text="Delete",
                  command=self.delete_task).pack()

        self.refresh()

    def add_task(self):
        title = self.task_entry.get()

        if title == "":
            messagebox.showerror(
                "Error",
                "Task cannot be empty"
            )
            return

        task = Task(
            title,
            self.priority.get(),
            self.category.get(),
            self.date.get()
        )

        self.tasks.append(task)
        save_tasks(self.tasks)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)

        for i, task in enumerate(self.tasks):
            status = "✅" if task.completed else "❌"

            self.listbox.insert(
                tk.END,
                f"{i+1}. {status} {task.title} | "
                f"{task.priority} | "
                f"{task.category} | "
                f"{task.due_date}"
            )

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index].completed = True
            save_tasks(self.tasks)
            self.refresh()
        except:
            pass

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks.pop(index)
            save_tasks(self.tasks)
            self.refresh()
        except:
            pass