from datetime import datetime

class Task:
    def __init__(self, title, due_date=None, priority="Medium", completed=False):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(**data)
