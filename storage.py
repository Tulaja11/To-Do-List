import json
from task import Task
from config import DATA_FILE

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return [Task.from_dict(t) for t in json.load(f)]
    except FileNotFoundError:
        return []
