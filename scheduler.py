from datetime import datetime

def sort_by_due_date(tasks):
    return sorted(tasks, key=lambda t: t.due_date or "")

def sort_by_priority(tasks):
    priority_map = {"High": 1, "Medium": 2, "Low": 3}
    return sorted(tasks, key=lambda t: priority_map.get(t.priority, 2))
