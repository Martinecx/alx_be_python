# Get user inputs
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Modify reminder message if time-bound
if time_bound.lower() == "yes":
    urgency_note = "This task requires immediate attention!"
else:
    urgency_note = "This task can be done at your convenience."

# Match case for priority level
match priority.lower():
    case "high":
        priority_note = "High priority - handle this as soon as possible."
    case "medium":
        priority_note = "Medium priority - try to get it done soon."
    case "low":
        priority_note = "Low priority - complete it when you have time."
    case _:
        priority_note = "Priority not recognized."

# Final customized reminder
print(f"Reminder: {task}")
print(priority_note)
print(urgency_note)
