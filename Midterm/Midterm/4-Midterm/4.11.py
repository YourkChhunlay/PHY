# Function to calculate cube of three numbers
def calculate_cube(n1, n2, n3):
    cube1 = n1 ** 3
    cube2 = n2 ** 3
    cube3 = n3 ** 3
    return cube1, cube2, cube3

# Prompt the user for input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

# Calculate and display the cubes
cube_result1, cube_result2, cube_result3 = calculate_cube(n1, n2, n3)
print(f"Cube of {n1}: {cube_result1}")
print(f"Cube of {n2}: {cube_result2}")
print(f"Cube of {n3}: {cube_result3}")
