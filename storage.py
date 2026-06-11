import json
from task_manager import Task

FILE = "tasks.json"


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)


def load_tasks():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        tasks = []
        for item in data:
            task = Task(
                item["title"],
                item["priority"],
                item["category"],
                item["due_date"]
            )
            task.completed = item["completed"]
            tasks.append(task)

        return tasks

    except:
        return []