# Function to find and print the maximum value
def find_max(n1, n2):
    max_val = max(n1, n2)
    print(f"The maximum value is: {max_val}")

# Prompt the user for input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Find and print the maximum value
find_max(n1, n2)
