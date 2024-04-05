# Prompt the user for input
day_number = int(input("Please input a number [1-7]: "))

# Define a dictionary to map numbers to days
days_mapping = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

# Check if the input is within the valid range
if 1 <= day_number <= 7:
    day_name = days_mapping[day_number]
    print(f"Today is: {day_name}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
