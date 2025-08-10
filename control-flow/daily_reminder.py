day = input("Enter the day of the week: ").lower()

match day:
    case "monday":
        print("Start your week with a positive mindset!")
    case "tuesday":
        print("Keep going strong!")
    case "wednesday":
        print("Halfway through the week!")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("Finish the week strong!")
    case "saturday":
        print("Enjoy your weekend!")
    case "sunday":
        print("Rest and recharge for the week ahead!")
    case _:
        print("Invalid day entered.")
