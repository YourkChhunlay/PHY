import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Prompt the user for input
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the area
area_result = calculate_circle_area(radius)
print(f"Area of the circle: {area_result}")
