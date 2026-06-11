from datetime import datetime

class Task:
    def __init__(self, title, priority, category, due_date):
        self.title = title
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "category": self.category,
            "due_date": self.due_date,
            "completed": self.completed
        }


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def edit_task(self, index, title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = title