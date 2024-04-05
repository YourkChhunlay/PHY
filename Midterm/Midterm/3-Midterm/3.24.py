# Prompt the user for input
num = int(input("Enter a number: "))

# Generate the pattern
for i in range(num, -1, -1):
    print(''.join(str(j) for j in range(i, -1, -1)), end="")
