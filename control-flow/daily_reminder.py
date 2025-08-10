import time
from datetime import datetime


def show_reminder(message):
    """Display a reminder message with timestamp."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Reminder: {message}")


def draw_pattern(rows=5):
    """Draws a simple star pattern."""
    for i in range(1, rows + 1):
        print("* " * i)


def daily_routine():
    """Main daily reminder routine."""
    reminders = [
        "Drink water",
        "Take a short walk",
        "Check your posture",
        "Review your to-do list"
    ]

    for reminder in reminders:
        show_reminder(reminder)
        time.sleep(1)  # Short delay for demo; can be changed

    print("\nPattern Drawing:")
    draw_pattern(5)


if __name__ == "__main__":
    try:
        daily_routine()
    except KeyboardInterrupt:
        print("\nReminder program stopped.")
