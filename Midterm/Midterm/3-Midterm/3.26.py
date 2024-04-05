import math

# Prompt the user for input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
beta = b**2 - 4*a*c

# Check for special case
if a == 0:
    x1 = x2 = -c / b
    print(f"Special Case: x1 = {x1}, x2 = {x2}")
else:
    # Check the discriminant
    if beta < 0:
        print("No Real Roots.")
    elif beta == 0:
        x = -b / (2*a)
        print(f"Real and Equal Roots: x = {x}")
    else:
        x1 = (-b - math.sqrt(beta)) / (2*a)
        x2 = (-b + math.sqrt(beta)) / (2*a)
        print(f"Real and Different Roots: x1 = {x1}, x2 = {x2}")
