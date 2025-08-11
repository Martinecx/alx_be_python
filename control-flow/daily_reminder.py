#!/usr/bin/env python3

def main():
    # Prompt for inputs
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process based on priority
    match priority:
        case "high":
            print(f"Reminder: '{task}' is a high priority task", end="")
        case "medium":
            print(f"Reminder: '{task}' is a medium priority task", end="")
        case "low":
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task", end="")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
                print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
                return
        case _:
            print(f"Reminder: '{task}' has an unspecified priority", end="")

    # Explicit time-bound check as required
    if time_bound == 'yes':
        print(" that requires immediate attention today!")
    else:
        print()  # move to a new line if no extra message

    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")


if __name__ == "__main__":
    main()
