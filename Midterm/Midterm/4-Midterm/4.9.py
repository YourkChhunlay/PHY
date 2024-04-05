# Function to calculate average of five scores
def calculate_average(score1, score2, score3, score4, score5):
    avg = (score1 + score2 + score3 + score4 + score5) / 5
    return avg

# Prompt the user for input
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
score4 = float(input("Enter score 4: "))
score5 = float(input("Enter score 5: "))

# Calculate and display the average
average_result = calculate_average(score1, score2, score3, score4, score5)
print(f"Average: {average_result}")
