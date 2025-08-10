# daily_reminder.py

# Get task priority from user
priority = input("Enter task priority (high, medium, low): ").lower()

# Get time sensitivity from user
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Match case statement to provide customized reminder based on priority
match priority:
    case "high":
        reminder = "⚡ High priority task! Complete it as soon as possible."
    case "medium":
        reminder = "⏳ Medium priority task. Plan to finish it soon."
    case "low":
        reminder = "📝 Low priority task. Do it when you have free time."
    case _:
        reminder = "❓ Unknown priority. Please set a valid one."

# If statement to modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " ⏰ Immediate action required due to time sensitivity!"

# Provide a customized reminder
print(f"Reminder: {reminder}")
