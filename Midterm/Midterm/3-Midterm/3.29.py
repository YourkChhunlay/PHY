# Prompt the user for input
hour = int(input("Enter the current hour: "))

# Determine the ticket fee based on the time
if hour < 17:
    fee = 100 * hour
else:
    fee = 200 * hour

# Display the result
print(f"The bicycle ticket fee is: {fee} riel.")
