# Prompt the user for input
num1 = float(input("Please input number - 1: "))
num2 = float(input("Please input number - 2: "))

# Prompt the user to choose a method
print("Please choose method below:")
print("1 – Summary")
print("2 – Multiply")
print("3 – Minus")

# Get the user's choice
choice = int(input("Your choice: "))

# Perform the calculation based on the user's choice
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 * num2
elif choice == 3:
    result = num1 - num2
else:
    result = "Invalid choice"

# Display the result
print(f"The result is: {result}")
