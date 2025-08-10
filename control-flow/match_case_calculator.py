first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        result = first_number / second_number
    case _:
        result = "Invalid operation"

print(f"The result is: {result}")
