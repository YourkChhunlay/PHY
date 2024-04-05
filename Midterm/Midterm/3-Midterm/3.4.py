# Prompt the user for input
color_shortcut = input("Enter a shortcut of color name [R, B, G, W, Y]: ")

# Define a dictionary to map shortcuts to full color names
color_mapping = {'R': 'Red', 'B': 'Blue', 'G': 'Green', 'W': 'White', 'Y': 'Yellow'}

# Check if the input is a valid shortcut
if color_shortcut in color_mapping:
    color_name = color_mapping[color_shortcut]
    print(f"Your favorite color is: {color_name}.")
else:
    print("Invalid input. Please enter a valid color shortcut.")
