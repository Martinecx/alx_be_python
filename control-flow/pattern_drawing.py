# Ask the user for size
size = int(input("Enter the size of the pattern: "))

# Initialize counters
i = 0

# While loop for rows
while i < size:
    j = 0
    while j < size:
        print("*", end="")
        j += 1
    print()  # Move to the next line
    i += 1
