# Function to calculate sum, minus, multiply, and division
def calculator(n1, n2):
    sum_result = n1 + n2
    minus_result = n1 - n2
    multiply_result = n1 * n2
    division_result = n1 / n2

    return sum_result, minus_result, multiply_result, division_result

# Prompt the user for input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Calculate and display the results
sum_res, minus_res, multiply_res, division_res = calculator(n1, n2)
print(f"Sum: {sum_res}")
print(f"Minus: {minus_res}")
print(f"Multiply: {multiply_res}")
print(f"Division: {division_res}")
