# Function to calculate factorial recursively
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Prompt the user for input
n = int(input("Enter a number: "))

# Calculate and display the result
factorial_result = recursive_factorial(n)
print(f"Factorial of {n} is: {factorial_result}")
