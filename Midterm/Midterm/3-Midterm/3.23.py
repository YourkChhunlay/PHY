# Prompt the user for input
n = int(input("Enter a number: "))
digit_to_check = int(input("Digits to be checked is: "))

# Convert the number to a string to easily check each digit
n_str = str(n)

# Find the position of the digit
position = n_str.rfind(str(digit_to_check)) + 1  # Adding 1 to make it human-readable

# Display the result
print(f"{digit_to_check} is present at the position {position} from right to left.")
