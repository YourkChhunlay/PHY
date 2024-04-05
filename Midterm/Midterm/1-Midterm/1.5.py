# Prompt the user for input
math_score = float(input("Please input Math score: "))
physics_score = float(input("Please input Physics score: "))
khmer_score = float(input("Please input Khmer score: "))
chemistry_score = float(input("Please input Chemistry score: "))
english_score = float(input("Please input English score: "))

# Calculate total and average
total_score = math_score + physics_score + khmer_score + chemistry_score + english_score
average_score = total_score / 5

# Display the results
print("The total is:", total_score)
print("The average is:", average_score)
