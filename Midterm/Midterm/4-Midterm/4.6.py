# Function to find and print the maximum and minimum values
def find_max_min(n1, n2, n3, n4, n5):
    max_val = max(n1, n2, n3, n4, n5)
    min_val = min(n1, n2, n3, n4, n5)
    print(f"The maximum value is: {max_val}")
    print(f"The minimum value is: {min_val}")

# Prompt the user for input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))
n5 = float(input("Enter the fifth number: "))

# Find and print the maximum and minimum values
find_max_min(n1, n2, n3, n4, n5)