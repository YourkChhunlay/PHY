# Prompt the user for input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
m = float(input("Enter the value of m: "))
n = float(input("Enter the value of n: "))

# Solve the system of equations
x = (n - c) / a
y = (m - a * x) / b

# Display the result
print(f"The solution is x = {x}, y = {y}")
