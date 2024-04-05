# Prompt the user for input
num1 = float(input("Calculate the maximum and minimum of three numbers:\nInput Number -1: "))
num2 = float(input("Input Number -2: "))
num3 = float(input("Input Number -3: "))

# Calculate the maximum and minimum
max_number = max(num1, num2, num3)
min_number = min(num1, num2, num3)

# Display the results
print(f"The maximum number is: {max_number}.")
print(f"The minimum number is: {min_number}.")
