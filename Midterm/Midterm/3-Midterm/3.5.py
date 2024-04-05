# Prompt the user for input
num_scores = int(input("How many scores?: "))

# Initialize variables for sum and scores
score_sum = 0

# Loop to input scores and accumulate them
for i in range(1, num_scores + 1):
    score = float(input(f"Score - {i}: "))
    score_sum += score

# Calculate the average
average = score_sum / num_scores

# Display the results
print("===========================")
print(f"The sum = {score_sum}")
print(f"The avg = {average}")
