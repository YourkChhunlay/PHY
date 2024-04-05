# Function to check if a number is ODD or EVEN
def check_odd_even(n):
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Prompt the user for input
n = int(input("Enter a number: "))

# Check and display the result
result = check_odd_even(n)
print(f"The number is: {result}")
