# Function to generate grade based on average score
def generate_grade(average_score):
    if 91 <= average_score <= 100:
        return "A"
    elif 81 <= average_score <= 90:
        return "B"
    elif 71 <= average_score <= 80:
        return "C"
    elif 61 <= average_score <= 70:
        return "D"
    elif 50 <= average_score <= 60:
        return "E"
    else:
        return "F"

# Prompt the user for input
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
score4 = float(input("Enter score 4: "))
score5 = float(input("Enter score 5: "))

# Calculate the average
average_result = calculate_average(score1, score2, score3, score4, score5)

# Generate and print the grade
grade_result = generate_grade(average_result)
print(f"Average: {average_result}")
print(f"Grade: {grade_result}")
