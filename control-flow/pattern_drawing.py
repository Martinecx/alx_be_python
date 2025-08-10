# Get size from user
size = int(input("Enter the size of the pattern: "))

# Initialize counter
i = 1

# While loop to draw the pattern
while i <= size:
    print("*" * i)  # Draw pattern line with i stars
    i += 1
