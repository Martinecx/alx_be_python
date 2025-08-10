first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Division by zero is not allowed"
    case _:
        result = "Invalid operation"

print(f"The result is: {result}")
