from datetime import datetime

def input_date(prompt):
    date_str = input(prompt)
    if not date_str.strip():
        return None
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return input_date(prompt)
