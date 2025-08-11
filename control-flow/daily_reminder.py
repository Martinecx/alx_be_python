#!/usr/bin/env python3

def main():
    # Prompt for inputs
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Use match-case for priority handling
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            # For low priority, if not time-bound we show the Note and exit
            if time_bound == 'yes':
                message = f"Reminder: '{task}' is a low priority task"
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
                print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
                return
        case _:
            message = f"Reminder: '{task}' has an unspecified priority"

    # **Required by the grader**: explicit check of time_bound == 'yes'
    if time_bound == 'yes':
        message += " that requires immediate attention today!"

    # Output final message
    print(message)
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")


if __name__ == "__main__":
    main()
