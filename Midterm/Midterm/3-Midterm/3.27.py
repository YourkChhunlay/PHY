# Function to calculate grade based on score
def calculate_grade(score):
    if 91 <= score <= 100:
        return "A"
    elif 81 <= score <= 90:
        return "B"
    elif 71 <= score <= 80:
        return "C"
    elif 61 <= score <= 70:
        return "D"
    elif 50 <= score <= 60:
        return "E"
    elif score < 50:
        return "F"
    else:
        return "Invalid"

# Prompt the user for input
while True:
    score = int(input("Please enter a score: "))
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
