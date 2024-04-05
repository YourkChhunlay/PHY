# Function to calculate factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Prompt the user for input
n = int(input("Enter a number: "))

# Calculate and display the result
factorial_result = calculate_factorial(n)
print(f"Factorial of {n} is: {factorial_result}")
