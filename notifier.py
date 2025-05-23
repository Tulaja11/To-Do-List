from datetime import datetime, timedelta

def get_upcoming_tasks(tasks):
    upcoming = []
    now = datetime.now()
    for t in tasks:
        if t.due_date:
            due = datetime.strptime(t.due_date, "%Y-%m-%d")
            if now <= due <= now + timedelta(days=2) and not t.completed:
                upcoming.append(t)
    return upcoming
