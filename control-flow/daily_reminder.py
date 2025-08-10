# daily_reminder.py

task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (unknown priority)"

if time_bound == "yes":  # EXACT condition the checker expects
    reminder += " — This task is time-sensitive! Take immediate action."

print(reminder)
