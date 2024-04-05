# Function to calculate series values recursively
def recursive_series(n):
    if n == 0:
        return 0
    else:
        return n + recursive_series(n - 1)

# Prompt the user for input
n = int(input("Enter a number: "))

# Calculate and display the results
sum_result = recursive_series(n)
print(f"Sum = {sum_result}")

# Additional series calculations can be added as needed
