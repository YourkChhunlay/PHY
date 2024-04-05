# Prompt the user for input
n = int(input("Enter a number: "))
digit_to_check = int(input("Digits to be checked is: "))

# Convert the number to a string to easily check each digit
n_str = str(n)

# Count the occurrences of the digit
count = n_str.count(str(digit_to_check))

# Display the result
print(f"The digit {digit_to_check} is present {count} time(s).")
