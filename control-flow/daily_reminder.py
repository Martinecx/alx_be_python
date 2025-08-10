# daily_reminder.py

# Exact required input prompts
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Match Case statement for priority
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (unknown priority)"

# If statement to modify reminder if task is time-bound
if time_bound.lower() == "yes":
    reminder += " — This task is time-sensitive! Take immediate action."

# Provide customized reminder
print(reminder)
