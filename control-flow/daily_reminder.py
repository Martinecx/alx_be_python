# daily_reminder.py

# Example inputs
task = "Finish project report"
priority = "high"  # could be 'low', 'medium', or 'high'
time_bound = True  # True if immediate action required

# Match statement for priority
match priority:
    case "high":
        reminder = f"⚠️ High priority: {task} — needs urgent attention!"
    case "medium":
        reminder = f"📌 Medium priority: {task} — plan to do it soon."
    case "low":
        reminder = f"📝 Low priority: {task} — can be done later."
    case _:
        reminder = f"Task: {task} — priority not set."

# If statement for time sensitivity
if time_bound:
    reminder += " ⏳ This is time-sensitive! Take immediate action."

# Customized output
print(reminder)
